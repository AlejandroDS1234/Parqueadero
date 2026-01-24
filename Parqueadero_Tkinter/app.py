import tkinter as tk
import funciones as fn
from tkinter import ttk
import tkcalendar 
import datetime as dt


# ventana
ventana = tk.Tk()
ventana.title("Parqueadero")
ventana.attributes("-fullscreen", True)
ventana.bind_all("<Control-g>", lambda e: fn.cerrar_ventana(ventana))


#columnas de la ventana
ventana.configure(bg="#efefef")
ventana.columnconfigure(0, weight=0)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=0)
ventana.columnconfigure(3, weight=1)
ventana.columnconfigure(4, weight=0)

#filas de la ventana
ventana.rowconfigure(0, weight=0)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=2)
ventana.rowconfigure(3, weight=0)
ventana.rowconfigure(4, weight=0)

#franjas superior e inferior
franjas=tk.PhotoImage(file="Parqueadero_Tkinter/botones/log.png")
franja_superior=tk.Label(ventana, image=franjas, bg="#efefef")
franja_superior.grid(column=0, row=0, columnspan=5, padx=0, sticky="ew")

franja_inferior=tk.Label(ventana, image=franjas, bg="#efefef")
franja_inferior.grid(column=0, row=4, columnspan=5, padx=0, sticky="ew")

#mensaje 
mensaje=tk.Label(ventana, bg="#efefef", font=("Arial", 16), anchor="center")



#título
tamaño_titulo=ventana.winfo_screenwidth()//20
titulo=tk.Label(ventana, text="Parking Center", bg="#efefef", relief="groove", font=("Arial", tamaño_titulo, "bold"), anchor="center")
titulo.grid(column=0, row=1, sticky="nswe", columnspan=5)


#----------------------------------------
#interfaz de inicio
inicio=tk.Frame(ventana, bg="#efefef", bd=2, relief="flat")
inicio.grid(column=0, row=2, columnspan=5 ,  sticky="nsew")

#columnas inicio
inicio.columnconfigure(0, weight=1)
inicio.columnconfigure(1, weight=2)
inicio.columnconfigure(2, weight=1)

#filas inicio
inicio.rowconfigure(0, weight=1)
inicio.rowconfigure(1, weight=1)

#botones de inicio
foto_entrada=tk.PhotoImage(file="Parqueadero_Tkinter/botones/ingreso.png")
entrar=tk.Button(inicio, image=foto_entrada, text="Entrar", bg="#efefef", relief="flat", command=lambda: fn.mostrar_interfaz(ingresar_info))
entrar.grid(column=1, row=0, pady=20, sticky="sw")

foto_salir=tk.PhotoImage(file="Parqueadero_Tkinter/botones/salida.png")
salir=tk.Button(inicio, image=foto_salir, text="Salir", bg="#efefef", relief="flat", command=lambda: fn.mostrar_interfaz(salir))
salir.grid(column=1, row=1, pady=20, sticky="nw")

#texto
precios="""Precios del parqueadero:

Moto: $1.000
Carro: $2.000
Camioneta: $3.000"""
tamaño_texto=ventana.winfo_screenwidth()//60

texto_precios=tk.Label(inicio, text=precios, bg="#efefef", font=("Arial", tamaño_texto), justify="center")
texto_precios.grid(column=0, row=0, sticky="nsew", rowspan=2)

#boton inicio en ventana
foto_inicio=tk.PhotoImage(file="Parqueadero_Tkinter/botones/inicio.png").subsample(8,8)
boton_inicio=tk.Button(ventana, image=foto_inicio, bg="#efefef", relief="flat", command=lambda: fn.mostrar_interfaz(inicio))
boton_inicio.grid(column=0, row=3, sticky="wn" , padx=10, pady=10)

#------------------------------------
#menu ingresar info
ingresar_info=tk.Frame(ventana, bg="#efefef", bd=2, relief="flat")
ingresar_info.grid(column=0, row=2, columnspan=5 ,  sticky="nsew")

