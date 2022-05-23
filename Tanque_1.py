''' 
  Enunciado

  Hacer un programa que calcule la cantida de litros de un tanque diariamente
  hasta cumnplirse 1 semana, partiendo que el tanque esta vacio al inicio de 
  la semana, tomar en cuenta que:

  1. 2 veces al dia se abre la llave por 3 horas para llenar 5 litros de agua
  por hora

  2. El resto del tiempo, cuando el tanque no se esta llenando, se consume a 
  razon de 1/2 litro de agua por hora
'''

import time

# declaracion de variables
semana = 7
salir = False
exit = ''
dia = 1
horas = 0
tanque = 0
linea = '-'*30
modo_llenado = False

# proceso
print(linea)
print('Tanque 1')

while not (salir):

  print(linea)
  time.sleep(0.5)
  print(f'Dia: {dia} Hora: {horas} \nLlenandose: {modo_llenado}')
  print(f'Tanque capacidad: {tanque} l')
  horas += 1

  # 1. 2 veces al dia se abre la llave por 3 horas para llenar 5 litros de agua por hora
  if (horas == 6 or horas == 7 or horas == 8 or horas == 12 or horas == 13 or horas == 14):
    modo_llenado = True
    tanque += 5
  else:
    modo_llenado = False

  if (horas == 24):
    dia += 1
    horas = 0
  
  # 2. el resto del tiempo, cuando el tanque no se esta llenando, se consume a razon de 1/2 litro de agrua por hora
  if (tanque and not modo_llenado):
    tanque -= 0.5

  if (dia == 7 and horas == 1):
    salir = True

print(linea)
print('Fin del programa...')
