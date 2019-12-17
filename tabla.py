"""tabla de multiplicar de un numero"""
# Declaración de Variables
result=int
# Captura del num
print("-"*30)
print(" Tabla de Multiplicar")
print("-"*30)
num = int(input(" Ingrese un número: "))
print("-"*30)
# Proceso
for i in range (1, num+1):
    result = num * i
    print("",num,"*",i,"=",result)
print("-"*30)

