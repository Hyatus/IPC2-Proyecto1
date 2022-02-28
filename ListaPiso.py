from NodoPiso import *
from clasePiso import *

class ListaPiso:
    def __init__(self) -> None:
        self.primero = None 
        
    def insertarPiso(self,Piso):
        if self.primero == None:
            self.primero = NodoPiso(Piso=Piso)
            return
        
        actual = self.primero 
        while actual.siguiente:
            actual = actual.siguiente
        
        actual.siguiente = NodoPiso(Piso=Piso)
            
        
    def recorrerPisosyPatrones(self):
        actual = self.primero
        contador = 0
        while actual != None:
            contador += 1
            print("╬ Piso {} : ".format(contador) + actual.Piso.nombre +
                  " Filas: " + actual.Piso.filas + 
                  " Columnas: " + actual.Piso.columnas + 
                  " Costo por Volteo: "  + actual.Piso.costoVolteo + 
                  " Costo por Intercambio " + actual.Piso.costoIntercambio)
            actual.Piso.patrones.recorrerPatrones(actual.Piso.columnas)
            actual = actual.siguiente 
    
    
    def ordenarPisos(self):
        actual = self.primero 
        if actual != None:
            while actual:
                nodoTemp = actual.siguiente
                while nodoTemp:
                    if actual.Piso.nombre > nodoTemp.Piso.nombre:
                        aux = actual.Piso
                        actual.Piso = nodoTemp.Piso
                        nodoTemp.Piso = aux
                    nodoTemp = nodoTemp.siguiente
                actual.Piso.patrones.ordenarPatrones()
                actual = actual.siguiente
        
 
    def buscarPiso(self,nombrePiso):
        actual = self.primero 
        
        while actual and actual.Piso.nombre != nombrePiso:
            actual = actual.siguiente
            
        if actual:
            return actual 
        else:
            return None   
            
            
            
    