from ListaPatron import *

class Piso: 
  def __init__(self,nombre,filas,columnas,costoVolteo,costoIntercambio) -> None:
    self.nombre = nombre
    self.filas = filas 
    self.columnas = columnas
    self.costoVolteo = costoVolteo
    self.costoIntercambio = costoIntercambio
    self.patrones = ListaPatron()