from tablero import Tablero
import os

class DCCasillas:

    def __init__(self, usuario:str, config:str) -> None:
        self.usuario= usuario
        self.puntaje= 0
        self.tablero_actual= None
        
        ruta=os.path.join("config",config)
        archivo=open(ruta,"r",encoding="utf-8")      
        tableros=[]
        cantidad_lineas = int(archivo.readline())
        for i in range(cantidad_lineas):
            tablero=Tablero()
            linea=archivo.readline()
            linea=linea.strip("\n")
            tablero.cargar_tablero(linea)
            tableros.append(tablero)

        self.tableros = tableros
        
        archivo.close()
        
        #atributo creado que representa la cantidad de tableros resueltos
        self.cantidad_resuelta = 0
        #atributo creado que contiene la clase Tablero()
        self.objeto_tablero_actual=None


    def abrir_tablero(self, num_tablero:int) -> None:
        self.tablero_actual=num_tablero
        nombre_archivo="tablero"+str(num_tablero)+ ".txt"
        nuevo_tablero=Tablero()
        nuevo_tablero.cargar_tablero(nombre_archivo)
        self.tableros.append(nuevo_tablero)
        self.objeto_tablero_actual=nuevo_tablero

    def guardar_estado(self) -> bool: 
        #En caso que no se pueda guardar
        if self.usuario=="":
            return False
        if self.tableros==[]:
            return False
        #En caso que se pueda guardar
        ruta=os.path.join("data",self.usuario + ".txt")
        file=open(ruta,"w",encoding="utf-8")
        #Escribe la cantidad de tableros
        file.write(str(len(self.tableros))+ "\n")
        for i in range(len(self.tableros)): 
            tablero=self.tableros[i]
            #tablero => Tablero()
            file.write(str(tablero.movimientos) + "\n")
            file.write(tablero.cantidad_filas_columnas)
            contador=0
            for j in range(len(tablero.tablero)):
                #tablero.tablero = [[],[],[]]
                lista_fila=tablero.tablero[j]
                #tablero.tablero[j] = [ , , , ]
                filas=" ".join(lista_fila)
                file.write(filas + "\n")
                contador+=1
        file.close()
        return True
        

    def recuperar_estado(self) -> bool:
        ruta=os.path.join("data",self.usuario + ".txt")
        #En caso que exista el archivo
        if os.path.exists(ruta):
            file=open(ruta,"r",encoding="utf-8")
            self.tableros=[]
            linea=file.readline()
            #Comprobar que sea la cantidad de tableros
            if " " in linea:
                return False
            cantidad_tableros=int(linea)
            for i in range(cantidad_tableros):
                tablero_recuperado=Tablero()
                linea=file.readline()
                if "\n" in linea:
                    linea=linea.strip("\n")
                tablero_recuperado.movimientos= int(linea)
                linea=file.readline()
                if "\n" in linea:
                    linea=linea.strip("\n")
                tablero_recuperado.cantidad_filas_columnas=linea
                filas=tablero_recuperado.cantidad_filas_columnas.split(" ")
                for i in range(int(filas[0])+1):
                    linea = file.readline()
                    #Comprobar que no tenga un numero negativo
                    if "-" in linea:
                        return False
                    if "\n" in linea:
                        linea=linea.strip("\n")
                    lista=linea.split(" ")
                    tablero_recuperado.tablero.append(lista)
                tablero_recuperado.validar()
                self.tableros.append(tablero_recuperado)
            file.close()
            return True
        #En caso que no exista
        return False
    
        
