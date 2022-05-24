''' 
Desarrolle un programa que permita agregar, consultar, modificar y eliminar 
usuarios con nombre, cedula, fecha de nacimiento y direccion, la busqueda debe
ser por cedula
'''

from multiprocessing.managers import ValueProxy
from unittest import expectedFailure


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
  try:
    print(linea)
    print(' CRUD de Usuarios')
    print(linea)
    print(' 1. Listar todos los usuarios')
    print(' 2. Agregar usuario')
    print(' 3. Consultar usuario')
    print(' 4. Actualizar usuario')
    print(' 5. Eliminar usuario')
    print(' 6. Salir del programa')
    print(linea)
    opc = int(input(' Seleccione una opcion: '))
    print(linea)
    if (opc == 1):
      pass
    elif (opc == 2):
      pass
    elif (opc == 3):
      pass
    elif (opc == 4):
      pass
    elif (opc == 5):
      pass
    elif (opc == 6):
      pass
    else:
      print(' Error: Ingrese una opcion valida.')    
  except ValueError:
    print(linea)
    print(' Error: solo se permite ingresar numeros enteros.')
  except TypeError:
    print(linea)
    print(' Error: solo se permite ingresar numeros enteros.')  

