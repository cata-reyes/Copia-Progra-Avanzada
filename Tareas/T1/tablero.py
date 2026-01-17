from visualizador import imprimir_tablero
import os

class Tablero:

    def __init__(self) -> None:
        self.tablero = []
        self.movimientos = 0
        self.estado = False

        #Atributo creado que contiene un string "[numero filas] [numero columnas]"
        self.cantidad_filas_columnas = ""

    def cargar_tablero(self, archivo:str) -> None:
        ruta=os.path.join("config",archivo)
        file=open(ruta, "r", encoding= "utf-8")
        self.cantidad_filas_columnas=file.readline()
        filas=self.cantidad_filas_columnas.split(" ")
        for i in range(int(filas[0])+1):
            linea=file.readline()
            if "\n" in linea:
                linea=linea.strip("\n")
            lista=linea.split(" ")
            self.tablero.append(lista)
        file.close()

    def mostrar_tablero(self) -> None:
        imprimir_tablero(self.tablero)

    def modificar_casilla(self, fila:int, columna:int) -> bool:
        if type(fila) != int or type(columna) != int:
            return False
        filas= len(self.tablero)
        columnas= len(self.tablero[0])
        if fila > (filas - 1) or columna > (columnas - 1):
            return False
        casilla = self.tablero[fila][columna]
        if "." in casilla:
            return False
        elif fila == filas  or columna == columnas:
            return False
        elif "X" in casilla:
            casilla = casilla[1:]
            self.movimientos+=1
            self.tablero[fila][columna]=casilla
            return True
        elif "X" not in casilla:
            casilla= "X" + casilla
            self.movimientos+=1
            self.tablero[fila][columna]=casilla    
            return True
        
    def validar(self) -> bool:
        filas= len(self.tablero)
        columnas= len(self.tablero[0])
        #Comprobar columna
        for i in range(columnas):
            contador = 0
            if "." not in self.tablero[filas-1][i]:
                for j in range(filas-1):
                    #Si solo hay numeros
                    if "." not in self.tablero[j][i] and "X" not in self.tablero[j][i]:
                        #numeros se suman al contador
                        contador+=int(self.tablero[j][i])
                #se comparan las cantidades
                if str(contador) != self.tablero[filas-1][i]:
                    return False
        #Comprobar filas
        for k in range(filas):
            contador=0
            if "." not in self.tablero[k][columnas-1]:
                for l in range(columnas-1):
                    #Solo si hay numeros
                    if "." not in self.tablero[k][l] and "X" not in self.tablero[k][l]:
                        contador+=int(self.tablero[k][l])
                #Se comparan las cantidades
                if str(contador) != self.tablero[k][columnas-1]:
                    return False
        self.estado=True
        return True
    
    def encontrar_solucion(self):
        tablero_1=Tablero()
        tablero_1.tablero=self.tablero.copy()
        if tablero_1.validar():
            return tablero_1
        else:
            return None

