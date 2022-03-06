from NodoMatriz import *
from claseCelda import *
import os
import pydot
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
                      
    def graficar(self,filasxcolumnas,iteracion,file):
        actual = self.primero 
        contador = 1
         
        while actual != None:
           nodoN = filasxcolumnas*iteracion + contador
           if actual.Celda.color == 'W': 
            cadena = "nodo{} [fillcolor=white fixedsize=true label=\"(x={},y={})\"]\n".format(nodoN,actual.Celda.columna,actual.Celda.fila)
           else:
            cadena = "nodo{} [fillcolor=gray fixedsize=true label=\"(x={},y={})\"]\n".format(nodoN,actual.Celda.columna,actual.Celda.fila)
           
           contador += 1 
           file.write(cadena)
           actual = actual.siguiente 
           
    def unirNodos(self,totalNodos,file,filasxcolumnas):
           contador = 1
           aux = 1 
           while contador < totalNodos:
               if aux == filasxcolumnas:
                  cadena = "nodo{}\n".format(contador)
                  aux = 0
               else:
                  cadena = "nodo{}->".format(contador)
                  
               file.write(cadena)
               contador += 1
               aux +=1
                            
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
            

    

        