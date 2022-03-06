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
        
    def recorrerPatrones(self,columnas):
        actual = self.primero
        contador = 0 
        c = columnas
        while actual != None:
            contador += 1
            print("  ╚Código {}: ".format(contador) + actual.Patron.codigo)
            print("   ╚Patron: ")
            self.imprimirPatron(actual.Patron.patron,c)
            print("\n")
            actual = actual.siguiente
    
    def buscarPatron(self,codigoPatron):
        actual = self.primero 
        
        while actual and actual.Patron.codigo != codigoPatron:
            actual = actual.siguiente 
        if actual:
            return actual.Patron.patron
        else:
            print("No se encontró el patrón ")  
            return None
    
    def imprimirPatron(self,patron,c):
        contador = 0
        columnas = c 
        print("\t")
        for letra in patron:
            if contador == int(columnas):
                print("")
                contador = 0
            if letra == "W":
                print("█",end="")
            if letra == "B":
                print("▒",end="")  
            contador += 1
           
    def ordenarPatrones(self):
        actual = self.primero 
        if actual != None:
            while actual:
                nodoTemp = actual.siguiente
                while nodoTemp:
                    if actual.Patron.codigo > nodoTemp.Patron.codigo:
                        aux = actual.Patron
                        actual.Patron = nodoTemp.Patron
                        nodoTemp.Patron = aux
                    nodoTemp = nodoTemp.siguiente
                actual = actual.siguiente  