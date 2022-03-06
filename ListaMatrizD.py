from NodoMatriz import *
from claseCelda import *
from ListaMatrizO import *

class ListaMatrizD():
    
    def __init__(self) -> None:
        self.primero = None
        self.sizeLista = 0
                 
    def limpiarMatriz(self):
        self.primero = None
    
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
                          
    def recorrerInverso(self,matrizO,texto,filasxcolumnas,iteracion,file):
        #print("Última posicion " + str(self.sizeLista-1))
        ultimo = self.buscarNodo(self.sizeLista-1)   
        while ultimo:
            posXMD = ultimo.Celda.columna
            posYMD = ultimo.Celda.fila
            buscarCeldaMO = matrizO.buscarCelda(posYMD,posXMD)
            if buscarCeldaMO.Celda.color != ultimo.Celda.color:
                buscarCeldaMOIzquierda = matrizO.buscarCelda(posYMD,posXMD-1)
                buscarCeldaMOArriba = matrizO.buscarCelda(posYMD-1,posXMD) 
                if buscarCeldaMOIzquierda and buscarCeldaMOIzquierda.Celda.color == ultimo.Celda.color and buscarCeldaMOIzquierda.Celda.cambio != True:
                    #Si la celda a la derecha existe y es del mismo color realizará el intercambio 
                    colorAux = buscarCeldaMO.Celda.color #Almacena el color de la celda Original
                    buscarCeldaMO.Celda.color = buscarCeldaMOIzquierda.Celda.color
                    buscarCeldaMO.Celda.cambio = True
                    buscarCeldaMOIzquierda.Celda.color = colorAux
                    if texto:
                        print("Se realizó un intercambio de color de la celda ({},{})".format(buscarCeldaMOIzquierda.Celda.fila, buscarCeldaMOIzquierda.Celda.columna) + 
                          " A la posición  -> ({},{}) ".format(buscarCeldaMO.Celda.fila,buscarCeldaMO.Celda.columna))
                        print("\n")
                        matrizO.imprimirPatron()
                        print("\n")
                    else:
                         matrizO.graficar(filasxcolumnas,iteracion,file)
                         iteracion +=1     
                else:
                    if buscarCeldaMOArriba and buscarCeldaMOArriba.Celda.color == ultimo.Celda.color and buscarCeldaMOArriba.Celda.cambio != True:
                        colorAux = buscarCeldaMO.Celda.color 
                        buscarCeldaMO.Celda.color = buscarCeldaMOArriba.Celda.color
                        buscarCeldaMO.Celda.cambio = True
                        buscarCeldaMOArriba.Celda.color = colorAux
                        if texto:
                            print("Se realizó un intercambio de color de la celda ({},{})".format(buscarCeldaMOArriba.Celda.fila, buscarCeldaMOArriba.Celda.columna) + 
                            " A la posición  -> ({},{}) ".format(buscarCeldaMO.Celda.fila,buscarCeldaMO.Celda.columna))
                            print("\n")
                            matrizO.imprimirPatron()
                            print("\n")
                        else:
                             matrizO.graficar(filasxcolumnas,iteracion,file)
                             iteracion +=1    
                    elif buscarCeldaMO.Celda.cambio != True:
                         buscarCeldaMO.Celda.color = ultimo.Celda.color
                         buscarCeldaMO.Celda.cambio = True
                         if texto:
                            print("Se realizó un volteo en la celda ({},{}) ".format(buscarCeldaMO.Celda.fila,buscarCeldaMO.Celda.columna))
                            print("\n")
                            matrizO.imprimirPatron()
                            print("\n")
                         else:
                            matrizO.graficar(filasxcolumnas,iteracion,file)
                            iteracion +=1

            ultimo = ultimo.anterior
                 
    def buscarNodo(self,posicion):
      actual = self.primero 
      while actual:
        if actual.posicion == posicion:
           return actual
        actual = actual.siguiente

      return None

