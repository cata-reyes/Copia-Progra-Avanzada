from Jugador import Jugador
from archivos import lista_ias_normal, lista_cartas, lista_ias_dificiles, lista_ias_facil
from archivos import multiplicadores
import parametros
import sys
import random


# Eleccion inicial
args=sys.argv

opciones_a_elegir=["facil","normal","dificil"]
while len(args) != 3 or args[2] == "" or args[1] not in opciones_a_elegir:
    print("\n****      Bienvenido      ****\n")
    print("Para empezar a jugar elige la dificultad (facil, dificil y normal) y tu nombre")
    print("Escribe tu comando de la forma:")
    print("python menu.py [dificultad] [nombre]")
    sys.exit()

jugador=Jugador()
menu_principal=False
menu_tienda=False
menu_taller=False
Combate=False

dificultad=args[1]
jugador.nombre=args[2]
numero_de_ia=0

cartas_inactivas=lista_cartas
opciones_a_elegir=["1","2","3"]
posicion_elegida=[]

for i in range(5): #Puede elegir hasta 5 cartas
    print("Ahora debe elegir una de las siguentes opciones")

    posicion_opciones_cartas=[] #Posición en la lista de las cartas que aparecen en pantalla
    while len(posicion_opciones_cartas) < 3:
        numero=random.randint(0,len(cartas_inactivas)-1)
        if str(numero) not in " ".join(posicion_opciones_cartas):
            print(f"[{len(posicion_opciones_cartas)+1}] {lista_cartas[numero].nombre}")
            posicion_opciones_cartas.append(str(numero))

    if len(cartas_inactivas) < 18: #Si ya se eligió una carta
        print(f"[4] Ir al menú principal")
        opciones_a_elegir.append("4")
    print("Seleccione el número de carta que quiere")
    numero=input()
    while numero not in opciones_a_elegir:
            print("Por favor escribir un número dentro de las opciones")
            numero=input()
    if numero == "4":
        break #No quiere más cartas
    else:
        posicion_elegida = int(posicion_opciones_cartas[int(numero)-1])
        #Se elimina una de las cartas inactivas para agregarla a Jugador
        carta_elegida=cartas_inactivas.pop(posicion_elegida)
        jugador.cartas.append(carta_elegida)
        jugador.coleccion.append(carta_elegida)

menu_principal=True
jugador.oro=parametros.dinero_inicial

if dificultad == "facil":
    lista_ias=lista_ias_facil
elif dificultad == "normal":
    lista_ias=lista_ias_normal
elif dificultad == "dificil":
    lista_ias=lista_ias_dificiles
