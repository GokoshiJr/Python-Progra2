"""calcular el factorial de un numero
"""
# Declaración de Variables
num = 0
factorial = 1
print("-"*30)
print(" Factorial de un Número")
print("-"*30)
num = int(input(" Ingrese un número: ")) # Capturamos el num
# Proceso
for i in range (1,num+1):
    factorial = factorial * i
print(" El factorial es:",factorial)
print("-"*30)
espera = input("Presione Enter para salir")