#   ---------------------- ALGORITMOS CON TEXTO --------------------------------- # 
            
    def algoritmoA(self,matrizO,texto,columnasPiso,filasPiso):
        '''
        Conforme recorro la matriz de destino voy comparando la celda de la matriz de destino contra la misma celda de la matriz de Origen, si la celda es distinta entonces en el caso de este algoritmo primero le daré prioridad al nodo de la derecha y luego si este no es igual al color que estoy buscando buscaré en el nodo de abajo y si este tampoco es igual entonces haré un volteo 
        '''
        actual = self.primero
        # Variables para generar el grafo 
        iteracion = 0
        filasxcolumnas = int(columnasPiso)*int(filasPiso)
        cadena = 'digraph {\n'
        cadena += "node [margin=0 fontcolor=blue fontsize=10 width=1 shape=box style=filled]\n"
        file = open("algoritmoA.dot", "w+")
        file.write(cadena)
        # ---------------------------------------
        
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
                    if texto:
                        print("Se realizó un intercambio de color de la celda ({},{})".format(buscarCeldaMODerecha.Celda.fila, buscarCeldaMODerecha.Celda.columna) + 
                          " A la posición  -> ({},{}) ".format(buscarCeldaMO.Celda.fila,buscarCeldaMO.Celda.columna))
                        print("\n")
                        matrizO.imprimirPatron()
                        print("\n")
                    else: 
                        matrizO.graficar(filasxcolumnas,iteracion,file)
                        iteracion +=1
                else:
                    if buscarCeldaMOAbajo and buscarCeldaMOAbajo.Celda.color == actual.Celda.color:
                        colorAux = buscarCeldaMO.Celda.color 
                        buscarCeldaMO.Celda.color = buscarCeldaMOAbajo.Celda.color
                        buscarCeldaMOAbajo.Celda.color = colorAux
                        if texto:
                            print("Se realizó un intercambio de color de la celda ({},{})".format(buscarCeldaMOAbajo.Celda.fila, buscarCeldaMOAbajo.Celda.columna) + 
                            " A la posición  -> ({},{}) ".format(buscarCeldaMO.Celda.fila,buscarCeldaMO.Celda.columna))
                            print("\n")
                            matrizO.imprimirPatron()
                            print("\n")
                        else: 
                            matrizO.graficar(filasxcolumnas,iteracion,file)
                            iteracion +=1
                    else:
                        buscarCeldaMO.Celda.color = actual.Celda.color
                        if texto:
                            print("Se realizó un volteo en la celda ({},{}) ".format(buscarCeldaMO.Celda.fila,buscarCeldaMO.Celda.columna))
                            print("\n")
                            matrizO.imprimirPatron()
                            print("\n")
                        else: 
                            matrizO.graficar(filasxcolumnas,iteracion,file)
                            iteracion +=1
                     
            actual = actual.siguiente
        cadena = "}"
        cadena = "rankdir=LR\n"
        file.write(cadena)
        totalNodos = filasxcolumnas*iteracion + 1 
        matrizO.unirNodos(totalNodos,file,filasxcolumnas)
        cadena = "\n}"
        file.write(cadena)
        file.close()
        os.system('dot -Tpng algoritmoA.dot -o algoritmoA.png')
             
    def algoritmoB(self,matrizO,texto,columnasPiso,filasPiso):
        '''
        Conforme recorro la matriz de destino voy comparando la celda de la matriz de destino contra la misma celda de la matriz de Origen, si la celda es distinta entonces en el caso de este algoritmo primero le daré prioridad al nodo de abajo y luego si este no es igual al color que estoy buscando buscaré en el nodo de la derecha y si este tampoco es igual entonces haré un volteo 
        '''
        actual = self.primero
        # Variables para generar el grafo 
        iteracion = 0
        filasxcolumnas = int(columnasPiso)*int(filasPiso)
        cadena = 'digraph {\n'
        cadena += "node [margin=0 fontcolor=blue fontsize=10 width=1 shape=box style=filled]\n"
        file = open("algoritmoB.dot", "w+")
        file.write(cadena)
        # ---------------------------------------
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
                    if texto:
                        print("Se realizó un intercambio de color de la celda ({},{})".format(buscarCeldaMOAbajo.Celda.fila, buscarCeldaMOAbajo.Celda.columna) + 
                          " A la posición  -> ({},{}) ".format(buscarCeldaMO.Celda.fila,buscarCeldaMO.Celda.columna))
                        print("\n")
                        matrizO.imprimirPatron()
                        print("\n")
                    else: 
                        matrizO.graficar(filasxcolumnas,iteracion,file)
                        iteracion +=1
                else:
                    if buscarCeldaMODerecha and buscarCeldaMODerecha.Celda.color == actual.Celda.color:
                        colorAux = buscarCeldaMO.Celda.color 
                        buscarCeldaMO.Celda.color = buscarCeldaMODerecha.Celda.color
                        buscarCeldaMODerecha.Celda.color = colorAux
                        if texto:
                            print("Se realizó un intercambio de color de la celda ({},{})".format(buscarCeldaMODerecha.Celda.fila, buscarCeldaMODerecha.Celda.columna) + 
                            " A la posición  -> ({},{}) ".format(buscarCeldaMO.Celda.fila,buscarCeldaMO.Celda.columna))
                            print("\n")
                            matrizO.imprimirPatron()
                            print("\n")
                        else: 
                            matrizO.graficar(filasxcolumnas,iteracion,file)
                            iteracion +=1
                    else:
                        buscarCeldaMO.Celda.color = actual.Celda.color
                        if texto:
                            print("Se realizó un volteo en la celda ({},{}) ".format(buscarCeldaMO.Celda.fila,buscarCeldaMO.Celda.columna))
                            print("\n")
                            matrizO.imprimirPatron()
                            print("\n")
                        else: 
                            matrizO.graficar(filasxcolumnas,iteracion,file)
                            iteracion +=1
                     
            actual = actual.siguiente
        cadena = "}"
        cadena = "rankdir=LR\n"
        file.write(cadena)
        totalNodos = filasxcolumnas*iteracion + 1 
        matrizO.unirNodos(totalNodos,file,filasxcolumnas)
        cadena = "\n}"
        file.write(cadena)
        file.close()
        os.system('dot -Tpng algoritmoB.dot -o algoritmoB.png')
                           
    def algoritmoD(self,matrizO,texto,columnasPiso,filasPiso):
        '''
        Conforme recorro la matriz de destino voy comparando la celda de la matriz de destino contra la misma celda de la matriz de Origen, si la celda es distinta entonces en el caso de este algoritmo primero le daré prioridad al nodo de la derecha y luego si este no es igual al color que estoy buscando buscaré en el nodo de abajo y si este tampoco es igual entonces haré un volteo 
        '''
        # Variables para generar el grafo 
        iteracion = 0
        filasxcolumnas = int(columnasPiso)*int(filasPiso)
        cadena = 'digraph {\n'
        cadena += "node [margin=0 fontcolor=blue fontsize=10 width=1 shape=box style=filled]\n"
        file = open("algoritmoD.dot", "w+")
        file.write(cadena)
        # ---------------------------------------
        actual = self.primero
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
                    if texto:
                        print("Se realizó un intercambio de color de la celda ({},{})".format(buscarCeldaMODerecha.Celda.fila, buscarCeldaMODerecha.Celda.columna) + 
                          " A la posición  -> ({},{}) ".format(buscarCeldaMO.Celda.fila,buscarCeldaMO.Celda.columna))
                        print("\n")
                        matrizO.imprimirPatron()
                        print("\n")
                    else: 
                        matrizO.graficar(filasxcolumnas,iteracion,file)
                        iteracion +=1   
                else:
                    if buscarCeldaMOAbajo and buscarCeldaMOAbajo.Celda.color == actual.Celda.color:
                        colorAux = buscarCeldaMO.Celda.color 
                        buscarCeldaMO.Celda.color = buscarCeldaMOAbajo.Celda.color
                        buscarCeldaMO.Celda.cambio = True
                        buscarCeldaMOAbajo.Celda.color = colorAux
                        if texto:
                            print("Se realizó un intercambio de color de la celda ({},{})".format(buscarCeldaMOAbajo.Celda.fila, buscarCeldaMOAbajo.Celda.columna) + 
                          " A la posición  -> ({},{}) ".format(buscarCeldaMO.Celda.fila,buscarCeldaMO.Celda.columna))
                            print("\n")
                            matrizO.imprimirPatron()
                            print("\n")
                        else:
                            matrizO.graficar(filasxcolumnas,iteracion,file)
                            iteracion +=1  
                    else:
                        buscarCeldaMO.Celda.color = actual.Celda.color
                        buscarCeldaMO.Celda.cambio = True
                        if texto:
                            print("Se realizó un volteo en la celda ({},{}) ".format(buscarCeldaMO.Celda.fila,buscarCeldaMO.Celda.columna))
                            print("\n")
                            matrizO.imprimirPatron()
                            print("\n")
                        else:
                            matrizO.graficar(filasxcolumnas,iteracion,file)
                            iteracion +=1  
                        self.recorrerInverso(matrizO,texto,filasxcolumnas,iteracion,file) 
                        #actual = self.buscarNodo(self.sizeLista-1)
            else:
                        buscarCeldaMO.Celda.cambio = True 
                                    
            actual = actual.siguiente 
        cadena = "}"
        cadena = "rankdir=LR\n"
        file.write(cadena)
        totalNodos = filasxcolumnas*iteracion + 1 
        matrizO.unirNodos(totalNodos,file,filasxcolumnas)
        cadena = "\n}"
        file.write(cadena)
        file.close()
        os.system('dot -Tpng algoritmoD.dot -o algoritmoD.png')               
        
