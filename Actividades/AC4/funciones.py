from functools import reduce
from itertools import product
from typing import Generator

from utilidades import Pelicula, Genero


# ----------------------------------------------------------------------------
# Parte I: Cargar dataset
# ----------------------------------------------------------------------------

def cargar_peliculas(ruta: str) -> Generator:
    with open(ruta,encoding='utf-8') as archivo:
        for linea in archivo:
            linea.strip("\n")
            linea= linea.split(",")
            if linea[0] != "id":
                pelicula=Pelicula(int(linea[0]),linea[1],linea[2],int(linea[3]),float(linea[4]))
                yield pelicula



# ----------------------------------------------------------------------------
# Parte II: Consultas sobre generadores
# ----------------------------------------------------------------------------


def obtener_directores(generador_peliculas: Generator) -> Generator:
    peliculas=generador_peliculas

    def sacar_director(tupla):
        return tupla[2]
    
    mapeo = map(sacar_director,peliculas) 
    return mapeo


def obtener_str_titulos(generador_peliculas: Generator) -> str:
    peliculas=generador_peliculas

    def sacar_nombre(tupla):
        return tupla[1]
    
    mapeo = map(sacar_nombre,peliculas)
    mapeo=", ".join(mapeo)
    titulos="" if len(mapeo) < 1 else mapeo
    return titulos


def filtrar_peliculas(
    generador_peliculas: Generator,
    director: str | None = None,
    rating_min: float | None = None,
    rating_max: float | None = None,
) -> filter:
    peliculas=generador_peliculas
    
    
    filtrar_si_es_director=filter(lambda x:x[2]==director,peliculas)
    
    """
    Filtra los elementos del generador de Películas según lo indicado en el input.
    """
    return filtrar_si_es_director


def filtrar_titulos(
    generador_peliculas: Generator,
    director: str,
    rating_min: float,
    rating_max: float
) -> Generator:
    """
    Genera un str con todos los títulos de las películas separados
    por ", ". Solo se consideran las películas que tengan el mismo
    director que el indicado, tengan un rating igual o mayor al
    rating_min y un rating igual o menor al rating_max.
    """
    return "COMPLETAR"


def filtrar_peliculas_por_genero(
    generador_peliculas: Generator,
    generador_generos: Generator,
    genero: str | None = None,
) -> Generator:
    """
    Crea un generador con todas las combinaciones posibles entre
    el generador de películas y el generador de géneros.
    Después, filtra las pares obtenidos y mantiene únicamente
    los que presentan el mismo id de película.
    Finalmente, retorna una lista con todos los pares pertenecientes
    a la categoría indicada.
    """
    return "COMPLETAR"
