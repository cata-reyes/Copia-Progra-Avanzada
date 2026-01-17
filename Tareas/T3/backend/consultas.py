from typing import Generator, List, Tuple
from math import pi
from itertools import tee
from collections import deque, defaultdict
import datetime

from utilidades import ( #type: ignore
    Astronauta,
    Nave,
    Tripulacion,
    Planeta,
    Mineral,
    PlanetaMineral,
    Mision,
    MisionMineral,
    radio_planeta
)

# Cargas 

def cargar_astronautas(path: str) -> Generator[Astronauta, None, None]:
    with open(path, encoding='utf-8') as archivo:
        archivo.readline()
        for linea in archivo:
            linea = linea.strip("\n")
            linea = linea.split(",")
            yield Astronauta(int(linea[0]), linea[1], linea[2])

def cargar_naves(path: str) -> Generator[Nave, None, None]:
    with open(path, encoding='utf-8') as archivo:
        archivo.readline()
        for linea in archivo:
            linea = linea.strip("\n")
            linea = linea.split(",")
            yield Nave(linea[0], linea[1], linea[2], int(linea[3]), float(linea[4]), float(linea[5]))

def cargar_tripulaciones(path: str) -> Generator[Tripulacion, None, None]:
    with open(path,encoding='utf-8') as archivo:
        archivo.readline()
        for linea in archivo:
            linea = linea.strip("\n")
            linea = linea.split(",")
            yield Tripulacion(int(linea[0]),linea[1],int(linea[2]),int(linea[3]))

def cargar_planetas(path: str) -> Generator[Planeta, None, None]:
    with open(path, encoding='utf-8') as archivo:
        archivo.readline()
        for linea in archivo:
            linea = linea.strip("\n")
            linea = linea.split(",")
            yield Planeta(int(linea[0]),linea[1],float(linea[2]),float(linea[3]),linea[4],linea[5])

def cargar_minerales(path: str) -> Generator[Mineral, None, None]:
    with open(path, encoding='utf-8') as archivo:
        archivo.readline()
        for linea in archivo:
            linea = linea.strip("\n")
            linea = linea.split(",")
            yield Mineral(int(linea[0]),linea[1],linea[2],int(linea[3]),float(linea[4]))

def cargar_planeta_minerales(path: str) -> Generator[PlanetaMineral, None, None]:
    with open(path, encoding='utf-8') as archivo:
        archivo.readline()
        for linea in archivo:
            linea = linea.strip("\n")
            linea = linea.split(",")
            yield PlanetaMineral(int(linea[0]), int(linea[1]), float(linea[2]), float(linea[3]))

def cargar_mision(path: str) -> Generator[Mision, None, None]:
    with open(path, encoding='utf-8') as archivo:
        archivo.readline()
        for linea in archivo:
            linea = linea.strip("\n")
            linea = linea.split(",")
            lograda = bool(linea[5]) if linea[5] in "TrueFalse" else None
            yield Mision(int(linea[0]), linea[1], linea[2], int(linea[3]), int(linea[4]), lograda)

def cargar_materiales_mision(path: str) -> Generator[MisionMineral, None, None]:
    with open(path, encoding='utf-8') as archivo:
        archivo.readline()
        for linea in archivo:
            linea = linea.strip("\n")
            linea = linea.split(",")
            yield MisionMineral(int(linea[0]), int(linea[1]), float(linea[2]))

# Consultas 1 generador

def naves_de_material(
        generador_naves: Generator[Nave, None, None], material: str
        ) -> Generator[Nave, None, None]:
    naves_con_el_material=filter(lambda x: x[1] == material, generador_naves)
    return naves_con_el_material

def misiones_desde_fecha(generador_misiones: Generator[Mision, None, None], fecha: str,
                         inverso: bool) -> Generator[Mision, None, None]:
    fecha_generador=generador_misiones[1].split("-")
    fecha_generador=datetime.date(fecha_generador[0],fecha_generador[1],fecha_generador[2])
    fecha= fecha.split("-")
    fecha=datetime.date(fecha[0],fecha[1],fecha[2])
    if inverso:
        if fecha_generador < fecha:
            yield generador_misiones
    else:
        if fecha_generador > fecha:
            yield generador_misiones

