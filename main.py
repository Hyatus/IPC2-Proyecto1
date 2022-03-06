from ListaPiso import *
from cargarData import *
from FuncionTransformar import *

listaP = ListaPiso() 

def menuPrincipal():
    opcion = None
    while(opcion != "4"):
        print("\n███████  MENÚ PRINCIPAL ██████████")
        print("█OPCIONES:                       █")
        print("█1. Cargar Data                  █")
        print("█2. Consulta de Pisos y patrones █")
        print("█3. Operaciones con patrones     █")
        print("█4. Salir                        █")
        print("██████████████████████████████████")
        print(" ")
        opcion = str(input("Ingrese una de las opciones: "))
        print(" ")
        if opcion == "1":
               ruta =  input("Ingrese la ruta del archivo: -> ") 
               listaP.limpiarLista()
               leerXML(ruta,listaP) 
               listaP.ordenarPisos()
        elif opcion == "2":
                listaP.recorrerPisosyPatrones()
        elif opcion == "3":
              OperacionesConPisos()
        elif opcion == "4": 
                print("Saliendo...")
        else:
                print("Ingrese una opción valida! ")
    
    print("HA SALIDO DE LA EJECUCIÓN DEL PROGRAMA CON ÉXITO ")


def OperacionesConPisos():
    opcion = None
    nodoPiso = None
    columnasPiso = 0
    filasPiso = 0
    patronO = None
    PatronD = None
    patronOrigen = None
    patronDestino = None

    while(opcion != "6"):
        print("\n███████   OPERACIONES  ██████████")
        print("█OPCIONES:                       █")
        print("█1. Seleccionar Piso             █")
        print("█2. Seleccionar Patron Origen    █")
        print("█3. Seleccionar Patrón Destino   █")
        print("█4. Transformar Patrón           █")
        print("█   Resolver paso a paso (Texto) █")
        print("█5. Transformar Patrón           █")
        print("█   Resolver paso a paso (Grafo) █")
        print("█6. Regresar a Menú Principal    █")
        print("██████████████████████████████████")
        print(" ")
        opcion = str(input("Ingrese una de las opciones: "))
        print(" ")
        if opcion == "1":
                nombrePiso = input("Coloque el nombre del piso: -> ")
                nodoPiso = listaP.buscarPiso(nombrePiso)
                if nodoPiso:
                        print("\n■ Usted Seleccionó -> "+str(nodoPiso.Piso.nombre))
                        print("■ Patrones disponibles para este piso -> ")
                        nodoPiso.Piso.patrones.recorrerPatrones(nodoPiso.Piso.columnas)
                        columnasPiso = int(nodoPiso.Piso.columnas)
                        filasPiso = int(nodoPiso.Piso.filas)
                else:
                   print("No existe ese piso")
        elif opcion == "2":
                if nodoPiso:
                   patronOrigen = input("Coloque el código del Patrón de Origen: -> ")
                   patronO = str(nodoPiso.Piso.patrones.buscarPatron(patronOrigen))
                   #print(patronO)
                else:
                   print("DEBE ESCOGER UN PISO PRIMERO! ")
        elif opcion == "3":
                if nodoPiso and patronO:
                   patronDestino = input("Coloque el código del Patrón de Destino: -> ")
                   patronD = str(nodoPiso.Piso.patrones.buscarPatron(patronDestino))
                   #print(patronD)
                elif patronO == None:
                   print("AÚN NO HA SELECCIONADO EL PATRÓN DE ORIGEN! ")   
                else:
                   print("DEBE ESCOGER UN PISO PRIMERO")
        elif opcion == "4":
                print("Transformando Patrón")   
                if patronO != None and patronD != None:
                        ejecutarAlgoritmosT(columnasPiso,filasPiso,patronO,patronD,nodoPiso,patronOrigen,patronDestino,texto=True)
                        columnasPiso = 0
                        filasPiso = 0
                        nodoPiso =  None
                else:
                   print("DEBE SELECCIONAR UN PATRON DE ORIGEN Y UNO DE DESTINO")
        elif opcion == "5":
                if patronO != None and patronD != None:
                        ejecutarAlgoritmosT(columnasPiso,filasPiso,patronO,patronD,nodoPiso,patronOrigen,patronDestino,texto=False)
                        columnasPiso = 0
                        filasPiso = 0
                        nodoPiso =  None
                else:
                   print("DEBE SELECCIONAR UN PATRON DE ORIGEN Y UNO DE DESTINO")  
        elif opcion == "6": 
                print("Saliendo...")
                menuPrincipal()
        else:
                print("Ingrese una opción valida! ")

        

