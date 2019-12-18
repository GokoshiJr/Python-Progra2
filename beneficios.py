""" Una empresa desea pagar a sus empleados todos los beneficios que se requieren, para lo 
cual desean saber cuánto le van a pagar a cada uno sabiendo que recibe beneficio por su 
instrucción de estudio (secundaria 5%, Técnica 10% y Profesional 20%); además si es casado 
recibirá un adicional del 5%, y si es soltero del 3%. Se debe tener en cuenta que si el sueldo 
excede a los 700 nuevos Bs recibirá una bonificación del 10%. 
Nota: Se debe visualizar todos los montos."""

def menuPrincipal():
    print("-"*30)
    print(" Instrucción de estudio")
    print("-"*30)
    print(" 1) Profesional")
    print(" 2) Técnica")
    print(" 3) Secundaria")
    print(" 4) Salir")
    print("-"*30)
    opc = input(" Ingrese una opción: ")
    return opc

def menuEstado():
    print("-"*30)
    print(" Estado Civil")
    print("-"*30)
    print(" 1) Casado")
    print(" 2) Soltero")    
    print("-"*30)
    opc2 = input(" Ingrese una opción: ")
    return opc2

def sueldoMenu():
    print("-"*30)    
    sueldo = int(input(" Ingrese su sueldo: "))
    return sueldo

def profesional():
    opc2 = menuEstado()
    sueldo = sueldoMenu()
    if (sueldo > 700):
        if (opc2 == "1"):
            bono = (sueldo * 35 / 100)
        elif (opc2 == "2"):
            bono = (sueldo * 33 / 100)   
    elif (sueldo <= 700):
        if (opc2 == "1"): 
            bono = (sueldo * 25 / 100)
        elif (opc2 == "2"): 
            bono = (sueldo * 23 / 100)
    print("-"*30)
    print(" Su sueldo es:",sueldo)
    print(" Su bono es:",bono)
    print("-"*30)
    print(" Su sueldo total es:",sueldo + bono)
     
def tecnica():
    opc2 = menuEstado()
    sueldo = sueldoMenu()
    if sueldo > 700:
        if (opc2 == "1"):
            bono = (sueldo * 25 / 100)
        elif (opc2 == "2"):
            bono = (sueldo * 23 / 100)
    elif (sueldo <= 700):
        if (opc2 == "1"): 
            bono = (sueldo * 15 / 100)
        elif (opc2 == "2"): 
            bono = (sueldo * 13 / 100)        
    print("-"*30)
    print(" Su sueldo es:",sueldo)
    print(" Su bono es:",bono)
    print("-"*30)
    print(" Su sueldo total es:",sueldo + bono)    
        
def secundaria():
    opc2 = menuEstado()
    sueldo = sueldoMenu()
    if (sueldo > 700):
        if (opc2 == "1"):
            bono = (sueldo * 20 / 100)
        elif (opc2 == "2"):
            bono = (sueldo * 18 / 100)           
    elif (sueldo <= 700):
        if (opc2 == "1"): 
            bono = (sueldo * 10 / 100)
        elif (opc2 == "2"): 
            bono = (sueldo * 8 / 100)
    print("-"*30)
    print(" Su sueldo es:",sueldo)
    print(" Su bono es:",bono)
    print("-"*30)
    print(" Su sueldo total es:",sueldo + bono)

def opciones(opc):
    salir = False
    if (opc == "1"):
        profesional()
    elif (opc == "2"):
        tecnica()
    elif (opc == "3"):
        secundaria()
    elif (opc == "4"):
        salir = True
        print("-"*30)
        print(" Cerrando el programa...")
    else:
        print(" Ingrese una Opción Valida")
    return salir        
      
import os,sys

salir = False
while not salir:
    opc = menuPrincipal()    
    salir = opciones(opc)
    
    