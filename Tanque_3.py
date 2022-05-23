import time

# declaracion de variables
tanque_1 = 500 # El tanque 1 inicia lleno
tanque_2 = 0
linea = '-'*30
modo_llenado_1 = False
modo_llenado_2 = True

# proceso
print(linea)
print('Tanque 1')

while (True):

  print(linea)
  time.sleep(1)

  if (tanque_1 == 500):
    print('El tanque 1 esta lleno')  
  print(f'Tanque 1 capacidad: {tanque_1} l')

  if (modo_llenado_1):
    print(f'Valvula 1 Abierta')
  else:
    print(f'Valvula 1 Cerrada')  

  print('')

  if (tanque_2 == 250):
    print('El tanque 2 esta lleno')  
  print(f'Tanque 2 capacidad: {tanque_2} l')

  if (modo_llenado_2):
    print(f'Valvula 2 Abierta')
  else:
    print(f'Valvula 2 Cerrada')
  

  # El tanque 1 cada segundo consume 50 litros para surtir al tanque 2
  if (tanque_1 and not modo_llenado_1):
    tanque_1 -= 50
  
  # El tanque 2 cada segundo consume 40 litros
  if (tanque_2 and not modo_llenado_2):
    tanque_2 -= 40
  

  # Cuando el tanque llegue a un nivel inferior de 50% debe cerar la valvula 
  # y comenzar a llenarse
  if (tanque_1 < 250):
    modo_llenado_1 = True

  if (tanque_2 < 125):
    modo_llenado_2 = True

  # El tanque 1 se llena a razon de 60 litros por segundo
  if (modo_llenado_1 and tanque_1 != 500):
    tanque_1 += 60
    if (tanque_1 > 500):
      tanque_1 = 500

  # El tanque 2 se llena a razon de 60 litros por segundo
  if (modo_llenado_2 and tanque_2 != 250):
    tanque_2 += 50
    if (tanque_2 > 250):
      tanque_2 = 250

  # Una vez lleno debe abrir la valvula para que permita el consumo del agua
  if (tanque_1 == 500):
    modo_llenado_1 = False
  
  if (tanque_2 == 250):
    modo_llenado_2 = False