def naves_por_intervalo_carga(generador_naves: Generator[Nave, None, None],
                              cargas: tuple[float, float]) -> Generator[Nave, None, None]:
    naves_en_intervalo=filter(lambda x: x[4] >= cargas[0] and x[4] <= cargas[1], generador_naves)
    return naves_en_intervalo
    
def planetas_con_cantidad_de_minerales(
        generador_planeta_mineral: Generator[PlanetaMineral, None, None],
        id_mineral: int, cantidad_minima: int
        ) -> List[int]:
    planetas_con_mineral=[]
    for planeta in generador_planeta_mineral:
        if planeta[1] == id_mineral and (planeta[2]*planeta[3]) >= cantidad_minima:
            planetas_con_mineral.append(planeta[0])
    return planetas_con_mineral

def naves_astronautas_rango(
        generador_tripulacion: Generator[Tripulacion, None, None], 
        rango: int, minimo_astronautas: int
        ) -> Generator[Tuple[str, Generator], None, None]:
    diccionario={}

    for tripulacion in generador_tripulacion:
        patente=tripulacion[1]
        try:
            diccionario[patente].append(tripulacion[2])
        except:
            diccionario[patente]=deque()
            diccionario[patente].append(tripulacion[2])

    def generador_id(key_diccionario):
        for valor in key_diccionario:
            yield valor

    for llave in diccionario:
        mapeo=map(generador_id,llave)
        tupla=tuple([llave,mapeo])
        yield tupla

def cambiar_rango_astronauta(generador_tripulacion: Generator[Tripulacion, None, None],
                             id_astronauta: int, rango_astronauta: int
                             ) -> Generator[Tripulacion, None, None]:
    for tripulacion in generador_tripulacion:
        if tripulacion[2] == id_astronauta:
            tripulacion= tripulacion._replace(rango=rango_astronauta)
        yield tripulacion

def encontrar_planetas_cercanos(generador_planetas: Generator[Planeta, None, None], x1: int, 
                                y1: int, x2: int, y2: int, cantidad: int | None = None
                                ) -> Generator[Planeta, None, None]:
    planetas_en_rango=filter(lambda x: x1 <= x[2] <= x2 and y1 <= x[3] <= y2, generador_planetas)
    for planeta in planetas_en_rango:
        if cantidad != None:
            cantidad-=1
            if cantidad < 0:
                break 
        yield planeta

# Consultas 2 generadores

def disponibilidad_por_planeta(generador_planeta_mineral: Generator[PlanetaMineral, None, None],
                               generador_planetas: Generator[Planeta, None, None], id_mineral: int
                               ) -> Generator[Tuple[str, int, float], None, None]:
    diccionario_mineral={}
    for planeta in generador_planeta_mineral:
        if planeta[1] == id_mineral:
            diccionario_mineral[planeta[0]]=planeta[2]
    for planeta in generador_planetas:
        try:
            yield tuple([planeta[1],planeta[0],diccionario_mineral[planeta[0]]])
        except KeyError:
            yield tuple([planeta[1],planeta[0],0.0])

def misiones_por_tipo_planeta(generador_misiones: Generator[Mision, None, None],
                              generador_planetas: Generator[Planeta, None, None],
                              tipo: str) -> Generator[Mision, None, None]:
    lista_planetas=[]
    for planeta in generador_planetas:
        if planeta[5] == tipo:
            lista_planetas.append(planeta[0])
    for mision in generador_misiones:
        if mision[4] in lista_planetas:
            yield mision

def naves_pueden_llevar(generador_naves: Generator[Nave, None, None],
                        generador_planeta_mineral: Generator[PlanetaMineral, None, None],
                        id_planeta: int) -> Generator[tuple[str, int, float], None, None]:
    diccionario={}
    for planeta in generador_planeta_mineral:
        if planeta[0] == id_planeta:
            diccionario[planeta[1]]=planeta[2]
    for nave in generador_naves:
        for llave in diccionario.keys():
            yield tuple([nave[0],llave,min(nave[4]/diccionario[llave]*100,100)])

# Consultas 3 generadores