#columnas ingresar info
ingresar_info.columnconfigure(0, weight=1)
ingresar_info.columnconfigure(1, weight=1)
ingresar_info.columnconfigure(2, weight=0)
ingresar_info.columnconfigure(3, weight=1)
ingresar_info.columnconfigure(4, weight=1)

#filas ingresar info
ingresar_info.rowconfigure(0, weight=1)
ingresar_info.rowconfigure(1, weight=1)
ingresar_info.rowconfigure(2, weight=0)

#ingresar placa
placa_texto=tk.Label(ingresar_info, text="Placa del vehículo (AAA111):", bg="#efefef", font=("Arial", tamaño_texto))
placa_texto.grid(column=2, row=0, sticky="nw", padx=10, pady=10)
placa_entry=tk.Entry(ingresar_info, font=("Arial", tamaño_texto))
placa_entry.grid(column=2, row=0, padx=10, pady=10)

#ingresar tipo de vehículo
tipo_texto=tk.Label(ingresar_info, text="Tipo de vehículo:", bg="#efefef", font=("Arial", tamaño_texto))
tipo_texto.grid(column=2, row=1, sticky="nw", padx=10, pady=10)

vehiculo=tk.StringVar()
tipo_vehiculo=["Moto", "Carro", "Camioneta"]
for i in enumerate(tipo_vehiculo):
    tipo_btn=tk.Radiobutton(ingresar_info, text=i[1], value=i[1], selectcolor="#c4a62e",  bg="#ffde59", indicatoron=False, font=("Arial", tamaño_texto), variable=vehiculo)
    tipo_btn.grid(column=i[0]+1, row=1, sticky="ew", pady=20, padx=10)


#boton ingresar info
recibo=tk.Frame(ventana, bg="#efefef", bd=2, relief="flat")
foto_ingresar=tk.PhotoImage(file="Parqueadero_Tkinter/botones/registrar_ingreso.png")
ingresar=tk.Button(ingresar_info, image=foto_ingresar, bg="#efefef", relief="flat", command=lambda: fn.registrar_ingreso_db(placa_entry, vehiculo, mensaje, recibo))
ingresar.grid(column=2, row=2)


#-------------------------------------
#recibo
recibo.grid(column=0, row=2, columnspan=5 ,  sticky="nsew")


#columnas recibo
recibo.columnconfigure(0, weight=1)
recibo.columnconfigure(1, weight=0)
recibo.columnconfigure(2, weight=0)
recibo.columnconfigure(3, weight=1)

#filas recibo
recibo.rowconfigure(0, weight=1)
recibo.rowconfigure(1, weight=0)
recibo.rowconfigure(2, weight=0)
recibo.rowconfigure(3, weight=0)
recibo.rowconfigure(4, weight=0)
recibo.rowconfigure(5, weight=0)
recibo.rowconfigure(6, weight=0)
recibo.rowconfigure(7, weight=1)

texto_recibo=tk.Label(recibo, text="Ticket", bg="#ffde59", font=("Arial", tamaño_texto+4, "bold"), relief="solid")
texto_recibo.grid(column=1, row=1, sticky="ew", columnspan=2)

placa_recibo=tk.Label(recibo, text="", bg="#efefef", font=("Arial", tamaño_texto))
placa_recibo.clase="Placa"

tipo_vehiculo_recibo=tk.Label(recibo, text="", bg="#efefef", font=("Arial", tamaño_texto))
tipo_vehiculo_recibo.clase="Tipo_de_vehículo"

hora_ingreso_recibo=tk.Label(recibo, text="", bg="#efefef", font=("Arial", tamaño_texto))
hora_ingreso_recibo.clase="Fecha_de_ingreso"

hora_salida_recibo=tk.Label(recibo, text="", bg="#efefef", font=("Arial", tamaño_texto))
hora_salida_recibo.clase="Fecha_de_salida"

