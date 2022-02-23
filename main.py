from ListaPiso import *

def menuPrincipal():
    opcion = 0
    while(opcion != 5):
        print("\n███████ MENÚ PRINCIPAL ██████████")
        print("█OPCIONES:                       █")
        print("█1. Cargar Data                  █")
        print("█2. Consulta de Pisos y patrones █")
        print("█3. Operaciones con patrones     █")
        print("█4. Generar Reportes             █")
        print("█5. Salir                        █")
        print("██████████████████████████████████")
        print(" ")
        opcion = int(input("Ingrese una de las opciones: "))
        print(" ")
        if opcion == 1:
               print("DATOS CARGADOS CON ÉXITO! ")
        elif opcion == 2:
                print("CARGA DE INSTRUCCIONES REALIZADA CON ÉXITO! ")
        elif opcion == 3:
                print("Análisis de Datos")
        elif opcion == 4:
                print("Generando Reporte...")   
        elif opcion == 5: 
                print("Saliendo...")
        else:
                print("Ingrese una opción valida! ")
    
    print("HA SALIDO DE LA EJECUCIÓN DEL PROGRAMA CON ÉXITO ")





