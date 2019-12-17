""" Realice una app que lea un numero entero y determine la
    si es un número primo
"""
# Declaración de Variables
result = int
divisible = 0

print("-"*30)
print(" Calculador de primos")
print("-"*30)
# Capturar el num
num = int(input("Ingrese un número: "))
# Proceso
for i in range(1,num + 1):    
    if (num % i == 0):
        divisible = divisible + 1
if divisible == 2: 
    print("Es un número Primo")
else:
    print("No es primo") 
print("-"*30)
espera = input("Presione Enter para salir")
    



