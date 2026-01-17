# Tarea 1: DCCasillas 4️⃣➕5️⃣🟰9️⃣


## Cosas implementadas y no implementadas :white_check_mark: :x:

### Parte 1 - Automatización tablero.py y ddcasillas.py (41.8%)

#### class Tablero

* ✅ init : Completo
* ✅ cargar_tablero: Completo
* ✅ mostrar_tablero: Completo
* ✅ modificar_casilla: Completo
* ✅ validar: Completo
* 🟠 encontrar_solucion : Unicamente funciona si el tablero inicial es solución

#### class DCCasillas

* ✅ init: Completo
* ✅ abrir_tablero: Completo
* ✅ guardar_estado: Completo
* ✅ recuperar_estado: Completo

### Parte 2 - Menús main.py (45.5%)

#### Menú de Juego

* ✅ Iniciar juego nuevo: Completo
* ✅ Continuar juego: Completo
* ✅ Guardar estado de juego: Completo
* ✅ Recuperar estado de juego: Completo
* ✅ Salir del programa: Completo

#### Menú de acciones

* ✅ Mostrar tablero: Completo
* ✅ Habilitar/deshabilitar casillas: Completo
* 🟠 Encontrar solución: Se realiza una acción únicamente si el tablero esta correcto al momento de realizar la acción
* ✅ Volver al menú de juego: Completo

## Ejecución

El módulo principal de la tarea a ejecutar es main.py.

Igualmente se pueden abrir los siguientes archivos.py:

1. ```tablero.py``` el cual contiene la clase Tablero()
2. ```dccasillas.py``` el cual contiene la clase Dccasillas()

## Librerías

#### Librerías externas utilizadas

1. ```os``` = ```path.join```
2. ```os``` = ```path.exist``` 
3. ```sys``` = ```exit```

#### Librerías propios

1. ```tablero``` -> Contiene la clase Tablero(). Se ejecutará en el archivo DCCasillas.py como un atributo de la clase DCCasillas()
2. ```dccasillas``` -> Contiene la clase Dccasillas(). Se ejecutará en el archivo main.py

## Supuestos y consideraciones adicionales

* Considere que al intentar modificar una casilla que contiene "." en vez de un número el movimiento será clasificado inválido

* Luego de validar el tablero no se permitirá realizar más modificaciones de casillas para no poder obtener más puntos

* Luego de validar el tablero no se permitirá validarlo de nuevo

* No se utilizarán tableros que contengan letras o caracteres especiales (Sin contar ".")

* En los archivos se explican ciertas partes del código mediante #

* Las posiciones del tablero partirán desde el 0

## Referencias a códigos externos

No se utilizaron referencias externas