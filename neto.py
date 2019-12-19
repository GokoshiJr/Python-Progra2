"""El sueldo neto de un trabajador se calcula con la suma del sueldo básico más el 12% del 
monto total de ventas hechas. Diseñar un programa por consola que determine el sueldo neto 
de un vendedor sabiendo que hizo tres ventas durante el mes.
"""
def menuOpc():
    print("-"*30)
    print(" Sueldo Neto")
    print("-"*30)
    print(" 1) Calcular")
    print(" 2) Salir")
    print("-"*30)
    opc = input(" Ingrese un Opción: ")
    return opc

def menuPrincipal():
    print("-"*30)    
    sueldo = int(input(" Ingrese el sueldo básico:"))
    print("-"*30)
    return sueldo

def menuVentas():
    acum = 0
    for i in range (1,4):
        print(" Ingrese la venta",i)
        venta = int(input(" Ganancia:"))
        print("-"*30)
        acum =acum + venta
    aux = acum*12/100
    return aux  

def Calcular():
    sueldo = menuPrincipal()
    aux = menuVentas()
    print(" Su sueldo es:",sueldo)
    print(" El 12% de las ventas:",aux)
    print("-"*30)
    print(" Su sueldo neto es:", sueldo + aux)

def opciones(opc):
    salir = False
    if (opc == "1"):
        Calcular()    
    elif (opc == "2"):
        salir = True
        print("-"*30)
        print(" Cerrando el programa...")
    else:
        print(" Ingrese una Opción Valida")
    return salir
 
salir = False
while not salir:
    opc = menuOpc()    
    salir = opciones(opc)