def planetas_por_estadisticas(generador_mineral: Generator[Mineral, None, None], 
                              generador_planeta_mineral: Generator[PlanetaMineral, None, None],
                              generador_planeta: Generator[Planeta, None, None], 
                              moles_elemento_min: int, concentracion_molar_min: int,
                              densidad_min: int) -> Generator[Planeta, None, None]:
    
    diccionario_mineral={} #llave es id_mineral, valor es masa_atomica
    for mineral in generador_mineral:
        diccionario_mineral[mineral[0]] = mineral[4]
    
    diccionario_planetas = {} #llave es id_planeta, valor es tamaño_planeta
    planeta1, planeta2 = tee(generador_planeta)
    for planeta in planeta1:
        diccionario_planetas[planeta[0]]= planeta[4]
    
    diccionario_calculos = {} #llaves es id_planeta, valor es tuple[moles, concentracion, densidad]
    for planeta_mineral in generador_planeta_mineral:
        for llave_planeta in diccionario_planetas.keys():
            if planeta_mineral[0] == llave_planeta: # se calcula el radio y el volumen
                radio = radio_planeta(llave_planeta, diccionario_planetas[llave_planeta])
                volumen = 4/3 * pi * radio ** 3 #km^3
                
        for llave_mineral in diccionario_mineral.keys():
            if planeta_mineral[1] == llave_mineral:
                masa_atomica = diccionario_mineral[llave_mineral]
                moles = float(planeta_mineral[2] * 1000000) / float(masa_atomica)
                concentracion = float(planeta_mineral[2] * 1000000) / float(volumen * masa_atomica)
                densidad = (planeta_mineral[2] * 1000000 / volumen)
                diccionario_calculos[planeta_mineral[0]] = tuple([moles, concentracion, densidad])
                
    for planeta in planeta2:
        for llave in diccionario_calculos.keys():
            if planeta[0] == llave:
                cumple_moles = diccionario_calculos[llave][0] >= moles_elemento_min
                cumple_concentracion = diccionario_calculos[llave][1] >= concentracion_molar_min
                cumple_densidad = diccionario_calculos[llave][2] >= densidad_min
                print(cumple_concentracion,cumple_densidad, cumple_moles)
                if cumple_moles and cumple_concentracion and cumple_densidad:
                    yield planeta
                    
def ganancias_potenciales_por_planeta(generador_minerales: Generator[Mineral, None, None],
                                      generador_planeta_mineral: Generator[PlanetaMineral,
                                                                           None, None],
                                      generador_planetas: Generator[Planeta, None, None],
                                      precios: dict) -> dict:
    diccionario_mineral = {} #llave es id_mineral, valor es precio
    for mineral in generador_minerales:
        try:
            diccionario_mineral[str(mineral[0])] = precios[mineral[1]]
        except KeyError:
            pass
    diccionario = defaultdict(float)
    for planeta_mineral in generador_planeta_mineral:
        id_mineral = str(planeta_mineral[1])
        if id_mineral in diccionario_mineral:
            cantidad_pura = planeta_mineral[2] * planeta_mineral[3]
            diccionario[planeta_mineral[0]] += diccionario_mineral[id_mineral] * cantidad_pura
    for planeta in generador_planetas:
        if planeta[0] not in diccionario:
            diccionario[planeta[0]] = 0.0
    return dict(diccionario)
    
def planetas_visitados_por_nave(generador_planetas: Generator[Planeta, None, None],
                                generador_misiones: Generator[Mision, None, None], 
                                generador_tripulaciones: Generator[Tripulacion, None, None]
                                ) -> Generator[Tuple[str, str | None, int | None], None, None]:
    diccionario_planetas = {} #llave es id_planeta, valor es nombre
    for planeta in generador_planetas:
        diccionario_planetas[planeta[0]] = planeta[1]

    diccionario_mision = {} #llave es id_equipo, valor es tuple(patente nave, id_planeta)

    for misiones in generador_misiones:
        if misiones[5] and misiones[4] in diccionario_planetas:
            diccionario_mision[misiones[3]] = tuple([diccionario_planetas[misiones[4]], misiones[4]])
    
    for tripulacion in generador_tripulaciones:
        if tripulacion[0] in diccionario_mision:
            valor_diccionario = diccionario_mision[tripulacion[0]]
            yield tuple([tripulacion[1], valor_diccionario[0], valor_diccionario[1]])
        else:
            yield tuple([tripulacion[1], None, None])
    #tupla = llave

