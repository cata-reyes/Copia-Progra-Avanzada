# Tarea 3: Departamento de las Colecciones del Cosmos :school_satchel:

## Consideraciones generales :octocat:

### Cosas implementadas y no implementadas :white_check_mark: :x:

### Carga de datos: 16pts (16%)
* Cargar_astronautas(): Hecho completo	
* Cargar_naves(): Hecho completo
* Cargar_tripulaciones(): Hecho completo
* Cargar_planetas(): Hecho completo
* Cargar_minerales(): Hecho completo
* Cargar_planeta_minerales(): Hecho completo
* Cargar_mision(): Hecho completo
* Cargar_materiales_mision(): Hecho completo

### Consultas Simples: 15pts (15%)

* Naves_de_material(): Hecho completo
* Misiones_desde_fecha(): Hecho completo. Falla la carga de datos
* Naves_por_intervalo_carga(): Hecho completo
* Planetas_con_cantidad_de_minerales(): Hecho completo
* Naves_astronautas_rango(): No se realizo correctamente
* Cambiar_rango_astronauta(): Hecho completo
* Encontrar_planetas_cercanos(): Hecho completo

### Consultas Complejas: 42pts (43%)

* Disponibilidad_por_planeta(): Hecho completo
* Misiones_por_tipo_planeta(): Hecho pero falla la carga de datos
* Naves_pueden_llevar(): Hecho completo
* Planetas_por_estadisticas(): Realizado pero falla la carga de datos y algunos test de correctitud
* Ganancias_potenciales_por_planeta(): Hecho completo
* Planetas_visitados_por_nave(): Hecho pero falla la carga de datos en archivos más pesados
* Mineral_por_nave(): Funciona pero no se cumple en el tiempo pedido
* Porcentaje_extraccion(): Hecho pero falla la carga de datos
* Resultado_mision(): Funcionan algunos tests (tanto de carga como correctitud). No realize la segunda condicion para retornar.

### Interfaz Gráfica e Interacción: 24pts (25%)

* Main: Abre las ventanas pero no conecta frontend con backend 
* Ventana de Entrada: Hecha completa
* Ventana Principal: Estan los botones pero funciona solo el que conduce a ventana mapa
* Ventana Mapa: Solo está el boton que regresa a ventana principal

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe abrir los siguientes archivos:
1. ```consultas.py``` en ```backend```
2. ```frontend``` en ```frontend```
3. ```parametros``` en T3


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```sys```: ```exit```
2. ```math```: ```pi```
3. ```itertools```: ```tee```
4. ```collections```: ```deque``` y ```defaultdict```
5. ```datetime```: ```date```
6. ```typing```: ```Generator```, ```List```y ```Tuple```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```consultas```: Contiene todas las funciones del backend
2. ```frontend```: Contiene las ventanas relacionadas al frontend
3. ```parámetros```: Contiene los parametros necesarios para el mapa
