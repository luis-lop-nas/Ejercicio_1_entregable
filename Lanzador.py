import math
from Estrella import Estrella
from Galaxia import Galaxia

def distancia(estrella1, estrella2):
    
    x1, y1, z1 = estrella1
    x2, y2, z2 = estrella2
    
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return distancia

def crear_galaxia(estrella):
    
    if Estrella.x > 0 and Estrella.y > 0 and Estrella.z > 0:
        return "Galaxia A"
    elif Estrella.x < 0 and Estrella.y < 0 and Estrella.z < 0:
        return "Galaxia B"
    else:
        return "Galaxia C"
    
def estrella_mas_lejos(estrellas):
    
    origen = (0, 0, 0)
    distancias = {estrella: distancia((estrella.x, estrella.y, estrella.z), origen) for estrella in estrellas}
    estrella_mas_lejos = max(distancias, key=distancias.get)
    return estrella_mas_lejos

def crear_galaxia(estrella):
    
    estrellas = []
    for i in range(10):
        estrella = Estrella()
        estrellas.append(estrella)
    return estrellas

def imprimir_estrellas(estrellas):
    
    for estrella in estrellas:
        print(estrella)
        
def determinar_galaxia(estrellas):
    
    for estrella in estrellas:
        print(f"{estrella} está en la {galaxia(estrella)}")
        
def calcular_distancia(estrellas):
    
    distancias = {}
    for i, estrella1 in enumerate(estrellas):
        for estrella2 in estrellas[i+1:]:
            dist = distancia((estrella1.x, estrella1.y, estrella1.z), (estrella2.x, estrella2.y, estrella2.z))
            distancias [(estrella1, estrella2)] = dist
    return distancias