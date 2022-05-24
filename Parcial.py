''' 
Desarrolle un programa que permita agregar, consultar, modificar y eliminar 
usuarios con nombre, cedula, fecha de nacimiento y direccion, la busqueda debe
ser por cedula
'''

class Usuario:
  # constructor
  def __init__(self, cedula, nombre, fecha_nacimiento, direccion):
    self.cedula = cedula
    self.nombre = nombre
    self.fecha_nacimiento = fecha_nacimiento
    self.direccion = direccion
  
  # getters
  def get_cedula(self):
    return self.cedula
  def get_nombre(self):
    return self.nombre
  def get_fecha_nacimiento(self):
    return self.fecha_nacimiento
  def get_direccion(self):
    return self.direccion
  
  # setters
  def set_cedula(self, cedula):
    self.cedula = cedula
  def set_nombre(self, nombre):
    self.nombre = nombre
  def set_fecha_nacimiento(self, fecha_nacimiento):
    self.fecha_nacimiento = fecha_nacimiento
  def set_direccion(self, direccion):
    self.direccion = direccion
  
usuarios_array = []
salir = False
linea = '-'*30
opc = 0

while not (salir):
  pass
