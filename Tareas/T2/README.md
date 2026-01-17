# Tarea 2: DCCartas contra la DCCatástrofe :school_satchel:
 

## Consideraciones generales :octocat:

### Cosas implementadas y no implementadas :white_check_mark: :x:

### Programación Orientada a Objetos 8%
* Aplicar Herencia : Hecha completa (Carta -> Tropa, Carta -> Estructura)
* Aplicar Clase abstracta: Hecha completa (Carta)
* Aplicar polimorfismo: Hecha Completa (Tropa y Estructura)
* Aplicar decoradores: Hecha pero a veces falla (Carta, Tropa y Estructura)

### Entidades 39%
* Carta: Hecha Completa
* Carta Tropa: Falta usar_habilidad_especial
* Carta Estructura: Falta usar_habilidad_especial
* Carta Mixta: Falta usar_habilidad_especial
* Jugador: Falta usar_habilidad_especial
* IA: Falta usar_habilidad_especial

### Flujo del programa 22%
* Menú principal: Hecho completo
* Menú Tienda: Hecho completo
* Menú Taller: Solo funciona volver a Menu Tienda. No estan implementadas las cartas Mixtas en el flujo del programa

### Combate 16%
* Turnos: Implementado completamente
* Ataque Jugador: Implementado completamente en Tropa y Estructura, Mixta no esta implementada en el flujo del programa
* Ataque Ia: Implementado completamente
* Calculo de daño: Implementado completamente

### Bonus
* Guardar partida: No realizado

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```menu.py```. Además se deben abrir los siguientes archivos
1. ```archivos.py``` en ```T2``` Contiene la lectura de los archivos csv
2. ```carta.py``` en ```T2``` Contiene a  la clase abstracta ```Carta()```
3. ```estructura.py``` en ```T2``` Contiene a  la clase ```Estructura()``` que hereda de ```Carta()```
4. ```tropa.py``` en ```T2``` Contiene a  la clase ```Tropa()``` que hereda de ```Carta()```
5. ```IA.py``` en ```T2``` Contiene a  la clase ```InteligenciaArtificial()```
6. ```Jugador.py``` en ```T2``` Contiene a  la clase ```Jugador()```
7. ```parametros.py``` en ```T2``` Contiene a las constantes asociadas al juego
8. ```mixta.py``` en ```T2``` Contiene a la clase ```TropaEstructura()``` que hereda de ```Tropa()``` y ```Estructura()```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```randint()``` y ```uniform()```
2. ```abc```: ```ABC``` y ```abstractmethod```
3. ```sys```: ```exit```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```Jugador```: Contiene ```Jugador()```
2. ```archivos```: Contiene la lectura de archivos csv
3. ```carta```: Contiene ```Carta()```
4. ```tropa```: Contiene ```Tropa()```
5. ```estructura```: Contiene ```Estructura()```
6. ```Ia```: Contiene ```InteligenciaArtificial()```
7. ```parametros```: Contiene a las constantes asociadas al juego
8. ```mixta.py``` en ```T2``` Contiene ```TropaEstructura```

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Se asume que en los archivos de ias.csv la descripción se encontrará siempre entre "" 
2. Se asume que al derrotar a todas las Ia el juego se terminará
3. 


## Referencias de código externo :book:

No se utilizaron referencias externas
