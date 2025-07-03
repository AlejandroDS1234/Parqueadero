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
        while True:
            placa=input("\nIngrese la placa del vehiculo (AAA000): ").upper()
            #detectar errores en la placa
            if len(placa)!=6:#longitud de la placa
                print("Placa no valida vuelva a intentarlo\n") 
                continue #si detecta un error vuelve al inicio del bucle a predir el codigo
            elif placa[0:3].isalpha()==False or placa[3:5].isdigit()==False: #ver los caracteres de la placa
                print("Placa no valida vuelva a intentarlo\n")
                continue #si detecta un error vuelve al inicio del bucle a predir el codigo
            else:
                #if
                break #si no hay errores con la placa sale del bucle de pedir la placa y continua con el siguiente

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
            fecha_entrada_dia,fecha_entrada_mes=input("\nIngrese la fecha de entrada (DD/MM): ").split("/") #Las dos variables que forman un elemento, se dividen y se asigna la variable 1 al elemento 1 y la variable 2 al elemento 2
            if len(fecha_entrada_dia)>2 or len(fecha_entrada_dia)<1 or len(fecha_entrada_mes)>2 or len(fecha_entrada_mes)<1:
                print("Fecha mal ingresada, tiene que ser en formato DD/MM, vuelva a intentarlo\n")
                continue
            if len(fecha_entrada_dia)==1:
                fecha_entrada_dia=f"{0}{fecha_entrada_dia}"
            if len(fecha_entrada_mes)==1:
                fecha_entrada_mes=f"{0}{fecha_entrada_mes}"
            
            #meses
            if int(fecha_entrada_mes)<=12 and int(fecha_entrada_mes)>=1:
                if fecha_entrada_mes=="01" or fecha_entrada_mes=="03" or fecha_entrada_mes=="05" or fecha_entrada_mes=="07" or fecha_entrada_mes=="08" or fecha_entrada_mes=="10" or fecha_entrada_mes=="12":
                    if int(fecha_entrada_dia)>31 or int(fecha_entrada_dia)<1:
                        print("Fecha incorrecta, el mes tiene 31 dias, vuelva a intentarlo\n")
                        continue
                    else:
                        break
                elif fecha_entrada_mes=="04" or fecha_entrada_mes=="06" or fecha_entrada_mes=="09" or fecha_entrada_mes=="11":
                    if int(fecha_entrada_dia)>30 or int(fecha_entrada_dia)<1:
                        print("Fecha incorrecta, el mes tiene 30 dias, vuelva a intentar\n")
                        continue
                    else:
                        break
                elif fecha_entrada_mes=="02":
                    if int(fecha_entrada_dia)>29 or int(fecha_entrada_dia)<1:
                        print("Fecha incorrecta, el mes tiene maximo 29 dias, vuelva a intentar\n")
                        continue
                    else:
                        break
            else:
                print("fecha incorrecta, el mes no existe, vuelva a intentar\n")
                continue
        fecha_entrada=(fecha_entrada_dia,fecha_entrada_mes)
        
        
        vehiculos.append((placa,tipo,hora_entrada_,fecha_entrada))
        print(f"\nLos datos ingresados son:\nPlaca: {placa}\nTipo: {tipo}\nHora de entrada: {hora_entrada_[0]}:{hora_entrada_[1]}\nFecha de entrada: {fecha_entrada[0]}/{fecha_entrada[1]}")
            
    #salida
    elif entrada=="S":
        if len(vehiculos)!=0:
            while True:    
                placa_salida=input("\nIngrese la placa de su vehiculo para salir: ").upper()
                if len(placa_salida)!=6:#longitud de la placa
                    print("Placa no valida vuelva a intentarlo\n") 
                    continue #si detecta un error vuelve al inicio del bucle a predir el codigo
                elif placa_salida[0:3].isalpha()==False or placa_salida[3:5].isdigit()==False: #ver los caracteres de la placa
                    print("Placa no valida vuelva a intentarlo\n")
                    continue #si detecta un error vuelve al inicio del bucle a predir el codigo
                else:
                    break #si no hay errores con la placa sale del bucle de pedir la placa y continua con el siguiente
            contador=0
            while True:
                if vehiculos[contador][0]==placa_salida:
                    while True:
                        hora_salida,minutos_salida=input("\nIngrese la hora de salida (HH:MM): ").split(":")
                        if int(hora_salida)>24 or int(hora_salida)<0 or int(minutos_salida)>59 or int(minutos_salida)<0:
                            print("Hora no valida, vuelva a intentarlo\n")
                            continue
                        elif len(hora_salida)>2 or len(hora_salida)<1:
                            print("Hora mal ingresada, tiene que ser en formato 24h, vuelva a intentarlo\n")
                            continue
                        else:
                            if len(hora_salida)==1:
                                hora_salida=f"{0}{hora_salida}"
                            if len(minutos_salida)==1:
                                minutos_salida=f"{0}{minutos_salida}"
                            hora_salida_=(hora_salida,minutos_salida)
                            break
                    while True:
                        fecha_salida_dia,fecha_salida_mes=input("\nIngrese la fecha de salida (DD/MM): ").split("/")
                        if len(fecha_salida_dia)>2 or len(fecha_salida_dia)<1 or len(fecha_salida_mes)>2 or len(fecha_salida_mes)<1:
                            print("Fecha mal ingresada, tiene que ser en formato DD/MM, vuelva a intentarlo\n")
                            continue
                        if len(fecha_salida_dia)==1:
                            fecha_salida_dia=f"{0}{fecha_salida_dia}"
                        if len(fecha_salida_mes)==1:
                            fecha_salida_mes=f"{0}{fecha_salida_mes}"
            
                        #meses
                        if int(fecha_salida_mes)<=12 and int(fecha_salida_mes)>=1:
                            if fecha_salida_mes=="01" or fecha_salida_mes=="03" or fecha_salida_mes=="05" or fecha_salida_mes=="07" or fecha_salida_mes=="08" or fecha_salida_mes=="10" or fecha_salida_mes=="12":
                                if int(fecha_salida_dia)>31 or int(fecha_salida_dia)<1:
                                    print("Fecha incorrecta, el mes tiene 31 dias, vuelva a intentarlo\n")
                                    continue
                                else:
                                    break
                            elif fecha_salida_mes=="04" or fecha_salida_mes=="06" or fecha_salida_mes=="09" or fecha_salida_mes=="11":
                                if int(fecha_salida_dia)>30 or int(fecha_salida_dia)<1:
                                    print("Fecha incorrecta, el mes tiene 30 dias, vuelva a intentar\n")
                                    continue
                                else:
                                    break
                            elif fecha_salida_mes=="02":
                                if int(fecha_salida_dia)>29 or int(fecha_salida_dia)<1:
                                    print("Fecha incorrecta, el mes tiene maximo 29 dias, vuelva a intentar\n")
                                    continue
                                else:
                                    break
                        else:
                            print("fecha incorrecta, el mes no existe, vuelva a intentar\n")
                            continue
                    fecha_salida=(fecha_salida_dia,fecha_salida_mes)


                    hora_minutos_entrada=(int(vehiculos[contador][2][0])*60)+int(vehiculos[contador][2][1])
                    hora_minutos_salida=(int(hora_salida)*60)+int(minutos_salida)
                    #mismo mes
                    if fecha_salida[1]==vehiculos[contador][3][1]:
                        dias_parqueo=int(fecha_salida[0])-int(vehiculos[contador][3][0])
                        if dias_parqueo<0:
                            print("Datos de salida incorrectos, ingrese los datos nuevamente\n")
                            continue
                        else:
                            horas_parqueo=hora_minutos_salida-hora_minutos_entrada
                            if horas_parqueo<0:
                                print("Datos de salida incorrectos, ingrese los datos nuevamente\n")
                                continue
                            else:
                                horas_parqueo=round(horas_parqueo/60,2)
                                dias_parqueo*=24
                                horas_parqueo+=dias_parqueo
                                total_pagar=horas_parqueo*precios[vehiculos[contador][1]]
                                print(f" Su vehiculo estubo {horas_parqueo} horas en el parqueadero ".center(20,"-"),"\n",f" Debe pagar: {total_pagar}$ ".center(20,"-"))
                                historial.append((vehiculos[contador],(total_pagar,hora_salida,fecha_salida)))
                                vehiculos.remove(vehiculos[contador])
                                break

                    elif int(fecha_salida[1])>int(vehiculos[contador][3][1]):
                        contador_dias=vehiculos[contador][3][1]
                        dias_parqueo=0
                        while int(contador_dias)<=int(fecha_salida[1]):
                            dias_parqueo+=meses[contador_dias]
                            if int(contador_dias)<10:
                                contador_dias=f"{0}{int(contador_dias)+1}"
                            else:
                                contador_dias=int(contador_dias)+1
                        dias_parqueo-=meses[fecha_salida[1]]-int(fecha_salida[0])
                        dias_parqueo-=int(vehiculos[contador][3][0])
                        dias_parqueo*=24
                        if dias_parqueo<0:
                            print("Datos de salida incorrectos, ingrese los datos nuevamente\n")
                            continue
                        else:
                            hora_minutos_entrada=(int(vehiculos[contador][2][0])*60)+int(vehiculos[contador][2][1])
                            hora_minutos_salida=(int(hora_salida)*60)+int(minutos_salida)
                            horas_parqueo=hora_minutos_salida-hora_minutos_entrada
                            if horas_parqueo<0:
                                print("Datos de salida incorrectos, ingrese los datos nuevamente\n")
                                continue
                            else:
                                horas_parqueo=round(horas_parqueo/60,2)
                                horas_parqueo+=dias_parqueo
                                total_pagar=horas_parqueo*precios[vehiculos[contador][1]]
                                print(f" Su vehiculo estubo {horas_parqueo} horas en el parqueadero ".center(20,"-"),"\n",f" Debe pagar: {total_pagar}$ ".center(20,"-"))
                                historial.append((vehiculos[contador],(total_pagar,hora_salida,fecha_salida)))
                                vehiculos.remove(vehiculos[contador])
                                break
                                
                    elif int(fecha_salida[1])<int(vehiculos[contador][3][1]):
                        print("Datos de salida incorrectos, ingrese los datos nuevamente\n")
                        continue
                else:
                    contador+=1
                    if contador>len(vehiculos):
                        print("El vehiculo no esta registrado en el parqueadero\n")
                        break
        else:
            print("No hay vehiculos en el parqueadero\n") 

    elif entrada=="X":
        print("\n\n")
        print("Opciones del programa".center(20,"-"))    
        print("\ningrese 1 para ver las vehiculos adentro del parqueadero\nIngrese 2 para ver el reporte de ingresos por un dia\nIngrese 3 para volver al menu inicial\nIngrese 4 para salir del programa")
        ajustes=int(input("Ingrese la accion que desee realizar: "))
        if ajustes==1:
            if len(vehiculos)!=0:
                print(f"\nLos vehiculos en el parqueadero por el momento son:\n{vehiculos}")
            else:
                print("\nNo hay ningun vehiculo en el parqueadero")
        elif ajustes==2:
            while True:
                fecha_ajustes_dia,fecha_ajustes_mes=input("\nIngrese la fecha para el reporte de ingresos diario (DD/MM): ").split("/")
                if len(fecha_ajustes_dia)>2 or len(fecha_ajustes_dia)<1 or len(fecha_ajustes_mes)>2 or len(fecha_ajustes_mes)<1:
                    print("Fecha mal ingresada, tiene que ser en formato DD/MM, vuelva a intentarlo\n")
                    continue
                if len(fecha_ajustes_dia)==1:
                    fecha_ajustes_dia=f"{0}{fecha_ajustes_dia}"
                if len(fecha_ajustes_mes)==1:
                    fecha_ajustes_mes=f"{0}{fecha_ajustes_mes}"
            
                #meses
                if int(fecha_ajustes_mes)<=12 and int(fecha_ajustes_mes)>=1:
                    if fecha_ajustes_mes=="01" or fecha_ajustes_mes=="03" or fecha_ajustes_mes=="05" or fecha_ajustes_mes=="07" or fecha_ajustes_mes=="08" or fecha_ajustes_mes=="10" or fecha_ajustes_mes=="12":
                        if int(fecha_ajustes_dia)>31 or int(fecha_ajustes_dia)<1:
                            print("Fecha incorrecta, el mes tiene 31 dias, vuelva a intentarlo\n")
                            continue
                        else:
                            break
                    elif fecha_ajustes_mes=="04" or fecha_ajustes_mes=="06" or fecha_ajustes_mes=="09" or fecha_ajustes_mes=="11":
                        if int(fecha_ajustes_dia)>30 or int(fecha_ajustes_dia)<1:
                            print("Fecha incorrecta, el mes tiene 30 dias, vuelva a intentar\n")
                            continue
                        else:
                            break
                    elif fecha_ajustes_mes=="02":
                        if int(fecha_ajustes_dia)>29 or int(fecha_ajustes_dia)<1:
                            print("Fecha incorrecta, el mes tiene maximo 29 dias, vuelva a intentar\n")
                            continue
                        else:
                            break
                else:
                    print("fecha incorrecta, el mes no existe, vuelva a intentar\n")
                    continue
            fecha_ajustes=(fecha_ajustes_dia,fecha_ajustes_mes)
            dia_reporte=[]
            ajustes_dia_reporte=0
            while ajustes_dia_reporte<len(historial):
                if historial[ajustes_dia_reporte][1][2]==fecha_ajustes:
                    dia_reporte.append(historial[ajustes_dia_reporte][1][0])
                else:
                    ajustes_dia_reporte+=1
            if len(dia_reporte)==0:
                print("\nEse dia no hubieron ingresos en el parqueadero\n")
            else:
                print(f"\nEl total de los ingresos del dia: {fecha_ajustes[0]}/{fecha_ajustes[1]} son:\n {sum(dia_reporte)}$")

        elif ajustes==3:
            continue

        elif ajustes==4:
            print("Se cierra el parqueadero".center(50,"="),"\n\n", f"Programa finalizado".center(50," "))
            break
        else:
            print("Accion no valida, ingrese otra\n")
            continue
