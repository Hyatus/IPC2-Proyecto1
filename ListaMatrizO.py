from NodoMatriz import *
from claseCelda import *

class ListaMatrizO():
    
    def __init__(self) -> None:
        self.primero = None
        self.columnas = None

    
    def insertarCelda(self,Celda,columnas):
        self.columnas = columnas
        if self.primero == None:
            self.primero = NodoMatriz(Celda=Celda)
            return
        
        actual = self.primero 
        while actual.siguiente:
            actual = actual.siguiente
        
        actual.siguiente = NodoMatriz(Celda=Celda)
        
    def buscarCelda(self,fila,columna):
        actual = self.primero 
        
        while actual != None:
            if actual.Celda.fila == fila and actual.Celda.columna == columna:
                return actual
            actual = actual.siguiente
        
        return None   
    
    def recorrerMatriz(self):
        actual = self.primero

        while actual != None:
            print(" Fila -> " + str(actual.Celda.fila) + 
                  " Columna -> " + str(actual.Celda.columna) + 
                  " Color: " + actual.Celda.color)
            
            actual = actual.siguiente 
            
            
    def limpiarMatriz(self):
        self.primero = None
        self.columnas = None
        
        
        
    def imprimirPatron(self):
        contador = 0
        columnas = self.columnas
        actual = self.primero

        while actual != None:
            
            if contador == int(columnas):
                print("")
                contador = 0
            if actual.Celda.color == "W":
                print("█",end="")
            if actual.Celda.color == "B":
                print("▒",end="")  
            contador += 1
            
            actual = actual.siguiente 
            

    

        