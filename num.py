""" Realice una app que lea un numero entero y determine la
    suma de sus digitos y su valor espejo, cada digito
    obtenido de ser mostrado por la consola
"""

# Inicializar Variables
num = temp = 0
dig = suma = espejo = 0
# Entrada de Datos
print("-"*30)
print(" Número Espejo")
print("-"*30)
num = int(input(" Ingrese un número: "))
# Proceso
temp = num
print("-"*30)
print(" Digitos Obtenidos:")
while temp != 0:
    dig = temp % 10 # Obtenemos un digito
    print(" ",dig)      # Lo mostramos por consola
    suma += dig     # Lo acumulamos en suma
    espejo = espejo * 10 + dig # Constuimos el espejo
    temp = temp // 10 # Obtenemos el nuevo número
print("-"*30)
print(" Suma de Digitos de: ",num," es: ", suma)
print(" El espejo es: ", espejo)
print("-"*30)
print(" Fin del programa")

