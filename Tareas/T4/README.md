# Tarea 4: DCCasino :school_satchel:


## Consideraciones generales :octocat:

### Cosas implementadas y no implementadas :white_check_mark: :x:

#### Interfaces gráficas (47%)
* Ventana de inicio: Implementada completamente
* Ventana principal: Creada pero no contiene todos los elementos mínimos
* Ventana de recarga: Implementada completamente
* Ventana Aviator: Creada pero no contiene los elementos mínimos
* Ventana Blackjack: Creada pero no contiene los elementos mínimos

#### Networking (15%)
* Networking general: Funciona correctamente
* Codificación y decodificación: Implementada correctamente

#### Funcionalidades servidor (20%)
* Inicio sesión:  Funciona correctamente
* Administracion de partidas: No implementado
* Durante la partida: No implementado
* WebServices: No implementado

#### Webservices (12%)
* Get users: No implementada
* Post users: No implementada
* Patch users: No implementada
* Post games: No implementada
* Concurrencia: No implementada

#### Archivos (7%)
* Estructura: Implementada correctamente
* Conexion.json: Implementada correctamente
* Parámetros: Implementada pero no se utilizan todos los parámetros


#### Bonus
* Ruleta: No implementado


## Ejecución :computer:
La tarea se ejecutará en dos módulos principales. El primero a ejecutar es ```main.py``` del directorio servidor para poder iniciar el servidor. Luego para iniciar los clientes se debe ejecutar ```main.py``` del directorio cliente. Tambien se encuentran otros. Además se deben abrir los siguientes archivos

1. ```backend.py``` en ```cliente/backend```
2. ```frontend.py``` en ```cliente/frontend```
3. ```conexion.json``` en ```cliente/backend```
4. ```parametros.py``` en ```cliente/database```
5. ```server.py``` en ```servidor```
6. ```conexion.json``` en ```servidor/database```
7. ```parametros.py``` en ```servidor/database```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```os```: ```path()``` 
2. ```json```: ```load()```, ```dumps()``` (debe instalarse)
3. ```socket```: ```socket()```, ```AF_INET```, ```Sock_STREAM```, ```bind()```, ```listen()```, ```settimeout()```, ```accept()```, ```recv()```y ```sendall```
4. ```math```: ```pi```
5. ```PyQt5.QtCore```: ```pyqtSignal```, ```QObject```
6. ```PyQt5.Widgets```: ```QApplication```, ```QWidget```, ```QLabel```, ```QPushButton``` y ```QLineEdit```
7. ```threading```: ```Lock()```, ```Thread()```
8. ```sys```: ```exit()```
9. ```random```: ```shuffle()```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```backend```: Contiene la clase cliente ```Cliente``` que maneja todo el backend del cliente
2. ```frontend```: Contiene todo el frontend del cliente
3. ```conexion.json``` (cliente): Archivo en cliente que le permiten al cliente iniciar conexion con el servidor
4. ```parametros_cliente``` (cliente): Contiene todos los parámetros del cliente
5. ```server```: Contiene la clase cliente ```Server``` que maneja toda las acciones del servidor
6. ```conexion.json``` (servidor): Archivo en servidor que le permiten al servidor iniciar conexion con el cliente
7. ```parametros_servidor``` (servidor): Contiene todos los parámetros del servidor

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Como no se implementaron los juegos se puede probar el networking mandando mensajes entre las terminales. El código para probarlo se encuentra comentado(#) en las funcion manejar_cliente() en servidor/server.py y en listen_thread() en cliente/cliente.py.

## Referencias de código externo :book:

No se utilizaron referencias