cobro=tk.Label(recibo, text="", bg="#efefef", font=("Arial", tamaño_texto, "bold"))
cobro.clase="Cobro"


#-------------------------------
#salir
#menu ingresar info
salir=tk.Frame(ventana, bg="#efefef", bd=2, relief="flat")
salir.grid(column=0, row=2, columnspan=5 ,  sticky="nsew")

#columnas ingresar info
salir.columnconfigure(0, weight=1)
salir.columnconfigure(1, weight=1)
salir.columnconfigure(2, weight=0)
salir.columnconfigure(3, weight=1)
salir.columnconfigure(4, weight=1)

#filas ingresar info
salir.rowconfigure(0, weight=1)
salir.rowconfigure(1, weight=1)
salir.rowconfigure(2, weight=0)

#ingresar placa
placa_texto_salir=tk.Label(salir, text="Placa del vehículo (AAA111):", bg="#efefef", font=("Arial", tamaño_texto))
placa_texto_salir.grid(column=2, row=0, sticky="nw", padx=10, pady=10)
placa_entry_salir=tk.Entry(salir, font=("Arial", tamaño_texto))
placa_entry_salir.grid(column=2, row=0, padx=10, pady=10)

foto_salir_btn=tk.PhotoImage(file="Parqueadero_Tkinter/botones/salir.png")
salir_btn=tk.Button(salir, image=foto_salir_btn, bg="#efefef", relief="flat", command=lambda: fn.registrar_salida_db(placa_entry_salir, mensaje, recibo))
salir_btn.grid(column=2, row=2)

#---------------------------------------
#panel admin

panel_admin=tk.Frame(ventana, bg="#efefef", bd=2, relief="flat")
panel_admin.grid(column=0, row=2, columnspan=5 ,  sticky="nsew")
ventana.bind_all("<Control-a>", lambda e: fn.mostrar_interfaz(panel_admin))
#columnas admin
panel_admin.columnconfigure(0, weight=1)
panel_admin.columnconfigure(1, weight=0)
panel_admin.columnconfigure(2, weight=1)

#filas admin
panel_admin.rowconfigure(0, weight=1)
panel_admin.rowconfigure(1, weight=1)
panel_admin.rowconfigure(2, weight=1)
panel_admin.rowconfigure(3, weight=1)

texto_admin=tk.Label(panel_admin, text="Panel Admin", bg="#efefef", font=("Arial", tamaño_texto+4, "bold"))
texto_admin.grid(column=0, row=0, sticky="ew", columnspan=3)
# botones de admin

foto_consulta=tk.PhotoImage(file="Parqueadero_Tkinter/botones/consulta_parqueadero.png")
consulta=tk.Button(panel_admin, image=foto_consulta, bg="#efefef", relief="flat", command=lambda: fn.mirar_parqueadero(placa_filtro, opcion, resultado_parqueadero, parqueadero_actual, mensaje, buscar, costo_total,calendario_completo))
consulta.grid(column=1, row=1, pady=5, sticky="w")

foto_total_diario=tk.PhotoImage(file="Parqueadero_Tkinter/botones/total_diario.png")
total_diario=tk.Button(panel_admin, image=foto_total_diario, bg="#efefef", relief="flat", command=lambda: fn.mostrar_total_diario(placa_filtro, opcion, calendario, resultado_parqueadero, parqueadero_actual, mensaje,buscar, costo_total, calendario_completo))
total_diario.grid(column=1, row=2, pady=5, sticky="w")

foto_salir_app=tk.PhotoImage(file="Parqueadero_Tkinter/botones/salir_del_app.png")
salir_app=tk.Button(panel_admin, image=foto_salir_app, bg="#efefef", relief="flat", command=lambda: fn.cerrar_ventana(ventana))
salir_app.grid(column=1, row=3, pady=5, sticky="w")


