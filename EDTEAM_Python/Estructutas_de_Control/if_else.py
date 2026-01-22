# if else

edad_persona = input("Ingresa tu edad: ")
EDAD_BASE = 18

# Condición = True => Bloque de código 1
# Condición = False => Bloque de código 2

if edad_persona >= EDAD_BASE:
    print("Eres mayor de edad")
elif edad_persona == 23:
    print("tienes 23 años")
else:
    print("Eres menor de edad")

