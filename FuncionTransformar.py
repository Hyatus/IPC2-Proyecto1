
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
            matrizO.insertarCelda(celdaAux,columnas)
            pos += 1     
    #print("MATRIZ ORIGEN")
    #matrizO.recorrerMatriz()

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

def ejecutarAlgoritmoAST(costoVolteo,costoIntercambio):
    costoA = matrizD.algoritmoAST(matrizO,costoVolteo,costoIntercambio)
    matrizO.limpiarMatriz()
    return costoA
    
def ejecutarAlgoritmoBST(costoVolteo,costoIntercambio):
    costoB = matrizD.algoritmoBST(matrizO,costoVolteo,costoIntercambio)
    matrizO.limpiarMatriz()
    return costoB
    
def ejecutarAlgoritmoCST(costoVolteo):
    costoC = matrizD.algoritmoCST(matrizO,costoVolteo)
    matrizO.limpiarMatriz()
    return costoC

def ejecutarAlgoritmoDST(costoVolteo,costoIntercambio):
    costoD = matrizD.algoritmoDST(matrizO,costoVolteo,costoIntercambio)
    matrizO.limpiarMatriz()
    matrizD.limpiarMatriz()
    return costoD



    



    
    
    
    