def ejecutarAlgoritmosT(columnasPiso,filasPiso,patronO,patronD,nodoPiso,patronOrigen,patronDestino,texto):
    costoA = 0
    costoB = 0
    costoD = 0
    crearMatrizOrigen(columnasPiso,filasPiso,patronO)
    crearMatrizDestino(columnasPiso,filasPiso,patronD)               
    costoA = ejecutarAlgoritmoAST(nodoPiso.Piso.costoVolteo,nodoPiso.Piso.costoIntercambio)
    patronO = None
    patronD = None
    patronO = str(nodoPiso.Piso.patrones.buscarPatron(patronOrigen))
    patronD = str(nodoPiso.Piso.patrones.buscarPatron(patronDestino))
    crearMatrizOrigen(columnasPiso,filasPiso,patronO)
    costoB = ejecutarAlgoritmoBST(nodoPiso.Piso.costoVolteo,nodoPiso.Piso.costoIntercambio)
    patronO = None
    patronD = None
    patronO = str(nodoPiso.Piso.patrones.buscarPatron(patronOrigen))
    patronD = str(nodoPiso.Piso.patrones.buscarPatron(patronDestino))
    crearMatrizOrigen(columnasPiso,filasPiso,patronO)
    costoD = ejecutarAlgoritmoDST(nodoPiso.Piso.costoVolteo,nodoPiso.Piso.costoIntercambio)  
      
    
    menorCosto = 0
    algoritmo = None
    if costoA < costoB and costoA < costoD:
            menorCosto = costoA
            algoritmo = "A"
    else:
        if costoB < costoA and costoB < costoD:
                menorCosto=costoB
                algoritmo = "B"
        else:
                menorCosto = costoD
                algoritmo = "D"

    if costoA == costoB and costoA == costoD:
            menorCosto = costoA
            algoritmo = "A"   
            
    if algoritmo == "A":
            patronO = str(nodoPiso.Piso.patrones.buscarPatron(patronOrigen))
            patronD = str(nodoPiso.Piso.patrones.buscarPatron(patronDestino))
            crearMatrizOrigen(columnasPiso,filasPiso,patronO)
            crearMatrizDestino(columnasPiso,filasPiso,patronD)
            ejecutarAlgoritmoA(texto,columnasPiso,filasPiso)
    if algoritmo == "B":
            patronO = str(nodoPiso.Piso.patrones.buscarPatron(patronOrigen))
            patronD = str(nodoPiso.Piso.patrones.buscarPatron(patronDestino))
            crearMatrizOrigen(columnasPiso,filasPiso,patronO)
            crearMatrizDestino(columnasPiso,filasPiso,patronD)
            ejecutarAlgoritmoB(texto,columnasPiso,filasPiso)
    if algoritmo == "D":
            patronO = str(nodoPiso.Piso.patrones.buscarPatron(patronOrigen))
            patronD = str(nodoPiso.Piso.patrones.buscarPatron(patronDestino))
            crearMatrizOrigen(columnasPiso,filasPiso,patronO)
            crearMatrizDestino(columnasPiso,filasPiso,patronD)
            ejecutarAlgoritmoD(texto,columnasPiso,filasPiso)
    
    print("Menor costo es " + str(menorCosto) + " con el algoritmo " + algoritmo )
    
menuPrincipal()