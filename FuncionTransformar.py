
from ListaMatrizO import *
from ListaMatrizD import *
from claseCelda import *
from NodoMatriz import *

matrizO = ListaMatrizO()
matrizD = ListaMatrizD()

def crearMatrizOrigen(columnas,filas,patron):
    pos = 0
    for i in range(filas):
        for j in range(columnas):
            celdaAux = Celda(int(i),int(j),patron[pos])
            matrizO.insertarCelda(celdaAux)
            pos += 1     
    print("MATRIZ ORIGEN")
    matrizO.recorrerMatriz()

def crearMatrizDestino(columnas,filas,patron):
    pos = 0
    for i in range(filas):
        for j in range(columnas):
            celdaAux = Celda(int(i),int(j),patron[pos])
            matrizD.insertarCelda(celdaAux)
            pos += 1
    #print("MATRIZ DESTINO")
    #matrizD.recorrerMatriz()
    #print("MATRIZ INVERSA")
    #matrizD.recorrerInverso()
    
    
def ejecutarAlgoritmoA(costoVolteo,costoIntercambio):
    matrizD.algoritmoA(matrizO,costoVolteo,costoIntercambio)
    matrizO.limpiarMatriz()
    
def ejecutarAlgoritmoB(costoVolteo,costoIntercambio):
    matrizD.algoritmoB(matrizO,costoVolteo,costoIntercambio)
    matrizO.limpiarMatriz()


def ejecutarAlgoritmoD(costoVolteo,costoIntercambio):
    matrizD.algoritmoD(matrizO,costoVolteo,costoIntercambio)
    matrizO.limpiarMatriz()
    
    



    
    
    
    