Ia=lista_ias[0]
print("\nLa Ia enemiga con la que te enfrentarás será:\n")
Ia.presentarse()
print("\n")
while True:
    # Menu principal
    while menu_principal:

        Ia=lista_ias[numero_de_ia]

        print("\n\n----------   MENÚ PRINCIPAL   ----------\n")
        print(f"Dinero disponible: {jugador.oro}G")
        print(f"Ronda actual: {numero_de_ia}/{len(lista_ias)}")
        print(f"Ia enemiga : {Ia.nombre} (Vida {Ia.vida} )\n")
        print("[1] Entrar en combate")
        print("[2] Inventario (gestionar mazo)")
        print("[3] Tienda")
        print("[4] Ver información de mis cartas")
        print("[5] Espiar a la IA")
        print("[0] Salir del juego\n")
        print("Seleccione una opción")
        opcion=input()
        while opcion not in ["1","2","3","4","5","0"]:
            print("Por favor solo introduzca numeros del 0 al 4")
            opcion=input()
        if opcion == "1":
            turno_jugador=False
            if parametros.velocidad_jugador > Ia.velocidad:
                turno_jugador=True
            Combate=True
            menu_principal=False
            #Codigo en la parte inferior de menu
        if opcion == "2":
            #Se reinicia jugador.cartas para elegir cartas de la colección
            jugador.cartas=[]
            numeros_posibles=[]
            print("Elige que cartas de tu colección ocuparas")
            while len(jugador.cartas) < 5:
                for i in range(len(jugador.coleccion)):
                    print(f"[{i+1}]{jugador.coleccion[i].nombre:25s}{jugador.coleccion[i].vida}HP")
                    numeros_posibles.append(str(i+1))
                if len(jugador.cartas) > 2:
                    numeros_posibles.append("0")
                    print("[0] Volver al menú")
                print("Escribe el numero de carta que quieras ocupar en combate")
                numero=input()
                while numero not in numeros_posibles:
                    print("Por favor solo introduzca numeros posibles")
                    print("No puede repetir los numeros escogidos anteriormente")
                    numero=input()
                if numero == "0":
                    break
                else:
                    numeros_posibles.remove(numero)
                    carta_elegida=jugador.coleccion[int(numero)-1]
                    jugador.cartas.append(carta_elegida)
        
        if opcion == "3":
            menu_tienda=True
            menu_principal=False
        
        if opcion == "4":
            for i in jugador.cartas:
                i.presentarse()
        
        if opcion == "5":
            Ia.presentarse()
        
        if opcion == "0":
            print("Saliendo del juego ...")
            sys.exit()

        #menu tienda
    while menu_tienda:
        print("\n----------   TIENDA   ----------\n")
        print(f"Dinero disponible: {jugador.oro}G")
        print("Cartas disponibles")
        
        posicion_opciones_cartas=[]
        contador=0
        while len(posicion_opciones_cartas) < 5:
            numero=random.randint(0,len(cartas_inactivas)-1)
            if str(numero) not in " ".join(posicion_opciones_cartas):
                nombre=cartas_inactivas[numero].nombre
                print(f"[{contador+1}] {nombre:25s}{cartas_inactivas[numero].precio}G")
                posicion_opciones_cartas.append(str(numero))
                contador+=1
        print(f"[6] Curar carta")
        print(f"[7] Revivir carta del cementerio")
        print(f"[8] Reroll del catálogo (Costo 3G)")
        print(f"[9] Ir al Taller")
        print(f"[0] Volver al menú Principal")
        print("Seleccione una opción")
        opcion=input()
        while opcion not in ["1","2","3","4","5","6","7","8","9","0"]:
            print("Por favor solo introduzca numeros del 0 al 9")
            opcion=input()
        if opcion in ["1","2","3","4","5"]:
            posicion_elegida=posicion_opciones_cartas[int(opcion)-1]
            precio_carta=cartas_inactivas[int(posicion_elegida)].precio
            if jugador.oro >= precio_carta:
                jugador.coleccion.append(cartas_inactivas[int(posicion_elegida)])
                jugador.oro-=precio_carta
            else:
                print("No tienen suficiente oro para comprar")

        if opcion == "6":
            contador=0
            numeros_posibles=["0"]
            for i in range(len(jugador.coleccion)):
                carta=jugador.coleccion[i]
                if carta.vida < carta.vida_maxima and carta.vida > 0:
                    print(f"[{contador+1}]{carta.nombre:25s}{carta.vida}/{carta.vida_maxima}HP")
                    numeros_posibles.append(str(contador+1))
                    contador+=1
            if contador > 0:
                print("Escribe el numero de carta que quieras ocupar en combate")
                numero=input()
                while numero not in numeros_posibles:
                    print("Por favor solo introduzca numeros posibles")
                    numero=input()
                if numero == "0":
                    pass
                else:    
                    numeros_posibles.remove(numero)
                    contador=0
                    for i in range(len(jugador.coleccion)):
                        carta=jugador.coleccion[i]
                        if carta.vida < carta.vida_maxima:
                            if contador+1 == int(numero):
                                carta.vida=carta.vida_maxima
                                jugador.oro-=parametros.costo_curar
                                break
                            else:
                                contador+=1
            else:
                print("No hay cartas que puedas curar")
                    
        if opcion == "7":
            contador=0
            numeros_posibles=["0"]
            for i in range(len(jugador.coleccion)):
                carta=jugador.coleccion[i]
                if carta.vida < 1:
                    print(f"[{contador+1}]{carta.nombre:25s}0/{carta.vida_maxima}HP")
                    numeros_posibles.append(str(contador+1))
                    contador+=1
            if contador > 0:
                print("Escribe el numero de carta que quieras revivir")
                numero=input()
                while numero not in numeros_posibles:
                    print("Por favor solo introduzca numeros posibles")
                    numero=input()
                if numero == "0":
                    pass
                else:    
                    numeros_posibles.remove(numero)
                    contador=0
                    for i in range(len(jugador.coleccion)):
                        carta=jugador.coleccion[i]
                        if carta.vida < 1:
                            if contador+1 == int(numero):
                                if jugador.oro > parametros.costo_revivir:
                                    jugador.oro-=parametros.costo_revivir
                                    carta.vida=carta.vida_maxima
                                else:
                                    print("No tienes suficiente oro para revivir tu carta")
                                break
                            else:
                                contador+=1
            else:
                print("No hay cartas que puedas revivir")

        if opcion == "8":
            if jugador.oro >= parametros.costo_reroll:
                jugador.oro-=parametros.costo_reroll
            else:
                print("No tiene suficiente dinero")
                menu_tienda=False
                menu_principal=True
        if opcion == "9":
            menu_taller=True
            menu_tienda=False
            pass
        if opcion == "0":
            menu_principal=True
            menu_tienda=False

    while menu_taller:
        #Mostrar combinaciones
        opciones_a_elegir=["0"]

        print("[0] Volver a tienda")
        print("Seleccione una opcion")
        opcion=input()
        while opcion not in opciones_a_elegir:
            print("Elija entre los numeros mostrados en pantalla")
            opcion=input()
        if opcion == "0":
            menu_taller=False
            menu_tienda=True

    while Combate:
    #Combate 
        tropas=[]
        estructuras= []   
        for i in range(len(jugador.cartas)):
            if jugador.cartas[i].tipo == "tropa":
                tropas.append(jugador.cartas[i])
            else:
                estructuras.append(jugador.cartas[i])

        if turno_jugador == True:
            #Multiplicador
            print(f"\nTurno de {jugador.nombre}")
            dano_total=0
            for j in range(len(multiplicadores)):
                if multiplicadores[j][0] == Ia.nombre and multiplicadores[j][1]=="tropa":
                    Ia.multiplicador_defensa=float(multiplicadores[j][3])
            dano_total=jugador.atacar()
            Ia.recibir_dano(dano_total)
            if Ia.vida <=0:
                print("La Ia murió. Felicitaciones!")
                jugador.oro+=parametros.oro_por_victoria
                Ia.vida=0
                if len(lista_ias) > (numero_de_ia +1):
                    numero_de_ia+=1
                    Combate=False
                    menu_principal=True
                else:
                    print("Derrotaste todas las Ias. Ganaste!!")
                    sys.exit()
            else:
                print(f"{Ia.nombre} queda con {Ia.vida} HP")
            turno_jugador=False

        else:
            print(f"\nTurno de {Ia.nombre}")
            
            if len(estructuras)> 0:
                for j in range(len(multiplicadores)):
                    if multiplicadores[j][0] == Ia.nombre and multiplicadores[j][1]=="estructura":
                        Ia.multiplicador_ataque=float(multiplicadores[j][2])
                dano=Ia.atacar()
                
            elif len(tropas)>0:
                for j in range(len(multiplicadores)):
                    if multiplicadores[j][0] == Ia.nombre and multiplicadores[j][1]=="tropa":
                        Ia.multiplicador_ataque=float(multiplicadores[j][2])
                dano=Ia.atacar()
            jugador.recibir_dano(dano)
            if jugador.cartas == []:
                print("Murieron todas tus cartas. Perdiste")
                jugador.oro+=parametros.oro_por_ronda
                Combate=False
                menu_principal=True

            turno_jugador=True
        
    