import os
from tropa import Tropa
from estructura import Estructura
from IA import InteligenciaArtificial

#archivo cartas

ruta=os.path.join("data","cartas.csv")
file=open(ruta,"r", encoding="utf-8")
fila=file.readline()
lista_cartas=[]
descripcion=[]
fila = file.readline()
while fila != "" and fila != "\n":
    if '"' in fila:
        fila=fila.split('"')
        descripcion.append(fila[1])
        fila=fila[0].split(",")
    else:
        fila=fila.split(",")
        descripcion.append(fila[8])
    if fila[1] == "tropa":
        carta=Tropa(fila[0],"tropa",fila[2],fila[3],fila[4],fila[5],fila[6],fila[7])
    else:
        carta=Estructura(fila[0],"estructura",fila[2],fila[3],fila[4],fila[5])
    lista_cartas.append(carta)
    fila=file.readline()
file.close()

#archivos ias_dificil
ruta=os.path.join("data","ias_dificil.csv")
file=open(ruta,"r", encoding="utf-8")
fila=file.readline()
lista_ias_dificiles=[]
fila = file.readline()
while fila != "":
    fila=fila.split('"')
    descripcion=fila.pop(1)
    fila="".join(fila)
    fila=fila.split(",")
    ias_dificil=InteligenciaArtificial(fila[0],fila[1],fila[2],descripcion,fila[4],fila[5])
    lista_ias_dificiles.append(ias_dificil)
    fila=file.readline()
file.close()

#archivos ias_normal
ruta=os.path.join("data","ias_normal.csv")
file=open(ruta,"r", encoding="utf-8")
fila=file.readline()
lista_ias_normal=[]
fila = file.readline()
while fila != "":
    fila=fila.split('"')
    descripcion=fila.pop(1)
    fila="".join(fila)
    fila=fila.split(",")
    ias_normal=InteligenciaArtificial(fila[0],fila[1],fila[2],descripcion,fila[4],fila[5])
    lista_ias_normal.append(ias_normal)
    fila=file.readline()
file.close()

#archivos ias_facil
ruta=os.path.join("data","ias_facil.csv")
file=open(ruta,"r", encoding="utf-8")
fila=file.readline()
lista_ias_facil=[]
fila = file.readline()
while fila != "":
    fila=fila.split('"')
    descripcion=fila.pop(1)
    fila="".join(fila)
    fila=fila.split(",")
    ia_facil=InteligenciaArtificial(fila[0],fila[1],fila[2],descripcion,fila[4],fila[5])
    lista_ias_facil.append(ia_facil)
    fila=file.readline()
file.close()

# multiplicadores
ruta=os.path.join("data","multiplicadores.csv")
file=open(ruta,"r", encoding="utf-8")
fila=file.readline()
multiplicadores=[]
fila = file.readline()
while fila != "":
    fila=fila.strip("\n")
    fila=fila.split(",")
    multiplicadores.append(fila)
    fila=file.readline()
file.close()