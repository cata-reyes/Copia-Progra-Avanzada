from dccasillas import DCCasillas
import os
import sys

menu_de_inicio=True
menu_de_acciones=False
inicio=False

while True:
    
    if menu_de_inicio==True:
        menu_de_acciones=False
        
        #Menu de inicio
        print("¡Bienvenido a DCCasillas!")

        #Si no existe usuario
        if inicio == False:
            print("Usuario: OOO , Puntaje: 000")
            print("Tableros Resueltos: 000 de 000")

        #Si existe usuario
        else:
            print(f"Usuario: {dccasillas.usuario}, Puntaje: {dccasillas.puntaje}")
            cantidad_de_tableros=len(dccasillas.tableros)
            print(f"Tableros Resueltos: {dccasillas.cantidad_resuelta} de {cantidad_de_tableros}")

        print("-----    Menú de Juego   -----\n")

        print("[1]  Iniciar juego nuevo ")
        print("[2]  Continuar juego")
        print("[3]  Guardar estado de juego")
        print("[4]  Recuperar estado de juego")
        print("[5]  Salir del programa \n")
        print("Seleccione una acción: 1, 2, 3, 4, 5")
        
        opcion_inicio =input()

        while opcion_inicio not in " 1 \n 2 \n 3 \n 4 \n 5 ":
            print("Debe indicar una de estos numeros: 1 ,2 ,3 ,4 ,5 ")
            opcion_inicio = input()
        
        if opcion_inicio == "1":
            #Existe usuario
            if inicio == True:
                print("Presione 1 para cambiar el nombre")
                numero=input()
                if numero == "1":
                    usuario=input()
            #No existe usuario
            else:
                print("Indique su nombre de usuario")
                usuario = input()
            #Si el usuario no es valido
            if usuario == "":
                print("Debe haber un nombre de usuario")
                print("Intente nuevamente")
            #Si el usuario es valido
            else:
                #Si se acaba de crear el usuario
                if inicio == False
                    print("Indique una configuración")
                    config=input()
                    ruta_configuracion=os.path.join("config",config)
                #Si existe la configuración
                if os.path.exists(ruta_configuracion) == True and config != "":
                    dccasillas=DCCasillas(usuario,config)
                    dccasillas.puntaje = 0
                    num_tablero=0
                    dccasillas.objeto_tablero_actual=None
                    dccasillas.abrir_tablero(num_tablero)
                    tableros_jugados=1
                    menu_de_acciones=True
                    menu_de_inicio=False
                    inicio=True
                else:
                    print("Ha ocurrido un error intente de nuevo")


        elif opcion_inicio == "2":
            if inicio ==True:
                print("Desea:\n[1] Elegir un nuevo tablero\n[2] Continuar con el tablero ")
                while True: 
                    numero = input()   
                    if numero == "1":                        
                        #Tablero debe ser valido
                        nombre_archivo="tablero"+str(num_tablero)+ ".txt"
                        ruta=os.path.join("config",nombre_archivo)
                        #Si Tablero es valido
                        if os.path.exists(ruta):
                            print("Elija un número de tablero")
                            num_tablero=int(input())
                            dccasillas.abrir_tablero(num_tablero)
                            tableros_jugados+=1
                            menu_de_inicio=False
                            break
                        else:
                            print("Ha ocurrido un error \nDebe elegir un tablero valido")
                    elif numero == "2":
                        menu_de_inicio=False
                        break
                    else:
                        print("Elija 1 o 2")
                menu_de_acciones=True
            else:
                print("Ha ocurrido un error \nInicie un juego nuevo para continuar \n")
                

        elif opcion_inicio == "3":
            if inicio==True:
                if dccasillas.guardar_estado():
                    print("Se guardo el estado")
                else:
                    print("No se pudo guardar estado \nInicie un nuevo juego para continuar")
            else:
                print("Ha ocurrido un error \nInicie un juego nuevo para continuar \n")


        elif opcion_inicio == "4":
            if inicio == True:
                nombre_archivo=dccasillas.usuario + ".txt"
                ruta=os.path.join("data",nombre_archivo)
                if os.path.exists(ruta):
                    if dccasillas.recuperar_estado():
                        print("Se recupero el estado")
                    else:
                        print("Ha ocurrido un error \nInicie un juego nuevo para continuar \n")
                else:
                    print("No hay ningun archivo a recuperar. \nGuarde el juego primero")
            else:
                print("Ha ocurrido un error \nInicie un juego nuevo para continuar \n")


        elif opcion_inicio == "5":
            print("Saliendo ...")
            menu_de_inicio=False
            sys.exit()




    #Menú de acciones

    if menu_de_acciones == True:

        print("DCCasillas")
        print(f"Usuario: {dccasillas.usuario}, Puntaje: {dccasillas.puntaje}")
        print(f"Número de tablero: {tableros_jugados} de {len(dccasillas.tableros)}")
        print(f"Movimientos tablero: {dccasillas.objeto_tablero_actual.movimientos}")

        print("-----    Menú de Acciones    -----\n")

        print("[1]  Mostrar tablero")
        print("[2]  Habilitar/Deshabilitar casillas")
        print("[3]  Verificar solución")
        print("[4]  Encontrar solución")
        print("[5]  Volver al menú de Juego\n")

        print("Seleccione una acción: 1, 2, 3, 4, 5")
    
        opcion_acciones=input()

        while opcion_acciones not in " 1 \n 2 \n 3 \n 4 \n 5 ":
            print("Debe selecionar uno de estos números: 1, 2, 3, 4, 5")
            opcion_acciones=input()   

        if opcion_acciones == "1":
            dccasillas.objeto_tablero_actual.mostrar_tablero()

        elif opcion_acciones == "2":
            print("Elige una fila(Debe ser un número)")
            fila=input()
            print("Elige una columna(Debe ser un número)")
            columna=input()
            modificacion=dccasillas.objeto_tablero_actual.modificar_casilla(int(fila),int(columna))
            if modificacion == False:
                print("Esa casilla es invalida, elije otra \n")
            else:
                dccasillas.objeto_tablero_actual.mostrar_tablero()

        
        elif opcion_acciones == "3":
            if dccasillas.objeto_tablero_actual.estado == False:
                validacion=dccasillas.objeto_tablero_actual.validar()
                if validacion:
                    dccasillas.puntaje+=dccasillas.objeto_tablero_actual.movimientos
                    dccasillas.cantidad_resuelta+=1
                    print("Felicidades! Lo lograste \n")
                else:
                    print("Sigue intentando \n")
            else:
                print("Ya validaste este tablero, por favor inicia otro")

        
        elif opcion_acciones == "4":
            solucion = dccasillas.objeto_tablero_actual.encontrar_solucion()
            if solucion != None:
                print("Esta es tu solucion")
                dccasillas.objeto_tablero_actual.mostrar_tablero()
            else:
                print("No se encontro solución :(")
        
        elif opcion_acciones == "5":
            menu_de_acciones=False
            menu_de_inicio=True