def mineral_por_nave(generador_tripulaciones: Generator[Tripulacion, None, None],
                     generador_misiones: Generator[Mision, None, None],
                     generador_misiones_mineral: Generator[MisionMineral, None, None]
                     ) -> Generator[Tuple[str, float], None, None]:
    diccionario_mineral = defaultdict(int)
    
    misiones1, misiones2 = tee(generador_misiones)
    diccionario_misiones = {}
    for misiones in misiones1:
        diccionario_misiones[misiones[0]] = misiones[5]
    
    for mineral in generador_misiones_mineral:
        if mineral[0] in diccionario_misiones:
            if diccionario_misiones[misiones[0]]:
                diccionario_mineral[mineral[0]] += mineral[2]
            else:
                diccionario_mineral[mineral[0]] += 0.0
    
    diccionario_misiones_2 = {}
    for misiones in misiones2:
        if misiones[0] in diccionario_mineral:
            diccionario_misiones_2[misiones[3]] = diccionario_mineral[misiones[0]]
    
    set_tripulacion = set()
    for tripulacion in generador_tripulaciones:
        if tripulacion[0] not in set_tripulacion:
            set_tripulacion.add(tripulacion[0])
            if tripulacion[0] in diccionario_misiones_2:
                yield tuple([tripulacion[1], diccionario_misiones_2[tripulacion[0]]])
            else:
                yield tuple([tripulacion[1], 0.0])
        
def porcentaje_extraccion(generador_tripulacion: Generator[Tripulacion, None, None],
                          generador_mision_mineral: Generator[MisionMineral, None, None],
                          generador_planeta_mineral: Generator[PlanetaMineral, None, None],
                          mision: Mision) -> Tuple[float, float]:
    tripulantes = 0
    for tripulacion in generador_tripulacion:
        if tripulacion[0] == mision.id_equipo:
            tripulantes += 1
    
    diccionario_misiones = {}
    mineral_extraido = 0
    for misiones in generador_mision_mineral:
        if mision.lograda:
            if mision.id_mision == misiones[0]:
                mineral_extraido += misiones[2]
                id_mineral = misiones[1]
                diccionario_misiones[id_mineral] = misiones[2]

    total_planeta = 0
    
    for planeta in generador_planeta_mineral:
        if planeta[1] in diccionario_misiones:
            total_planeta += planeta[2] * planeta[3]
    
    try:
        porcentaje_extraido = mineral_extraido * 100 / total_planeta
        porcentaje_por_tripulante = porcentaje_extraido / tripulantes
    except ZeroDivisionError:
        return tuple([0.0, 0.0])
    
    return tuple([porcentaje_extraido, porcentaje_por_tripulante])
     
# Consultas 4 generadores

def resultado_mision(mision: Mision, generador_naves: Generator[Nave, None, None],
                     generador_planeta_mineral: Generator[PlanetaMineral, None, None],
                     generador_tripulaciones: Generator[Tripulacion, None, None],
                     generador_mision_mineral: Generator[MisionMineral, None, None]) -> Mision:
    diccionario_planeta = {} # llave es id_mineral, valor es capacidad
    logrado = True

    for planeta in generador_planeta_mineral:
        diccionario_planeta[planeta[1]] = planeta[2]
    
    total = 0
    for misiones in generador_mision_mineral:
        if mision.id_mision == misiones[0]:
            if misiones[1] in diccionario_planeta:
                diccionario_planeta[misiones[1]] -= misiones[2]
                total += misiones[2]
                if diccionario_planeta[misiones[1]] <= 0:
                    logrado = False
    
    if total == 0:
        logrado = False

    for tripulacion in generador_tripulaciones:
        if mision.id_equipo == tripulacion[0]:
            patente_nave = tripulacion[1]
    
    for naves in generador_naves:
        if naves[0] == patente_nave:
            if total > naves[4]:
                logrado = False

    tupla = Mision(mision.id_mision, mision.fecha, mision.hora, mision.id_equipo, 
                  mision.id_planeta, logrado)
    return tupla