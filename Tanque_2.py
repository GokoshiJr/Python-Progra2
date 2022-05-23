''' 
Enunciado

Realizar un programa que simule el consumo de un tanque de agua de 250 litros, 
tomando en cuenta las siguientes premisas:

1. El tanque inicia lleno
2. Cada segundo consume 40 litros
3. Cuando el tanque llegue a un nivel inferior de 50% debe cerar la valvula 
y comenzar a llenarse
4. El tanque se llena a razon de 35 litros por segundo
5. Una vez lleno debe abrir la valvula para que permita el consumo del agua

Cada segundo debe reportar la cantidad de agua en el tanque e informar 
cuando cierra y abre la valvula
'''

import time

# declaracion de variables
tanque = 250 # 1. El tanque inicia lleno
linea = '-'*30
modo_llenado = False

# proceso
print(linea)
print('Tanque 1')

while (True):

  print(linea)
  time.sleep(1)

  if (tanque == 250):
    print('El tanque esta lleno')  
  print(f'Tanque capacidad: {tanque} l')
  if (modo_llenado):
    print(f'Valvula Abierta')
  else:
    print(f'Valvula Cerrada')  

  # 2. Cada segundo consume 40 litros
  if (tanque and not modo_llenado):
    tanque -= 40

  # 3. Cuando el tanque llegue a un nivel inferior de 50% debe cerar la valvula 
  # y comenzar a llenarse
  if (tanque < 125):
    modo_llenado = True

  # 4. El tanque se llena a razon de 35 litros por segundo
  if (modo_llenado and tanque != 250):
    tanque += 35
    if (tanque > 250):
      tanque = 250

  # 5. Una vez lleno debe abrir la valvula para que permita el consumo del agua
  if (tanque == 250):
    modo_llenado = False
