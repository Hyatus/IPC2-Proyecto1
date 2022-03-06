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

def crearMatrizDestino(columnas,filas,patron):
    pos = 0
    for i in range(filas):
        for j in range(columnas):
            celdaAux = Celda(int(i),int(j),patron[pos])
            matrizD.insertarCelda(celdaAux)
            pos += 1

def ejecutarAlgoritmoA(texto,columnasPiso,filasPiso):
    matrizD.algoritmoA(matrizO,texto,columnasPiso,filasPiso)
    matrizO.limpiarMatriz()
    matrizD.limpiarMatriz()

def ejecutarAlgoritmoB(texto,columnasPiso,filasPiso):
    matrizD.algoritmoB(matrizO,texto,columnasPiso,filasPiso)
    matrizO.limpiarMatriz()
    matrizD.limpiarMatriz()

def ejecutarAlgoritmoD(texto,columnasPiso,filasPiso):
    matrizD.algoritmoD(matrizO,texto,columnasPiso,filasPiso)
    matrizO.limpiarMatriz()
    matrizD.limpiarMatriz()

def ejecutarAlgoritmoAST(costoVolteo,costoIntercambio):
    costoA = matrizD.algoritmoAST(matrizO,costoVolteo,costoIntercambio)
    matrizO.limpiarMatriz()
    #matrizD.limpiarMatriz()
    return costoA
    
def ejecutarAlgoritmoBST(costoVolteo,costoIntercambio):
    costoB = matrizD.algoritmoBST(matrizO,costoVolteo,costoIntercambio)
    matrizO.limpiarMatriz()
    #matrizD.limpiarMatriz()
    return costoB
    
def ejecutarAlgoritmoCST(costoVolteo):
    costoC = matrizD.algoritmoCST(matrizO,costoVolteo)
    matrizO.limpiarMatriz()
    #matrizD.limpiarMatriz()
    return costoC

def ejecutarAlgoritmoDST(costoVolteo,costoIntercambio):
    costoD = matrizD.algoritmoDST(matrizO,costoVolteo,costoIntercambio)
    matrizO.limpiarMatriz()
    matrizD.limpiarMatriz()
    return costoD



    



    
    
    
    