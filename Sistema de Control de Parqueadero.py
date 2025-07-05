historial=[]
vehiculos=[]
precios={"MOTO":1000,"CARRO":2000,"CAMIONETA":2500}
meses={"01":31,"02":29,"03":31,"04":30,"05":31,"06":30,"07":31,"08":31,"09":30,"10":31,"11":30,"12":31}

while True:
    print("\n\n")
    print("PARQUEADERO".center(100,"="))
    print(f"\nEl precio por hora para cada vehiculo es:\n{precios}\n")
    print("\n Para entrar un nuevo vehiculo al parqueadero ingrese 'E'\n Para sacar un vehiculo del parqueadero ingrese 'S'\n Para ver mas opciones del programa ingrese 'X'\n")
    entrada=input("\nIngrese la accion que va a realizar: ").upper()
    #entrada
    if entrada=="E":
        #placa
        comprobador_placa=0
        while True:
            if comprobador_placa==1:
                break
            placa=input("\nIngrese la placa del vehiculo (AAA000): ").upper()
            #detectar errores en la placa
            if len(placa)!=6:#longitud de la placa
                print("Placa no valida vuelva a intentarlo\n") 
                continue #si detecta un error vuelve al inicio del bucle a predir el codigo
            elif placa[0:3].isalpha()==False or placa[3:5].isdigit()==False: #ver los caracteres de la placa
                print("Placa no valida vuelva a intentarlo\n")
                continue #si detecta un error vuelve al inicio del bucle a predir el codigo
            else:
                contador_placa=0
                while True:
                    if comprobador_placa==1:
                        comprobador_placa=0
                        break
                    if len(vehiculos)==0:
                        break
                        
                    if placa==vehiculos[contador_placa][0]:
                        print("El vehiculo ya esta ingresado en el parqueadero, no lo puede ingresar de nuevo\n")
                        comprobador_placa=1
                        break
                    else:
                        contador_placa+=1
                        if contador_placa>=len(vehiculos):
                            break #si no hay errores con la placa sale del bucle de pedir la placa y continua con el siguiente
            if comprobador_placa==1:
                continue
            else:
                break
        if comprobador_placa==1:
            continue



        #tipo de vehiculo
        while True:
            tipo=input("\nIngrese el tipo de vehiculo (Moto, Carro, Camioneta): ").upper()#pide el tipo de vehiculo y lo pone en mayusculas
            #detectar errores en el tipo de vehiculo
            if tipo=="MOTO" or tipo=="CARRO" or tipo=="CAMIONETA": #verifica si el tipo que se ingreso es uno de los 3 validos
                break #si es valido sale del bucle de pedir el tipo del vehiculo
            else: #detectar si el vehiculo que se ingreso no esta entre los vehiculos validos
                print("Tipo de vehiculo no valido, vuelva a intentar\n")
                continue  #si detecta que no es valido regresa al inicio del bucle a pedir el tipo de vehiculo
        while True:
            hora_entrada,minutos_entrada=input("\nIngrese la hora de entrada (HH:MM): ").split(":") #Divide la cadena de caracteres en datos según el caracter que se le asignó
            if int(hora_entrada)>24 or int(hora_entrada)<0 or int(minutos_entrada)>59 or int(minutos_entrada)<0: 
                print("Hora no valida, vuelva a intentarlo\n")
                continue #Sí se cumple una de esas condiciones, se volverá a repetir el bucle por el continue
            elif len(hora_entrada)>2 or len(hora_entrada)<1: #Cuenta los dígitos de la hora de entrada y la hora de salida para asegurarse de que estén bien ingresados los datos
                print("Hora mal ingresada, tiene que ser en formato 24h, vuelva a intentarlo\n")
                continue
            else:
                if len(hora_entrada)==1:
                    hora_entrada=f"{0}{hora_entrada}" #Sí la hora que ingresa el usuario sólo tiene 1 dígito, se le agregará un 0 antes de imprimir la hora (ej: pasa la hora 3:30 -> 03:30)
                if len(minutos_entrada)==1:
                    minutos_entrada=f"{0}{minutos_entrada}" #Sí los minutos que ingresa el usuario sólo tienen 1 dígito, se le agregará un 0 antes de imprimir los minutos (ej: 11:05)
                hora_entrada_=(hora_entrada,minutos_entrada)
                break 
        while True:
            fecha_entrada_dia,fecha_entrada_mes=input("\nIngrese la fecha de entrada (DD/MM): ").split("/") #Se nombran 2 variables a las que se les asigna un input, donde se divide el dato del input con un .split en 2 datos diferentes, donde se les asigna a las variables nombradas
            if len(fecha_entrada_dia)>2 or len(fecha_entrada_dia)<1 or len(fecha_entrada_mes)>2 or len(fecha_entrada_mes)<1: #Creamos 2 len para cada variable para que cuenten sus dígitos y reinicie el bucle cuando el usuario ingrese más de 2 dígitos o menos de 1 dígito 
                print("Fecha mal ingresada, tiene que ser en formato DD/MM, vuelva a intentarlo\n")
                continue
            if len(fecha_entrada_dia)==1:
                fecha_entrada_dia=f"{0}{fecha_entrada_dia}" #Se cuentan los caracteres de la variable, donde si es igual a 1, se le agregue un 0 antes de imprimir el dígito que ingresó el usuario (ej: pasa de 9 a 09 -> 09/11)
            if len(fecha_entrada_mes)==1:
                fecha_entrada_mes=f"{0}{fecha_entrada_mes}" #Se cuentan los caracteres de la variable, donde si es igual a 1, se le agregue un 0 antes de imprimir el dígito que ingresó el usuario (ej: pasa de 3 a 03 -> 23/04)
            
            #meses
            if int(fecha_entrada_mes)<=12 and int(fecha_entrada_mes)>=1: #Se asegura de que el número del mes ingresado por el usuario esté entre el 1 y el 12
                if fecha_entrada_mes=="01" or fecha_entrada_mes=="03" or fecha_entrada_mes=="05" or fecha_entrada_mes=="07" or fecha_entrada_mes=="08" or fecha_entrada_mes=="10" or fecha_entrada_mes=="12": #Mira sí el mes ingresado por el usuario es alguno de los que tienen 31 días
                    if int(fecha_entrada_dia)>31 or int(fecha_entrada_dia)<1:
                        print("Fecha incorrecta, el mes tiene 31 dias, vuelva a intentarlo\n") 
                        continue #Hace que el usuario vuelva a ingresar la fecha cuando el día que ingresa es mayor a 31 o menor a 1 (negativo)
                    else:
                        break #Rompe el bucle para continuar cuando el usuario ingresa la fecha correctamente
                elif fecha_entrada_mes=="04" or fecha_entrada_mes=="06" or fecha_entrada_mes=="09" or fecha_entrada_mes=="11": #Mira si el mes ingresado por el usuario es uno de los que tienen 30 días
                    if int(fecha_entrada_dia)>30 or int(fecha_entrada_dia)<1:
                        print("Fecha incorrecta, el mes tiene 30 dias, vuelva a intentar\n")
                        continue #Hace que el usuario vuelva a ingresar la fecha cuando el día que ingresa es mayor a 30 o menor a 1 (negativo)
                    else:
                        break #Rompe el bucle para continuar cuando el usuario ingresa la fecha correctamente
                elif fecha_entrada_mes=="02": #Mira sí el mes que ingresó el usuario tiene 29 días (Febrero/Año biciesto)
                    if int(fecha_entrada_dia)>29 or int(fecha_entrada_dia)<1:
                        print("Fecha incorrecta, el mes tiene maximo 29 dias, vuelva a intentar\n")
                        continue #Hace que el usuario vuelva a ingresar la fecha cuando el día que ingresa es mayor a 29 o menor a 1 (negativo)
                    else:
                        break #Rompe el bucle cuando el usuario ingresa la fecha correctamente
            else:
                print("fecha incorrecta, el mes no existe, vuelva a intentar\n")
                continue  #Hace que el usuario vuelva a ingresar la fecha cuando ingresa un número que no pertenece a ningún mes
        fecha_entrada=(fecha_entrada_dia,fecha_entrada_mes)
        
        
        vehiculos.append((placa,tipo,hora_entrada_,fecha_entrada)) #Agresa los datos que ingresa el usuario (placa, tipo, hora de entrada y fecha de entrada) a la lista de vehiculos
        print(f"\nLos datos ingresados son:\nPlaca: {placa}\nTipo: {tipo}\nHora de entrada: {hora_entrada_[0]}:{hora_entrada_[1]}\nFecha de entrada: {fecha_entrada[0]}/{fecha_entrada[1]}")
            
    #salida
    elif entrada=="S":
        if len(vehiculos)!=0:
            while True:    
                placa_salida=input("\nIngrese la placa de su vehiculo para salir: ").upper()
                if len(placa_salida)!=6: #longitud de la placa
                    print("Placa no valida vuelva a intentarlo\n") 
                    continue #Sí la longitud de la placa es diferente a 6, vuelve al inicio del bucle a pedir la placa
                elif placa_salida[0:3].isalpha()==False or placa_salida[3:5].isdigit()==False: #ver los caracteres de la placa
                    print("Placa no valida vuelva a intentarlo\n")
                    continue #Sí la placa no tiene los caracteres correctos, vuelve al inicio del bucle a pedir la placa
                else:
                    break #si no hay errores con la placa sale del bucle de pedir la placa y continua con el siguiente
            contador=0
            while True:
                if vehiculos[contador][0]==placa_salida: #verifica que la placa de salida que ingresó el usuario esté en la lista de vehiculos
                    while True:
                        hora_salida,minutos_salida=input("\nIngrese la hora de salida (HH:MM): ").split(":") #Divide la cadena de caracteres (la hora) en datos según el caracter que se le asignó
                        if int(hora_salida)>24 or int(hora_salida)<0 or int(minutos_salida)>59 or int(minutos_salida)<0: #verifica que la hora y los minutos ingresados por el usuario estén dentro de los rangos correctos
                            print("Hora no valida, vuelva a intentarlo\n")
                            continue #Sí la hora ingresada por el usuario es mayor a 24 o menor a 0, o los minutos son mayores a 59 o menores a 0, se vuelve a pedir la hora de salida
                        elif len(hora_salida)>2 or len(hora_salida)<1: 
                            print("Hora mal ingresada, tiene que ser en formato 24h, vuelva a intentarlo\n")
                            continue #Sí los caracteres de la hora ingresada por el usuario son mayor a 2 o menor a 1, se vuelve a repetir el bucle para pedir la hora de salida de nuevo
                        else:
                            if len(hora_salida)==1: #Cuenta los caracteres de la variable, donde si es igual a 1, se le agregue un 0 antes de imprimir la hora (ej: pasa de 3 a 03 -> 03:30)
                                hora_salida=f"{0}{hora_salida}"
                            if len(minutos_salida)==1: #Cuenta los caracteres de la variable, donde si es igual a 1, se le agregue un 0 antes de imprimir los minutos (ej: pasa de 5 a 05 -> 11:05)
                                minutos_salida=f"{0}{minutos_salida}" 
                            hora_salida_=(hora_salida,minutos_salida) #Se crea una variable que almacena la hora de salida y los minutos de salida en una tupla
                            break #Rompe el bucle cuando ya la hora de salida y los minutos de salida son correctos
                    while True:
                        fecha_salida_dia,fecha_salida_mes=input("\nIngrese la fecha de salida (DD/MM): ").split("/") #Divide la cadena de caracteres (la fecha) en datos según el caracter asignado
                        if len(fecha_salida_dia)>2 or len(fecha_salida_dia)<1 or len(fecha_salida_mes)>2 or len(fecha_salida_mes)<1: 
                            print("Fecha mal ingresada, tiene que ser en formato DD/MM, vuelva a intentarlo\n") 
                            continue #Vuelve a iniciar el bucle, pidiéndole al usuario que ingrese la fecha de salida de nuevo cuando la fecha ingresada tiene más de 2 dígitos o menos de 1 dígito
                        if len(fecha_salida_dia)==1:
                            fecha_salida_dia=f"{0}{fecha_salida_dia}" #Sí  el día de la fecha de salida ingresada por el usuario sólo tiene 1 dígito, se le agregará un 0 antes de imprimir el día (ej: pasa de 9 a 09 -> 09/11)
                        if len(fecha_salida_mes)==1:
                            fecha_salida_mes=f"{0}{fecha_salida_mes}" #Sí el mes de la fecha de salida ingresada por el usuario sólo tiene 1 dígito, se le agregará un 0 antes de imprimir el mes (ej: pasa de 4 a 04 -> 23/04)
            
                        #meses
                        if int(fecha_salida_mes)<=12 and int(fecha_salida_mes)>=1:
                            if fecha_salida_mes=="01" or fecha_salida_mes=="03" or fecha_salida_mes=="05" or fecha_salida_mes=="07" or fecha_salida_mes=="08" or fecha_salida_mes=="10" or fecha_salida_mes=="12": #Verifica que el mes ingresado por el usuario sea uno de los que tienen 31 días
                                if int(fecha_salida_dia)>31 or int(fecha_salida_dia)<1:
                                    print("Fecha incorrecta, el mes tiene 31 dias, vuelva a intentarlo\n")
                                    continue  #Vuelve a iniciar el bucle, pidiéndole al usuario que ingrese la fecha de salida de nuevo cuando ingresa un mes de 31 días y el día que ingresa es mayor a 31 o menor a 1 (negativo)
                                else: 
                                    break #Rompe el bucle cuando el usuario ingresa la fecha correctamente
                            elif fecha_salida_mes=="04" or fecha_salida_mes=="06" or fecha_salida_mes=="09" or fecha_salida_mes=="11": #Verifica que el mes ingresado por el usuario sea uno de los que tienen 30 días
                                if int(fecha_salida_dia)>30 or int(fecha_salida_dia)<1:
                                    print("Fecha incorrecta, el mes tiene 30 dias, vuelva a intentar\n")
                                    continue #Vuelve a iniciar el bucle, pidiéndole al usuario que ingrese la fecha de salida de nuevo cuando ingresa un mes de 30 días y el día que ingresa es mayor a 30 o menor a 1 (negativo)
                                else:
                                    break #Rompe el bucle cuando el usuario ingresa la fecha correctamente
                            elif fecha_salida_mes=="02":
                                if int(fecha_salida_dia)>29 or int(fecha_salida_dia)<1: #Verifica que el mes ingresado por el usuario sea Febrero (posibilidad de año biciesto)
                                    print("Fecha incorrecta, el mes tiene maximo 29 dias, vuelva a intentar\n")
                                    continue #Vuelve a iniciar el bucle, pidiéndole al usuario que ingrese la fecha de salida de nuevo cuando ingresa el mes 2 (febrero) y el día que ingresa es mayor a 29 o menor a 1 (negativo)
                                else:
                                    break #Rompe el bucle cuando el usuario ingresa la fecha correctamente
                        else:
                            print("fecha incorrecta, el mes no existe, vuelva a intentar\n")
                            continue #Vuelve a iniciar el bucle, pidiéndole al usuario que ingrese la fecha de salida de nuevo cuando ingresa un mes que no existe
                    fecha_salida=(fecha_salida_dia,fecha_salida_mes) #Se crea una variable que almacena la fecha de salida (día y mes) en una tupla


                    hora_minutos_entrada=(int(vehiculos[contador][2][0])*60)+int(vehiculos[contador][2][1]) #Convierte la hora de entrada en minutos para sumarla con los minutos de entrada
                    hora_minutos_salida=(int(hora_salida)*60)+int(minutos_salida) #Convierte la hora de salida en minutos para sumarla con los minutos de salida y obtener el tiempo total de parqueo de los vehículos en minutos
                    #mismo mes
                    if fecha_salida[1]==vehiculos[contador][3][1]: 
                        dias_parqueo=int(fecha_salida[0])-int(vehiculos[contador][3][0]) #Sirve para calcular la diferencia de días entre la fecha de entrada y la fecha de salida del vehículo, dando así los días de parqueo
                        if dias_parqueo<0:
                            print("Datos de salida incorrectos, ingrese los datos nuevamente\n")
                            continue #Vuelve a iniciar el bucle, pidiéndole al usuario que ingrese la fecha de salida de nuevo cuando la fecha de salida es menor a la fecha de entrada
                        else:
                            horas_parqueo=hora_minutos_salida-hora_minutos_entrada #Calcula la diferencia de horas entre la hora de entrada y la hora de salida del vehículo
                            if int(vehiculos[contador][3][0])==int(fecha_salida[0]):
                                if horas_parqueo<0:
                                    print("Datos de salida incorrectos, ingrese los datos nuevamente\n")
                                    continue
                                else:
                                    horas_parqueo=round(horas_parqueo/60,2) #Pasa el tiempo de parqueo de minutos a horas, y luego el resultado se redondea a 2 decimales
                                    dias_parqueo*=24 #Convierte los días de parqueo a horas multiplicando por 24
                                    horas_parqueo+=dias_parqueo #Suma las horas de parqueo con los días de parqueo ya pasados a horas
                                    total_pagar=horas_parqueo*precios[vehiculos[contador][1]] #Calcula el total a pagar por el tiempo de parqueo multiplicando las horas totales de parqueo por el precio del tipo de vehículo que ingresó el usuario
                                    print(f" Su vehiculo estubo {horas_parqueo} horas en el parqueadero ".center(20,"-"),"\n",f" Debe pagar: {total_pagar}$ ".center(20,"-")) #Imprime el tiempo total de parqueo y el total a pagar por el tiempo de parqueo (los .center son para poner en medio el texto con caracteres de relleno, en este caso guiones)
                                    historial.append((vehiculos[contador],(total_pagar,hora_salida,fecha_salida))) #Agrega los datos del vehículo, el total a pagar, la hora de salida y la fecha de salida al historial para tener los registros del parqueadero
                                    vehiculos.remove(vehiculos[contador]) #Elimina el vehículo que salió de la lista de los vehículos en el parqueadero
                                    break #Rompe el bucle cuando ya se ha terminado de tomar el registro del vehículo que salió del parqueadero
                            elif int(vehiculos[contador][3][0])>int(fecha_salida[0]):
                                print("Datos de salida incorrectos, ingrese los datos nuevamente\n")
                                continue
                            else:
                                horas_parqueo=round(horas_parqueo/60,2) #Pasa el tiempo de parqueo de minutos a horas, y luego el resultado se redondea a 2 decimales
                                dias_parqueo*=24 #Convierte los días de parqueo a horas multiplicando por 24
                                horas_parqueo+=dias_parqueo #Suma las horas de parqueo con los días de parqueo ya pasados a horas
                                total_pagar=horas_parqueo*precios[vehiculos[contador][1]] #Calcula el total a pagar por el tiempo de parqueo multiplicando las horas totales de parqueo por el precio del tipo de vehículo que ingresó el usuario
                                print(f" Su vehiculo estubo {horas_parqueo} horas en el parqueadero ".center(20,"-"),"\n",f" Debe pagar: {total_pagar}$ ".center(20,"-")) #Imprime el tiempo total de parqueo y el total a pagar por el tiempo de parqueo (los .center son para poner en medio el texto con caracteres de relleno, en este caso guiones)
                                historial.append((vehiculos[contador],(total_pagar,hora_salida,fecha_salida))) #Agrega los datos del vehículo, el total a pagar, la hora de salida y la fecha de salida al historial para tener los registros del parqueadero
                                vehiculos.remove(vehiculos[contador]) #Elimina el vehículo que salió de la lista de los vehículos en el parqueadero
                                break #Rompe el bucle cuando ya se ha terminado de tomar el registro del vehículo que salió del parqueadero


                    elif int(fecha_salida[1])>int(vehiculos[contador][3][1]): #Verifica sí la fecha de salida es mayor a la fecha de entrada del vehículo
                        contador_dias=vehiculos[contador][3][1] #Obtiene el mes de la fecha de entrada del vehículo
                        dias_parqueo=0 
                        while int(contador_dias)<=int(fecha_salida[1]): 
                            dias_parqueo+=meses[contador_dias]  #Mientras el mes de la fecha de entrada sea menor o igual al mes de la fecha de salida, se suman los días de parqueo
                            if int(contador_dias)<10:
                                contador_dias=f"{0}{int(contador_dias)+1}" #Agrega un 0 antes del número del mes sí es menor a 10 para que tenga el formato correcto 
                            else:
                                contador_dias=int(contador_dias)+1
                        dias_parqueo-=meses[fecha_salida[1]]-int(fecha_salida[0]) #Resta los días del mes de la fecha de salida menos el día de la fecha de salida ingresada por el usuario
                        dias_parqueo-=int(vehiculos[contador][3][0]) #Resta el día de la fecha de entrada del vehículo a los días de parqueo calculados
                        dias_parqueo*=24 #Convierte los días de parqueo a horas multiplicando por 24
                        if dias_parqueo<0:
                            print("Datos de salida incorrectos, ingrese los datos nuevamente\n")
                            continue #Vuelve a iniciar el bucle, pidiéndole al usuario que ingrese la fecha de salida de nuevo sí la fecha de salida es menor a la fecha de entrada
                        else:
                            hora_minutos_entrada=(int(vehiculos[contador][2][0])*60)+int(vehiculos[contador][2][1]) #Convierte la hora de entrada en minutos para sumarla con los minutos de entrada
                            hora_minutos_salida=(int(hora_salida)*60)+int(minutos_salida) #Convierte la hora de salida en minutos para sumarla con los minutos de salida y obtener el tiempo total de parqueo de los vehículos en minutos
                            horas_parqueo=hora_minutos_salida-hora_minutos_entrada #Calcula la diferencia de horas entre la hora de entrada y la hora de salida del vehículo
                            if horas_parqueo<0:
                                print("Datos de salida incorrectos, ingrese los datos nuevamente\n")
                                continue #Vuelve a iniciar el bucle, pidiéndole al usuario que ingrese los datos de salida de nuevo cuando se ingresan de manera incorrecta
                            else:
                                horas_parqueo=round(horas_parqueo/60,2) #Pasa el tiempo de parqueo de minutos a horas, y luego el resultado es redondeado a 2 decimales
                                horas_parqueo+=dias_parqueo #Suma las horas de parqueo con los días de parqueo ya pasados a horas
                                total_pagar=horas_parqueo*precios[vehiculos[contador][1]] #Calcula el total a pagar por el tiempo de parqueo multiplicando las horas totales de parqueo por el precio del tipo de vehículo que ingresó el usuario
                                print(f" Su vehiculo estubo {horas_parqueo} horas en el parqueadero ".center(20,"-"),"\n",f" Debe pagar: {total_pagar}$ ".center(20,"-")) #Imprime el tiempo total de parqueo y el total a pagar por el tiempo de parqueo (los .center son para poner en medio el texto con caracteres de relleno, en este caso guiones)
                                historial.append((vehiculos[contador],(total_pagar,hora_salida,fecha_salida))) #Agrega los datos del vehículo, el total a pagar, la hora de salida y la fecha de salida al historial para tener los registros del parqueadero
                                vehiculos.remove(vehiculos[contador]) #Elimina el vehículo que salió de la lista de los vehículos en el parqueadero
                                break #Rompe el bucle cuando ya se ha terminado de tomar el registro del vehículo que salió del parqueadero
                                
                    elif int(fecha_salida[1])<int(vehiculos[contador][3][1]):
                        print("Datos de salida incorrectos, ingrese los datos nuevamente\n")
                        continue #Vuelve a iniciar el bucle, pidiéndole al usuario que ingrese los datos de salida de nuevo cuando la fecha de salida es menor a la fecha de entrada del vehículo
                else:
                    contador+=1
                    if contador>len(vehiculos):
                        print("El vehiculo no esta registrado en el parqueadero\n")
                        break #Sí no se encuentra la placa del vehículo en la lista de vehículos, se le notificará al usuario y se romperá el bucle para que pueda volver a intentarlo
        else:
            print("No hay vehiculos en el parqueadero\n") 

    elif entrada=="X": #Sí el usuario ingresa 'X', se le mostrarán las opciones del programa
        print("\n\n")
        print("Opciones del programa".center(20,"-")) #Imprime el título centrado con guiones
        print("\ningrese 1 para ver las vehiculos adentro del parqueadero\nIngrese 2 para ver el reporte de ingresos por un dia\nIngrese 3 para volver al menu inicial\nIngrese 4 para salir del programa")
        ajustes=int(input("Ingrese la accion que desee realizar: ")) #Pide al usuario que ingrese una opción del menú de ajustes 
        if ajustes==1:
            if len(vehiculos)!=0: #Cuenta la cantidad de vehículos en el parqueadero
                contador_vehiculos=0
                print("\nLos vehiculos en el parqueadero actualmente son:")
                while len(vehiculos)>contador_vehiculos:
                    print("".center(100,"="))
                    print(f"{(vehiculos[contador_vehiculos][1]).lower()} con placa {vehiculos[contador_vehiculos][0]}\n    Hora de entrada: {vehiculos[contador_vehiculos][2][0]}:{vehiculos[contador_vehiculos][2][1]}\n    Fecha de entrada: {vehiculos[contador_vehiculos][3][0]}/{vehiculos[contador_vehiculos][3][1]}\n")
                    print("".center(100,"="))
                    contador_vehiculos+=1
                print(f"\n\n Hay un total de {len(vehiculos)} en el interior del parqueadero actualmente\n")
            else:
                print("\nNo hay ningun vehiculo en el parqueadero") #Sí la cantidad de vehículos es igual a 0, muestra un mensaje indicando que no hay vehículos en el parqueadero
        elif ajustes==2:
            while True:
                fecha_ajustes_dia,fecha_ajustes_mes=input("\nIngrese la fecha para el reporte de ingresos diario (DD/MM): ").split("/") #Combina la fecha de ajustes en una variable, donde se divide el dato del input con un .split en 2 datos diferentes, donde se les asigna a las variables nombradas
                if len(fecha_ajustes_dia)>2 or len(fecha_ajustes_dia)<1 or len(fecha_ajustes_mes)>2 or len(fecha_ajustes_mes)<1: #Cuenta los dígitos de la fecha de ajustes para asegurarse de que estén bien ingresados los datos
                    print("Fecha mal ingresada, tiene que ser en formato DD/MM, vuelva a intentarlo\n")
                    continue #Vuelve a iniciar el bucle, pidiéndole al usuario que ingrese la fecha de ajustes de nuevo con el formato indicado
                if len(fecha_ajustes_dia)==1:
                    fecha_ajustes_dia=f"{0}{fecha_ajustes_dia}" #Sí los dígitos del día de la fecha de ajustes son igual a 1, se le agregará un 0 antes de imprimir el dígito que ingrese el usuario (ej: pasa de 8 a 08 -> 08/12)
                if len(fecha_ajustes_mes)==1:
                    fecha_ajustes_mes=f"{0}{fecha_ajustes_mes}" #Sí los dígitos del mes de la fecha de ajustes son igual a 1, se le agregará un 0 antes de imprimir el dígito que ingrese el usuario (ej: pasa de 5 a 05 -> 23/05)
            
                #meses
                if int(fecha_ajustes_mes)<=12 and int(fecha_ajustes_mes)>=1: #Verifica que el número del mes ingresado por el usuario esté entre el 1 y el 12
                    if fecha_ajustes_mes=="01" or fecha_ajustes_mes=="03" or fecha_ajustes_mes=="05" or fecha_ajustes_mes=="07" or fecha_ajustes_mes=="08" or fecha_ajustes_mes=="10" or fecha_ajustes_mes=="12": #Verifica que el mes ingresado por el usuario sea uno de los que tienen 31 días
                        if int(fecha_ajustes_dia)>31 or int(fecha_ajustes_dia)<1:
                            print("Fecha incorrecta, el mes tiene 31 dias, vuelva a intentarlo\n")
                            continue #Vuelve a iniciar el bucle, pidiéndole al usuario que ingrese la fecha de nuevo cuando ingresa un mes de 31 días y el día que ingresa es mayor a 31 o menor a 1 (negativo)
                        else:
                            break #Rompe el bucle cuando el usuario ingresa la fecha correctamente
                    elif fecha_ajustes_mes=="04" or fecha_ajustes_mes=="06" or fecha_ajustes_mes=="09" or fecha_ajustes_mes=="11": #Verifica que el mes ingresado por el usuario sea uno de los que tienen 30 días
                        if int(fecha_ajustes_dia)>30 or int(fecha_ajustes_dia)<1:
                            print("Fecha incorrecta, el mes tiene 30 dias, vuelva a intentar\n")
                            continue #Vuelve a iniciar el bucle, pidiéndole al usuario que ingrese la fecha de nuevo cuando ingresa un mes de 30 días y el día que ingresa es mayor a 30 o menor a 1 (negativo)
                        else:
                            break #Rompe el bucle cuando el usuario ingresa la fecha correctamente
                    elif fecha_ajustes_mes=="02": #Verifica que el mes ingresado por el usuario sea Febrero (posibilidad de año biciesto)
                        if int(fecha_ajustes_dia)>29 or int(fecha_ajustes_dia)<1:
                            print("Fecha incorrecta, el mes tiene maximo 29 dias, vuelva a intentar\n")
                            continue #Vuelve a iniciar el bucle, pidiéndole al usuario que ingrese la fecha de nuevo cuando ingresa el mes 2 (febrero) y el día que ingresa es mayor a 29 o menor a 1 (negativo)
                        else:
                            break #Rompe el bucle cuando el usuario ingresa la fecha correctamente
                else:
                    print("fecha incorrecta, el mes no existe, vuelva a intentar\n")
                    continue #Vuelve a iniciar el bucle, pidiéndole al usuario que ingrese la fecha de nuevo cuando ingresa un mes que no existe
            fecha_ajustes=(fecha_ajustes_dia,fecha_ajustes_mes) 
            dia_reporte=[]
            ajustes_dia_reporte=0
            while ajustes_dia_reporte<len(historial): #Recorre el historial de vehículos para buscar los reportes del día especificado
                if historial[ajustes_dia_reporte][1][2]==fecha_ajustes: #Verifica que alguna fecha del historial de reportes coincida con la fecha ingresada por el usuario
                    dia_reporte.append(historial[ajustes_dia_reporte][1][0]) #Agrega el total a pagar del reporte del día especificado a la lista
                else:
                    ajustes_dia_reporte+=1 #Incrementa el contador para seguir buscando en el historial de reportes
            if len(dia_reporte)==0:
                print("\nEse dia no hubieron ingresos en el parqueadero\n") #Sí no hay reportes del día especificado, se le notificará al usuario
            else:
                print(f"\nEl total de los ingresos del dia: {fecha_ajustes[0]}/{fecha_ajustes[1]} son:\n {sum(dia_reporte)}$") #Imprime el total de los ingresos del día especificado sumando todos los reportes del historial que coincidan con la fecha ingresada por el usuario

        elif ajustes==3:
            continue #Sí el usuario ingresa 3, se vuelve al menú inicial del programa para que pueda realizar otra acción

        elif ajustes==4:
            print("Se cierra el parqueadero".center(50,"="),"\n\n", f"Programa finalizado".center(50," "))
            break #Sí el usuario ingresa 4, se cierra el programa y se imprime un mensaje que indica que el parqueadero se ha cerrado y el programa ha finalizado
        else:
            print("Accion no valida, ingrese otra\n")
            continue #Sí el usuario ingresa una opción que no está en el menú de ajustes, se le notificará y se le pedirá que ingrese una opción válida
    else:
        print("\nAccion no valida, ingrese una valida\n")
        continue
    