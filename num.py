""" Realice una app que lea un numero entero y determine la
    suma de sus digitos y su valor espejo, cada digito
    obtenido de ser mostrado por la consola
"""

# Inicializar Variables
num = temp = 0
dig = suma = espejo = 0
# Entrada de Datos
num = int(input("Ingrese un número: "))
# Proceso
temp = num
print(" ")
print("Digitos Obtenidos")
while temp != 0:
    dig = temp % 10 # Obtenemos un digito
    print(dig)      # Lo mostramos por consola
    suma += dig     # Lo acumulamos en suma
    espejo = espejo * 10 + dig # Constuimos el espejo
    temp = temp // 10 # Obtenemos el nuevo número
print(" ")
print("La suma de los digitos de: ",num," es: ", suma)
print("El espejo es: ", espejo)
print("Fin del programa")

