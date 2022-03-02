from NodoMatriz import *
from claseCelda import *
from ListaMatrizO import *

class ListaMatrizD():
    
    def __init__(self) -> None:
        self.primero = None
        self.sizeLista = 0
    
    
    def insertarCelda(self,Celda):
        if self.primero == None:
            self.primero = NodoMatriz(Celda=Celda,posicion=self.sizeLista)
            self.sizeLista += 1
            return
        
        actual = self.primero 
        while actual.siguiente:
            actual = actual.siguiente
        
        actual.siguiente = NodoMatriz(Celda=Celda,anterior=actual,posicion=self.sizeLista)
        self.sizeLista += 1
        
    
    def recorrerMatriz(self):
        actual = self.primero

        while actual != None:
            print(" Columna -> " + str(actual.Celda.columna) + " Fila -> " + str(actual.Celda.fila) + " Color: " + actual.Celda.color)
            actual = actual.siguiente 
            
            
   
    def recorrerInverso(self,matrizO,costoV,costoI,costoTotal):
        #print("Última posicion " + str(self.sizeLista-1))
        ultimo = self.buscarNodo(self.sizeLista-1)   
        costoVolteo = int(costoV)
        costoIntercambio = int(costoI)
        costoTot = costoTotal
        while ultimo:
            posXMD = ultimo.Celda.columna
            posYMD = ultimo.Celda.fila
            buscarCeldaMO = matrizO.buscarCelda(posYMD,posXMD)
            if buscarCeldaMO.Celda.color != ultimo.Celda.color:
                buscarCeldaMOIzquierda = matrizO.buscarCelda(posYMD,posXMD-1)
                buscarCeldaMOArriba = matrizO.buscarCelda(posYMD-1,posXMD) 
                if buscarCeldaMOIzquierda and buscarCeldaMOIzquierda.Celda.color == ultimo.Celda.   color and buscarCeldaMOIzquierda.Celda.cambio != True:
                    #Si la celda a la derecha existe y es del mismo color realizará el intercambio 
                    colorAux = buscarCeldaMO.Celda.color #Almacena el color de la celda Original
                    buscarCeldaMO.Celda.color = buscarCeldaMOIzquierda.Celda.color
                    buscarCeldaMO.Celda.cambio = True
                    buscarCeldaMOIzquierda.Celda.color = colorAux
                    print("Se realizó un intercambio de color de la celda ({},{})".format(buscarCeldaMOIzquierda.Celda.fila, buscarCeldaMOIzquierda.Celda.columna) + 
                          " A la posición  -> ({},{}) ".format(buscarCeldaMO.Celda.fila,buscarCeldaMO.Celda.columna))
                    costoTot += costoIntercambio
                else:
                    if buscarCeldaMOArriba and buscarCeldaMOArriba.Celda.color == ultimo.Celda.color and buscarCeldaMOArriba.Celda.cambio != True:
                        colorAux = buscarCeldaMO.Celda.color 
                        buscarCeldaMO.Celda.color = buscarCeldaMOArriba.Celda.color
                        buscarCeldaMO.Celda.cambio = True
                        buscarCeldaMOArriba.Celda.color = colorAux
                        print("Se realizó un intercambio de color de la celda ({},{})".format(buscarCeldaMOArriba.Celda.fila, buscarCeldaMOArriba.Celda.columna) + 
                          " A la posición  -> ({},{}) ".format(buscarCeldaMO.Celda.fila,buscarCeldaMO.Celda.columna))
                        costoTot += costoIntercambio
                    else:
                        buscarCeldaMO.Celda.color = ultimo.Celda.color
                        buscarCeldaMO.Celda.cambio = True
                        print("Se realizó un volteo en la celda ({},{}) ".format(buscarCeldaMO.Celda.fila,buscarCeldaMO.Celda.columna))
                        costoTotal += costoVolteo
                
            ultimo = ultimo.anterior
        
        print("El costo total de este algoritmo fue " + str(costoTot))
            
            

    def buscarNodo(self,posicion):
      actual = self.primero 
      while actual:
        if actual.posicion == posicion:
           return actual
        actual = actual.siguiente

      return None
            
    def algoritmoA(self,matrizO,costoV,costoI):
        '''
        Conforme recorro la matriz de destino voy comparando la celda de la matriz de destino contra la misma celda de la matriz de Origen, si la celda es distinta entonces en el caso de este algoritmo primero le daré prioridad al nodo de la derecha y luego si este no es igual al color que estoy buscando buscaré en el nodo de abajo y si este tampoco es igual entonces haré un volteo 
        '''
        print("====== ALGORITMO A ======== ")
        actual = self.primero
        costoVolteo = int(costoV)
        costoIntercambio = int(costoI)
        costoTotal = 0
        #print("Costo por Volteo "  +  costoVolteo)
        #print("Costo por intercambio " + costoIntercambio)
        while actual != None:
            posXMD = actual.Celda.columna
            posYMD = actual.Celda.fila
            buscarCeldaMO = matrizO.buscarCelda(posYMD,posXMD)
            if buscarCeldaMO.Celda.color != actual.Celda.color:
                #print("El piso en la posicion ({} , {}) NO tiene el mismo color que la #celda de Destino ".format(posXMD,posYMD))
                #BUSCA LA CELDA DE LA DERECHA PRIMERO 
                buscarCeldaMODerecha = matrizO.buscarCelda(posYMD,posXMD+1)
                buscarCeldaMOAbajo = matrizO.buscarCelda(posYMD+1,posXMD)
                #if buscarCeldaMODerecha:
                #    print("Resultado de la celda derecha en pos ({},{}) ".format(posYMD,posXMD+1) + buscarCeldaMODerecha.Celda.color)
                #else:
                #    print("No se encontró el nodo de la derecha ") 
                if buscarCeldaMODerecha and buscarCeldaMODerecha.Celda.color == actual.Celda.color:
                    #Si la celda a la derecha existe y es del mismo color realizará el intercambio 
                    colorAux = buscarCeldaMO.Celda.color #Almacena el color de la celda Original
                    buscarCeldaMO.Celda.color = buscarCeldaMODerecha.Celda.color
                    buscarCeldaMODerecha.Celda.color = colorAux
                    print("Se realizó un intercambio de color de la celda ({},{})".format(buscarCeldaMODerecha.Celda.fila, buscarCeldaMODerecha.Celda.columna) + 
                          " A la posición  -> ({},{}) ".format(buscarCeldaMO.Celda.fila,buscarCeldaMO.Celda.columna))
                    costoTotal += costoIntercambio
                else:
                    if buscarCeldaMOAbajo and buscarCeldaMOAbajo.Celda.color == actual.Celda.color:
                        colorAux = buscarCeldaMO.Celda.color 
                        buscarCeldaMO.Celda.color = buscarCeldaMOAbajo.Celda.color
                        buscarCeldaMOAbajo.Celda.color = colorAux
                        print("Se realizó un intercambio de color de la celda ({},{})".format(buscarCeldaMOAbajo.Celda.fila, buscarCeldaMOAbajo.Celda.columna) + 
                          " A la posición  -> ({},{}) ".format(buscarCeldaMO.Celda.fila,buscarCeldaMO.Celda.columna))
                        costoTotal += costoIntercambio
                    else:
                        buscarCeldaMO.Celda.color = actual.Celda.color
                        print("Se realizó un volteo en la celda ({},{}) ".format(buscarCeldaMO.Celda.fila,buscarCeldaMO.Celda.columna))
                        costoTotal += costoVolteo
                     
            actual = actual.siguiente
            
        print("El costo total fue: " + str(costoTotal))                   
        #matrizO.recorrerMatriz()
        
    def algoritmoB(self,matrizO,costoV,costoI):
        '''
        Conforme recorro la matriz de destino voy comparando la celda de la matriz de destino contra la misma celda de la matriz de Origen, si la celda es distinta entonces en el caso de este algoritmo primero le daré prioridad al nodo de abajo y luego si este no es igual al color que estoy buscando buscaré en el nodo de la derecha y si este tampoco es igual entonces haré un volteo 
        '''
        print("====== ALGORITMO B ======== ")
        actual = self.primero
        costoVolteo = int(costoV)
        costoIntercambio = int(costoI)
        costoTotal = 0
        while actual != None:
            posXMD = actual.Celda.columna
            posYMD = actual.Celda.fila
            buscarCeldaMO = matrizO.buscarCelda(posYMD,posXMD)
            if buscarCeldaMO.Celda.color != actual.Celda.color:
                buscarCeldaMODerecha = matrizO.buscarCelda(posYMD,posXMD+1)
                buscarCeldaMOAbajo = matrizO.buscarCelda(posYMD+1,posXMD)

                if buscarCeldaMOAbajo and buscarCeldaMOAbajo.Celda.color == actual.Celda.color:
                    #Si la celda a la derecha existe y es del mismo color realizará el intercambio 
                    colorAux = buscarCeldaMO.Celda.color #Almacena el color de la celda Original
                    buscarCeldaMO.Celda.color = buscarCeldaMOAbajo.Celda.color
                    buscarCeldaMOAbajo.Celda.color = colorAux
                    print("Se realizó un intercambio de color de la celda ({},{})".format(buscarCeldaMOAbajo.Celda.fila, buscarCeldaMOAbajo.Celda.columna) + 
                          " A la posición  -> ({},{}) ".format(buscarCeldaMO.Celda.fila,buscarCeldaMO.Celda.columna))
                    costoTotal += costoIntercambio
                else:
                    if buscarCeldaMODerecha and buscarCeldaMODerecha.Celda.color == actual.Celda.color:
                        colorAux = buscarCeldaMO.Celda.color 
                        buscarCeldaMO.Celda.color = buscarCeldaMODerecha.Celda.color
                        buscarCeldaMODerecha.Celda.color = colorAux
                        print("Se realizó un intercambio de color de la celda ({},{})".format(buscarCeldaMODerecha.Celda.fila, buscarCeldaMODerecha.Celda.columna) + 
                          " A la posición  -> ({},{}) ".format(buscarCeldaMO.Celda.fila,buscarCeldaMO.Celda.columna))
                        costoTotal += costoIntercambio
                    else:
                        buscarCeldaMO.Celda.color = actual.Celda.color
                        print("Se realizó un volteo en la celda ({},{}) ".format(buscarCeldaMO.Celda.fila,buscarCeldaMO.Celda.columna))
                        costoTotal += costoVolteo
                     
            actual = actual.siguiente
            
        print("El costo total fue: " + str(costoTotal))                   
        #matrizO.recorrerMatriz()
        #PRIMERO ABAJO LUEGO DERECHA
        
    def algoritmoC(self,matrizO,costoV):
        '''
        Este algoritmo convierte la matriz de origen a la matriz de destino sólo con volteos 
        '''
        actual = self.primero
        costoVolteo = int(costoV)
        costoTotal = 0
        while actual != None:
            posXMD = actual.Celda.columna
            posYMD = actual.Celda.fila
            buscarCeldaMO = matrizO.buscarCelda(posYMD,posXMD)
            if buscarCeldaMO.Celda.color != actual.Celda.color:
                
                buscarCeldaMO.Celda.color = actual.Celda.color
                print("Se realizó un volteo en la celda ({},{}) ".format(buscarCeldaMO.Celda.fila,buscarCeldaMO.Celda.columna))
                costoTotal += costoVolteo
                                    
            actual = actual.siguiente
            
        print("El costo total fue: " + str(costoTotal))                   
        #matrizO.recorrerMatriz()
        #LE DA VUELTA A TODOS 
        
    def algoritmoD(self,matrizO,costoV,costoI):
        '''
        Conforme recorro la matriz de destino voy comparando la celda de la matriz de destino contra la misma celda de la matriz de Origen, si la celda es distinta entonces en el caso de este algoritmo primero le daré prioridad al nodo de la derecha y luego si este no es igual al color que estoy buscando buscaré en el nodo de abajo y si este tampoco es igual entonces haré un volteo 
        '''
        print("====== ALGORITMO D ======== ")
        actual = self.primero
        costoVolteo = int(costoV)
        costoIntercambio = int(costoI)
        costoTotal = 0
        #print("Costo por Volteo "  +  costoVolteo)
        #print("Costo por intercambio " + costoIntercambio)
        while actual != None:
            posXMD = actual.Celda.columna
            posYMD = actual.Celda.fila
            buscarCeldaMO = matrizO.buscarCelda(posYMD,posXMD)
            if buscarCeldaMO.Celda.color != actual.Celda.color:
                #print("El piso en la posicion ({} , {}) NO tiene el mismo color que la #celda de Destino ".format(posXMD,posYMD))
                #BUSCA LA CELDA DE LA DERECHA PRIMERO 
                buscarCeldaMODerecha = matrizO.buscarCelda(posYMD,posXMD+1)
                buscarCeldaMOAbajo = matrizO.buscarCelda(posYMD+1,posXMD)
                #if buscarCeldaMODerecha:
                #    print("Resultado de la celda derecha en pos ({},{}) ".format(posYMD,posXMD+1) + buscarCeldaMODerecha.Celda.color)
                #else:
                #    print("No se encontró el nodo de la derecha ") 
                if buscarCeldaMODerecha and buscarCeldaMODerecha.Celda.color == actual.Celda.color:
                    #Si la celda a la derecha existe y es del mismo color realizará el intercambio 
                    colorAux = buscarCeldaMO.Celda.color #Almacena el color de la celda Original
                    buscarCeldaMO.Celda.color = buscarCeldaMODerecha.Celda.color
                    buscarCeldaMO.Celda.cambio = True
                    buscarCeldaMODerecha.Celda.color = colorAux
                    print("Se realizó un intercambio de color de la celda ({},{})".format(buscarCeldaMODerecha.Celda.fila, buscarCeldaMODerecha.Celda.columna) + 
                          " A la posición  -> ({},{}) ".format(buscarCeldaMO.Celda.fila,buscarCeldaMO.Celda.columna))
                    costoTotal += costoIntercambio
                else:
                    if buscarCeldaMOAbajo and buscarCeldaMOAbajo.Celda.color == actual.Celda.color:
                        colorAux = buscarCeldaMO.Celda.color 
                        buscarCeldaMO.Celda.color = buscarCeldaMOAbajo.Celda.color
                        buscarCeldaMO.Celda.cambio = True
                        buscarCeldaMOAbajo.Celda.color = colorAux
                        print("Se realizó un intercambio de color de la celda ({},{})".format(buscarCeldaMOAbajo.Celda.fila, buscarCeldaMOAbajo.Celda.columna) + 
                          " A la posición  -> ({},{}) ".format(buscarCeldaMO.Celda.fila,buscarCeldaMO.Celda.columna))
                        costoTotal += costoIntercambio
                    else:
                        buscarCeldaMO.Celda.color = actual.Celda.color
                        buscarCeldaMO.Celda.cambio = True
                        print("Se realizó un volteo en la celda ({},{}) ".format(buscarCeldaMO.Celda.fila,buscarCeldaMO.Celda.columna))
                        costoTotal += costoVolteo
                        self.recorrerInverso(matrizO,costoV,costoI,costoTotal) 
                        actual = self.buscarNodo(self.sizeLista-1)     
            actual = actual.siguiente
            
        #print("El costo total fue: " + str(costoTotal))                   
        #matrizO.recorrerMatriz()
        
        
        
