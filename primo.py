""" Realice una app que lea un numero entero y determine la
    si es un número primo
"""
result = int
print("Calculador de primos")
num = int(input("Ingrese un número: "))
divisible = 0
for i in range(1,num + 1):    
    if (num % i == 0):
        divisible = divisible + 1

if divisible == 2: 
    print("Es un número Primo")
else:
    print("No es primo") 

espera = input("Presione Enter para salir")
    



