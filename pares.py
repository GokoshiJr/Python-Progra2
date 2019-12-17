"""app para calcular cuando un numero es par
"""

# Variables
impar = par = 0
estatus = ""
print("-"*30)
print(" Número Par o Impar")
print("-"*30)
num = int(input(" Ingrese un número: "))
print("-"*30)
if (num % 2 == 0) :
    par = par + 1
    estatus = " Es Par"
else:
    impar = impar + 1
    estatus = " Es Impar"
print(" El número ",num, " es",estatus)