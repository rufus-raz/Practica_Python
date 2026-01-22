# Ejercicio

"""
Imagina que tienes la siguiente lista que representa las temperaturas registradas
en una semana:

"""
temperaturas = [18, 22, 15, 30 , 27, 12, 35]

fin_de_semana = temperaturas[-2:]
# fin_de_semana = temperaturas[::-1][:2]
print("1. = ", fin_de_semana)

color = [x for x in temperaturas if x > 25]
print("2. = ", color)

farengeit = [((x * 9/5)+ 32) for x in temperaturas ]
print("3. = ",farengeit)


"""
Tienes una lista de productos en un almacén. Algunos están agotados (tienen valor 0).
- Misión A: Usa remove() o cuna comprensión de listas para crear un anueva lista llamada 
disponibles que lemine todos los ceros
- Misión B: Ordena la lista disponibles de mayor a menor.

"""
inventario = [15, 0 , 8, 42, 0, 12, 7, 0]

# disponibles = inventario.copy()
# for producto in disponibles:
#     if producto == 0:
#         disponibles.remove(producto)

# disponibles.sort(reverse= True)
# print(disponibles)

disponibles = [art for art in inventario if art != 0]
disponibles.sort(reverse = True)
print("Disponibles: ", disponibles)

"""
Las listas no solo son de números. Imagina que tienes una lista de correos electrónicos:
- Misión: Usa una List Comprehension y el método .split("@") para crear una lista que solo 
contenga los dominios (ejemplo: ["gmail.com", "hotmail.com", ...]).

"""
emails = ["juanq@gmail.com", "ana@hotmail.com", "pedro@yahoo.com", "luis@gmail.com"]

# dominios = [email.split("@") for email in emails ]
# print(dominios)

dominios = [correo.split("@")[1] for correo in emails]
print("Doninios: ", dominios)

"""
Este es el formato que verás en bases de datos reales. Tines una lista de diccionarios:
- Misión: Crea una lita llamada pro_players que contenga solo los nombres de los usuarios
que tengan más de 50 puntos

"""

usuarios = [
    {"nombre": "Alice", "puntos": 45},
    {"nombre": "Bob", "puntos": 78},
    {"nombre": "Charlie", "puntos": 12},
    {"nombre": "Diana", "puntos": 90}
]
pro_players = [user["nombre"] for user in usuarios if user["puntos"] > 50]
print("Pro Players: ", pro_players)