#--------------------------------
#interfaz parqueadero actual y total diario
parqueadero_actual=tk.Frame(ventana, bg="#efefef", bd=2, relief="flat")
parqueadero_actual.grid(column=0, row=2, columnspan=5 ,  sticky="nsew")

#columnas parqueadero actual
parqueadero_actual.columnconfigure(0, weight=0)
parqueadero_actual.columnconfigure(1, weight=1)
parqueadero_actual.columnconfigure(2, weight=1)
parqueadero_actual.columnconfigure(3, weight=1)

#filas parqueadero actual
parqueadero_actual.rowconfigure(0, weight=0)
parqueadero_actual.rowconfigure(1, weight=1)
parqueadero_actual.rowconfigure(2, weight=1)
parqueadero_actual.rowconfigure(3, weight=1)
parqueadero_actual.rowconfigure(4, weight=1)

#filtros
texto_tipo_vehiculo=tk.Label(parqueadero_actual, text="Filtrar por tipo de vehículo:", bg="#efefef", font=("Arial", tamaño_texto-4))
texto_tipo_vehiculo.grid(column=0, row=1, padx=10, pady=20, sticky="nw")

opcion=tk.StringVar()
tipo_vehiculo_filtro=ttk.Combobox(parqueadero_actual,
                                  textvariable=opcion,
                                  values=["", "Moto", "Carro", "Camioneta"],
                                  state="readonly",
                                  font=("Arial", tamaño_texto)
                                  )

tipo_vehiculo_filtro.current(0)
tipo_vehiculo_filtro.grid(column=0, row=1, padx=10, pady=20, sticky="sew")

texto_placa_filtro=tk.Label(parqueadero_actual, text="Filtrar por placa:", bg="#efefef", font=("Arial", tamaño_texto))
texto_placa_filtro.grid(column=0, row=2, padx=10, pady=10, sticky="nw")
placa_filtro=tk.Entry(parqueadero_actual, font=("Arial", tamaño_texto))
placa_filtro.grid(column=0, row=2, padx=10, pady=10, sticky="swe")

texto_calendario=tk.Label(parqueadero_actual, text="Filtrar por fecha:", bg="#efefef", font=("Arial", tamaño_texto))
texto_calendario.grid(column=0, row=3, padx=10, pady=10, sticky="nw")
calendario=tkcalendar.DateEntry(parqueadero_actual,
                                date_pattern="yyyy-mm-dd",
                                year=dt.datetime.now().year,
                                month=dt.datetime.now().month,
                                day=dt.datetime.now().day,
                                font=("Arial", tamaño_texto-6))
calendario.grid(column=0, row=3, padx=10, pady=10, sticky="swe")
calendario_completo=(texto_calendario, calendario)

buscar=tk.Button(parqueadero_actual, text="Buscar", bg="#ffde59", font=("Arial", tamaño_texto), relief="flat", command=lambda: fn.mostrar_total_diario(placa_filtro, opcion, calendario, resultado_parqueadero, parqueadero_actual, mensaje, buscar,costo_total, calendario_completo))
buscar.grid(column=0, row=4, padx=10, sticky="ews")

#tabla de resultados
decoracion = ttk.Style()
decoracion.theme_use("default")
decoracion.configure("Treeview", font=("Arial", tamaño_texto), background="#efefef", rowheight=tamaño_texto+12)
decoracion.configure("Treeview.Heading", font=("Arial", tamaño_texto, "bold"), background="#ffde59")
resultado_parqueadero=ttk.Treeview(parqueadero_actual,show="headings",height=10)

resultado_parqueadero.grid(column=1, row=1, columnspan=3, rowspan=3, padx=20, pady=20, sticky="nsew")

costo_total=tk.Label(parqueadero_actual, text="", bg="#ffde59", font=("Arial", tamaño_texto, "bold"))
costo_total.grid(column=1, row=4, columnspan=3, padx=20, sticky="ew")

if __name__ == "__main__":
    inicio.tkraise()
    ventana.mainloop()