from ListaPiso import *
from cargarData import *
from FuncionTransformar import *

listaP = ListaPiso() 

def menuPrincipal():
    opcion = None
    while(opcion != "5"):
        print("\n███████  MENÚ PRINCIPAL ██████████")
        print("█OPCIONES:                       █")
        print("█1. Cargar Data                  █")
        print("█2. Consulta de Pisos y patrones █")
        print("█3. Operaciones con patrones     █")
        print("█4. Generar Reportes             █")
        print("█5. Salir                        █")
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
                print("Generando Reporte...")   
        elif opcion == "5": 
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
    while(opcion != "5"):
        print("\n███████   OPERACIONES  ██████████")
        print("█OPCIONES:                       █")
        print("█1. Seleccionar Piso             █")
        print("█2. Seleccionar Patron Origen    █")
        print("█3. Seleccionar Patrón Destino   █")
        print("█4. Transformar Patrón           █")
        print("█5. Regresar a Menú Principal    █")
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
                   print(patronO)
                else:
                   print("DEBE ESCOGER UN PISO PRIMERO! ")
        elif opcion == "3":
                if nodoPiso and patronO:
                   patronDestino = input("Coloque el código del Patrón de Destino: -> ")
                   patronD = str(nodoPiso.Piso.patrones.buscarPatron(patronDestino))
                   print(patronD)
                elif patronO == None:
                   print("AÚN NO HA SELECCIONADO EL PATRÓN DE ORIGEN! ")   
                else:
                   print("DEBE ESCOGER UN PISO PRIMERO")
        elif opcion == "4":
                print("Transformando Patrón")   
                if patronO != None and patronD != None:
                   crearMatrizOrigen(columnasPiso,filasPiso,patronO)
                   crearMatrizDestino(columnasPiso,filasPiso,patronD)
                   ejecutarAlgoritmoA(nodoPiso.Piso.costoVolteo,nodoPiso.Piso.costoIntercambio)
                   patronO = None
                   patronD = None
                   patronO = str(nodoPiso.Piso.patrones.buscarPatron(patronOrigen))
                   patronD = str(nodoPiso.Piso.patrones.buscarPatron(patronDestino))
                   print("PATRÓN DE ORIGEN " + patronO)
                   print("PATRON DE DESTINO " + patronD)
                   crearMatrizOrigen(columnasPiso,filasPiso,patronO)
                   ejecutarAlgoritmoB(nodoPiso.Piso.costoVolteo,nodoPiso.Piso.costoIntercambio)
                   patronO = None
                   patronD = None
                   patronO = str(nodoPiso.Piso.patrones.buscarPatron(patronOrigen))
                   patronD = str(nodoPiso.Piso.patrones.buscarPatron(patronDestino))
                   print("PATRÓN DE ORIGEN " + patronO)
                   print("PATRON DE DESTINO " + patronD)
                   crearMatrizOrigen(columnasPiso,filasPiso,patronO)
                   ejecutarAlgoritmoD(nodoPiso.Piso.costoVolteo,nodoPiso.Piso.costoIntercambio)
                else:
                   print("DEBE SELECCIONAR UN PATRON DE ORIGEN Y UNO DE DESTINO")
        elif opcion == "5": 
                print("Saliendo...")
                menuPrincipal()
        else:
                print("Ingrese una opción valida! ")

        



menuPrincipal()


