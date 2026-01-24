import psycopg2
import tkinter as tk
import datetime as dt
import psycopg2.extras
from tkinter import ttk
import tkcalendar



def cerrar_ventana(ventana: tk.Tk) -> None:
    ventana.destroy()
    
def mostrar_interfaz(interfaz: tk.Frame) -> None:
    interfaz.tkraise()

def limpiar_entry(inputs: list) -> None:
    for entry in inputs:
        if isinstance(entry, tk.Entry):
            entry.delete(0, tk.END)
        elif isinstance(entry, tk.Radiobutton):
            entry.deselect()
        elif isinstance(entry, tk.Label):
            entry.config(text="")
        elif isinstance(entry, tk.StringVar):
            entry.set("")

def mensaje(mensaje: tk.Label, texto: str, color: str) -> None:
    mensaje.config(text=texto, bg=color, fg="white")
    mensaje.grid(column=1, row=3, columnspan=3, sticky="ew", padx=20)
    mensaje.after(8000, lambda: mensaje.grid_remove())

def base_datos_conectar() -> psycopg2.extensions.connection:
    conexion = psycopg2.connect(
        host="localhost",
        database="Parking Center",
        user="postgres",
        password="123456"
    )
    return conexion

def comprobar_placa_db(placa: str) -> bool:
    with base_datos_conectar() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM vehiculos WHERE placa = %s AND activo = %s", (placa, True))
            resultado = cursor.fetchone()
            return resultado[0] > 0

def validar_placa(placa: str) -> bool:
    if len(placa) != 6:
        return False
    if not placa[:3].isalpha() or not placa[3:5].isdigit():
        return False
    return True

def registrar_ingreso_db(placalb: tk.Label, tipo_vehiculo: tk.Radiobutton, error_msg: tk.Label, recibo: tk.Frame) -> None:
    placa = placalb.get().upper().strip()
    vehiculo = tipo_vehiculo.get()
    if not validar_placa(placa):
        mensaje(error_msg, "Placa inválida. Formato correcto: AAA111", "red")
        return
    if comprobar_placa_db(placa):
        mensaje(error_msg, "El vehículo ya está dentro del parqueadero.", "red")
        return
    if not vehiculo:
        mensaje(error_msg, "Seleccione un tipo de vehículo.", "red")
        return
    with base_datos_conectar() as conexion:
        with conexion.cursor() as cursor:
            fecha_ingreso = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
            cursor.execute(
                "INSERT INTO vehiculos (placa, tipo, fecha_entrada, activo) VALUES (%s, %s, %s, %s)",
                (placa, vehiculo, fecha_ingreso, True)
            )
            conexion.commit()
            datos={
                "Placa": placa,
                "Tipo_de_vehículo": vehiculo,
                "Fecha_de_ingreso": fecha_ingreso
            }
            limpiar_entry([placalb, tipo_vehiculo])
            recibo_poner_datos(recibo, datos)
            mostrar_interfaz(recibo)
        

def recibo_poner_datos(recibo: tk.Frame, datos: dict) -> None:
    filas=2
    for widget in recibo.winfo_children():
        if hasattr(widget, "clase"):
            clase = widget.clase
            if clase in datos:
                llave=list(datos.keys())[list(datos.keys()).index(clase)]
                valor=datos[clase]
                widget.config(text=f"{llave.replace("_", " ")}: {valor}", relief="solid")
                widget.grid(column=1, row=filas, columnspan=2, sticky="wesn")
                filas+=1

def calcular_cobro(fecha_ingreso: dt.datetime, fecha_salida: dt.datetime, tipo_vehiculo: str) -> int:
    duracion = fecha_salida - fecha_ingreso
    horas = int(round(duracion.total_seconds() / 3600, 0))
    if horas == 0:
        horas = 1
    tarifas = {
        "Moto": 1000,
        "Carro": 2000,
        "Camioneta": 3000
    }
    tarifa_hora = tarifas.get(tipo_vehiculo)
    cobro_total = tarifa_hora * horas
    return cobro_total

def registrar_salida_db(placalb: tk.Label, error_msg: tk.Label, recibo: tk.Frame) -> None:
    placa = placalb.get().upper().strip()
    if not validar_placa(placa):
        mensaje(error_msg, "Placa inválida. Formato correcto: AAA111", "red")
        return
    if not comprobar_placa_db(placa):
        mensaje(error_msg, "La placa no está registrada en el sistema.", "red")
        return
    with base_datos_conectar() as conexion:
        with conexion.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute(
                "SELECT tipo, fecha_entrada FROM vehiculos WHERE placa = %s AND activo = TRUE",
                (placa,)
            )
            resultado = cursor.fetchone()
            if not resultado:
                mensaje(error_msg, "El vehículo ya ha salido o no está registrado.", "red")
                return
            fecha_salida = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
            fecha_salida = dt.datetime.strptime(fecha_salida, "%Y-%m-%d %H:%M")
            cobro_total = calcular_cobro(resultado["fecha_entrada"], fecha_salida, resultado["tipo"])
            cursor.execute(
                "UPDATE vehiculos SET fecha_salida = %s, activo = %s, coste=%s WHERE placa = %s",
                (fecha_salida,False, cobro_total, placa)
            )
            conexion.commit()
            datos={
                "Placa": placa,
                "Tipo_de_vehículo": resultado["tipo"],
                "Fecha_de_ingreso": resultado["fecha_entrada"],
                "Fecha_de_salida": fecha_salida,
                "Cobro": f"${cobro_total}"
            }
            limpiar_entry([placalb])
            recibo_poner_datos(recibo, datos)
            mostrar_interfaz(recibo)

