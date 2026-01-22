# Tipos de datos

# Formas de convencionar nombres:
# Camel Case => MiNombreCompleto
# Snake Case => mi_nombre_completo
# Pascal Case => miNombreCompleto

VarName = "PascalCase"
varName = "camelCase"
var_name = "snake_case"



# NÚMERICOS
#Tipos:
# int (entero) => 10, 200, 1000, -300
# float (punto flotante - decimales) => 2.1, -4.5, -500.4
# complex (complejo) => 2 +1j, 1

n1 = 10 # Entero
n2 = 2.4 # Punto flotante
n3 = 3 + 2j # Complejo
millon = -1e6 # Notación científica

print(type(n1))
print(type(n2))
print(type(n3))
print(type(millon))

#STRINGS
# Tipos:
# str (cadenas de texto) => "Hola", 'Mundo', """EDteam"""

name = """Texto para hacer pruebas
con múltipes líneas 'str'
con las cadenas de texto"""
print(name)
name ="EDteam"
print(name[3]) # Imprime la letra que esta en la posición 3

# BOOLEANOS
# Tipos:
# bool (booleanos) => True, False

contenido = 1
print(bool(contenido))