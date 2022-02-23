from NodoPatron import *
from clasePatron import*


class ListaPatron():
    def __init__(self):
        self.primero = None
        
    def insertarPatron(self,Patron):
        if self.primero == None: #Si el primero es vacío 
            self.primero = NodoPatron(Patron=Patron)
            return
        actual = self.primero #Vamos a recorrer la lista hasta encontrar un nodo vacío 
        
        while actual.siguiente: #Mientras no sea vacío
            actual = actual.siguiente
        #Al llegar aquí es que encontró un nodo vacío entonces insertamos un nuevo nodo y lo enlazamos 
        actual.siguiente = NodoPatron(Patron=Patron)
        
    
    def recorrerPatrones(self):
        actual = self.primero 
        while actual != None:
            print("Nombre del Patrón: " + actual.Patron.codigo, "Patrón: " + actual.Patron.patron)
            actual = actual.siguiente
    
    def buscarPatron(self,nombre):
        actual = self.primero 
        anterior = None 
        
        while actual and actual.nombre != nombre:
            anterior = actual
            actual = actual.siguiente 
            
        if actual:
            print("Nombre del Patrón: " + actual.nombre, "Patrón: " + actual.patron)
        else:
            print("No se encontró el patrón ")    