def parqueadero_actual(placa: str | None, tipo: str | None, activo: bool = True, fecha: dt.date | bool = False) -> list:
    with base_datos_conectar() as conexion:
        with conexion.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            comando = "SELECT placa, tipo, fecha_entrada FROM vehiculos WHERE"
            params = []
            if fecha:
                fecha_inicio = dt.datetime.combine(fecha, dt.time.min)
                fecha_fin = dt.datetime.combine(fecha, dt.time.max)
                comando = "SELECT placa, tipo, fecha_entrada, fecha_salida, coste FROM vehiculos WHERE fecha_entrada BETWEEN %s AND %s AND activo = %s"
                params.append(fecha_inicio)
                params.append(fecha_fin)
                params.append(activo)
            if activo:
                comando += " activo = %s"
                params.append(activo)
            if placa:
                comando += " AND placa = %s"
                params.append(placa)
            if tipo:
                comando += " AND tipo = %s"
                params.append(tipo)
            cursor.execute(comando, tuple(params))
            resultados = cursor.fetchall()
            return resultados
        
def poner_info_tabla(tabla: ttk.Treeview, resultados: list) -> None:
    tabla["columns"]=()
    for encabezado in tabla["columns"]:
        tabla.heading(encabezado, text="")
    for vehiculo in tabla.get_children():
        tabla.delete(vehiculo)
    encabezados=tuple(resultados[0].keys())
    tabla.configure(columns=encabezados)
    ancho_tabla=tabla.winfo_width()
    ancho_columna=ancho_tabla//len(encabezados)
    for encabezado in encabezados:
        tabla.heading(encabezado, text=encabezado.replace("_", " "))
        tabla.column(encabezado, width=ancho_columna, anchor="center")
    for vehiculo in resultados:
        tabla.insert("", "end", values=tuple(vehiculo.values()))

        
def mirar_parqueadero(placa: tk.Entry, tipo: tk.StringVar, tabla: ttk.Treeview, interfaz: tk.Frame, error: tk.Label, boton: tk.Button,total: tk.Label, calendario_completo: tuple = None) -> None:
    calendario_completo[0].grid_remove()
    calendario_completo[1].grid_remove()
    total.config(text="")
    
    placa_valor=placa.get().upper().strip() if placa.get().strip() != "" else None
    if placa_valor is not None:
        if not validar_placa(placa_valor):
            mensaje(error, "Placa inválida. Formato correcto: AAA111", "red")
            return
    tipo_valor=tipo.get() if tipo.get() != "" else None
    resultados = parqueadero_actual(placa_valor, tipo_valor)
    poner_info_tabla(tabla, resultados)
    limpiar_entry([placa, tipo])
    boton.config(command=lambda: mirar_parqueadero(placa, tipo, tabla, interfaz, error, boton, total,calendario_completo))
    mostrar_interfaz(interfaz)
    

def mostrar_total_diario(placa: tk.Entry, tipo: tk.StringVar, fecha: tkcalendar.DateEntry,tabla: ttk.Treeview, interfaz: tk.Frame, error: tk.Label, boton: tk.Button,total: tk.Label, calendario_completo: tuple) -> None:
    calendario_completo[0].grid(column=0, row=3, padx=10, pady=10, sticky="nw")
    calendario_completo[1].grid(column=0, row=3, padx=10, pady=10, sticky="we")
    boton.config(command=lambda: mostrar_total_diario(placa, tipo, fecha, tabla, interfaz, error, boton, total, calendario_completo))
    placa_valor=placa.get().upper().strip() if placa.get().strip() != "" else None
    if placa_valor is not None:
        if not validar_placa(placa_valor):
            mensaje(error, "Placa inválida. Formato correcto: AAA111", "red")
            return
    tipo_valor=tipo.get() if tipo.get() != "" else None
    fecha_valor = fecha.get_date()
    resultados = parqueadero_actual(placa_valor, tipo_valor, activo=False, fecha=fecha_valor)
    if not resultados:
        mensaje(error, "No hay registros para la fecha seleccionada.", "red")
        mostrar_interfaz(interfaz)
        return
    total_coste=0
    for vehiculo in resultados:
        total_coste+=vehiculo["coste"]
    total.config(text=f"Costo total del día {fecha_valor}: ${total_coste}")
    poner_info_tabla(tabla, resultados)
    limpiar_entry([placa, tipo, fecha])
    mostrar_interfaz(interfaz)