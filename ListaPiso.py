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
            
        
    def recorrerPiso(self):
        
        actual = self.primero
        
        while actual != None:
            print("Nombre: " + actual.Piso.nombre +
                  " Filas: " + actual.Piso.filas + 
                  " Columnas: " + actual.Piso.columnas + 
                  " Costo por Volteo: "  + actual.Piso.costoVolteo + 
                  " Costo por Intercambio " + actual.Piso.costoIntercambio)
            actual.Piso.patrones.recorrerPatrones()
            actual = actual.siguiente 
            
            
    def buscarPiso(self,nombrePiso):
        actual = self.primero 
        anterior = None
        
        while actual and actual.Piso.nombre != nombrePiso:
            anterior = actual 
            actual = actual.siguiente
            
        if actual:
            return actual 
        else:
            print("No se encontró ")    
            
            
            
    