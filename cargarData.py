from distutils.errors import LibError
from clasePatron import *
from clasePiso import *
from ListaPiso import *


def leerXML(path,pisos):
    try:
        import xml.etree.ElementTree as ET
        tree = ET.parse(path)
        root = tree.getroot()
        
        for piso in root:
            nombre = piso.attrib['nombre']
            for filas in piso.iter('R'):
                fila = filas.text
            for columnas in piso.iter('C'):
                columna = columnas.text
            for costoxVolteos in piso.iter('F'):
                costoxVolteo = costoxVolteos.text
            for costoxIntercambios in piso.iter('S'):
                costoxIntercambio = costoxIntercambios.text
            pisoAux = Piso(nombre,fila,columna,costoxVolteo,costoxIntercambio)
            pisos.insertarPiso(pisoAux) 
            
            for patrones in piso.iter('patron'):
                #print(patrones.attrib['codigo'],patrones.text)
                buscarPiso = pisos.buscarPiso(nombre)
                patronAux = Patron(patrones.attrib['codigo'],patrones.text)
                buscarPiso.Piso.patrones.insertarPatron(patronAux)
        print("CARGA DE DATOS REALIZADA CON ÉXITO!")
    except:
        print("ERROR AL CARGAR ARCHIVO! ")    