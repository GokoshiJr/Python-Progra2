"""dado 5 numeros se requiere determinar cuantos son primos y cuantos no, los numeros primos deben ser 
elevados al cubo y los no primos al cuadrado"""
import math
contNoPrimos = contPrimos = 0
for i in range(1,6):
    divisible = 0
    print(" Ingrese el num",i)
    num = int(input(" número:"))
    
    for i in range(1,num + 1):
        if (num % i == 0):
            divisible = divisible + 1
    if (divisible == 2):
        print(" Es un número Primo")
        print(" Condición:",pow(num,3))
        print("-"*30)
        contPrimos = contPrimos + 1
    else:
        print(" No es primo")
        print(" Condición:",pow(num,2))
        print("-"*30)
        contNoPrimos = contNoPrimos + 1 
          
print(" Cantidad de num primos:",contPrimos)
print(" Cantidad de num Noprimos:",contNoPrimos)
print("-"*30)