#   ---------------------- ALGORITMOS SIN TEXTO --------------------------------- #  

    def recorrerInversoST(self,matrizO,costoV,costoI,costoTotal):
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
                    costoTot += costoIntercambio
                else:
                    if buscarCeldaMOArriba and buscarCeldaMOArriba.Celda.color == ultimo.Celda.color and buscarCeldaMOArriba.Celda.cambio != True:
                        colorAux = buscarCeldaMO.Celda.color 
                        buscarCeldaMO.Celda.color = buscarCeldaMOArriba.Celda.color
                        buscarCeldaMO.Celda.cambio = True
                        buscarCeldaMOArriba.Celda.color = colorAux
                        costoTot += costoIntercambio
                    elif buscarCeldaMO.Celda.cambio != True:
                        buscarCeldaMO.Celda.color = ultimo.Celda.color
                        buscarCeldaMO.Celda.cambio = True
                        costoTot += costoVolteo
                
            ultimo = ultimo.anterior
    
        return costoTot
        
    def algoritmoAST(self,matrizO,costoV,costoI):
        '''
        Conforme recorro la matriz de destino voy comparando la celda de la matriz de destino contra la misma celda de la matriz de Origen, si la celda es distinta entonces en el caso de este algoritmo primero le daré prioridad al nodo de la derecha y luego si este no es igual al color que estoy buscando buscaré en el nodo de abajo y si este tampoco es igual entonces haré un volteo 
        '''
        # ------------ ALGORITMO A - SIN TEXTO -------------------
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
                if buscarCeldaMODerecha and buscarCeldaMODerecha.Celda.color == actual.Celda.color:
                    #Si la celda a la derecha existe y es del mismo color realizará el intercambio 
                    colorAux = buscarCeldaMO.Celda.color #Almacena el color de la celda Original
                    buscarCeldaMO.Celda.color = buscarCeldaMODerecha.Celda.color
                    buscarCeldaMODerecha.Celda.color = colorAux
                    costoTotal += costoIntercambio
                else:
                    if buscarCeldaMOAbajo and buscarCeldaMOAbajo.Celda.color == actual.Celda.color:
                        colorAux = buscarCeldaMO.Celda.color 
                        buscarCeldaMO.Celda.color = buscarCeldaMOAbajo.Celda.color
                        buscarCeldaMOAbajo.Celda.color = colorAux
                        costoTotal += costoIntercambio
                    else:
                        buscarCeldaMO.Celda.color = actual.Celda.color
                        costoTotal += costoVolteo
                     
            actual = actual.siguiente
        return costoTotal  #DEVUELVE EL COSTO DE ESTE ALGORITMO 

    def algoritmoBST(self,matrizO,costoV,costoI):
        '''
        Conforme recorro la matriz de destino voy comparando la celda de la matriz de destino contra la misma celda de la matriz de Origen, si la celda es distinta entonces en el caso de este algoritmo primero le daré prioridad al nodo de abajo y luego si este no es igual al color que estoy buscando buscaré en el nodo de la derecha y si este tampoco es igual entonces haré un volteo 
        '''
        # ===================== ALGORITMO B - SIN TEXTO ===================== #
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
                    costoTotal += costoIntercambio
                else:
                    if buscarCeldaMODerecha and buscarCeldaMODerecha.Celda.color == actual.Celda.color:
                        colorAux = buscarCeldaMO.Celda.color 
                        buscarCeldaMO.Celda.color = buscarCeldaMODerecha.Celda.color
                        buscarCeldaMODerecha.Celda.color = colorAux
                        costoTotal += costoIntercambio
                    else:
                        buscarCeldaMO.Celda.color = actual.Celda.color
                        costoTotal += costoVolteo
                     
            actual = actual.siguiente
        return costoTotal    

    def algoritmoCST(self,matrizO,costoV):
        '''
        Este algoritmo convierte la matriz de origen a la matriz de destino sólo con volteos 
        '''
        # ============================ ALGORITMO C - SIN TEXTO ===================== #
        actual = self.primero
        costoVolteo = int(costoV)
        costoTotal = 0
        while actual != None:
            posXMD = actual.Celda.columna
            posYMD = actual.Celda.fila
            buscarCeldaMO = matrizO.buscarCelda(posYMD,posXMD)
            if buscarCeldaMO.Celda.color != actual.Celda.color:
                buscarCeldaMO.Celda.color = actual.Celda.color
                costoTotal += costoVolteo
                                    
            actual = actual.siguiente
        return costoTotal

    def algoritmoDST(self,matrizO,costoV,costoI):
        '''
        Conforme recorro la matriz de destino voy comparando la celda de la matriz de destino contra la misma celda de la matriz de Origen, si la celda es distinta entonces en el caso de este algoritmo primero le daré prioridad al nodo de la derecha y luego si este no es igual al color que estoy buscando buscaré en el nodo de abajo y si este tampoco es igual entonces haré un volteo 
        '''
        # ========================= ALGORITMO D - SIN TEXTO ========================== #
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
                if buscarCeldaMODerecha and buscarCeldaMODerecha.Celda.color == actual.Celda.color:
                    #Si la celda a la derecha existe y es del mismo color realizará el intercambio 
                    colorAux = buscarCeldaMO.Celda.color #Almacena el color de la celda Original
                    buscarCeldaMO.Celda.color = buscarCeldaMODerecha.Celda.color
                    buscarCeldaMO.Celda.cambio = True
                    buscarCeldaMODerecha.Celda.color = colorAux
                    costoTotal += costoIntercambio
                else:
                    if buscarCeldaMOAbajo and buscarCeldaMOAbajo.Celda.color == actual.Celda.color:
                        colorAux = buscarCeldaMO.Celda.color 
                        buscarCeldaMO.Celda.color = buscarCeldaMOAbajo.Celda.color
                        buscarCeldaMO.Celda.cambio = True
                        buscarCeldaMOAbajo.Celda.color = colorAux
                        costoTotal += costoIntercambio
                    else:
                        buscarCeldaMO.Celda.color = actual.Celda.color
                        buscarCeldaMO.Celda.cambio = True
                        costoTotal += costoVolteo
                        costoTotal = self.recorrerInversoST(matrizO,costoV,costoI,costoTotal)
            else:
                        buscarCeldaMO.Celda.cambio = True                
            actual = actual.siguiente
        return costoTotal


