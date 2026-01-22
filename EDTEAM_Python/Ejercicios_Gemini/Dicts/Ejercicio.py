# Ejercicios

"""
1. El Perfil de Usuarios
Crea un programa que haga lo siguiente:
- Define un diccionario vacío llamado usuario.
- Pide al ususario ( por tecado con input()) su nombre, edad y país.
- Agrega esos datos al diccionario con las claves "nombre", "edad" y "pais"
- finalmente, imprime un mensaje que diga: "Hola[nombre], veo que tienes [edad] 
años y vivies en [pais] "accediendo a los valores del diccionario.

"""

# usuario = {}

# nombre = input("Ingresa tu nombre: ")
# edad = input("Ingresa tu edad: ")
# pais = input("Ingresa tu pais: ")

# usuario = {
#     "nombre": nombre,
#     "edad": edad,
#     "pais": pais
#     }

# print(f"Hola {usuario.get("nombre")}, veo que tienes {usuario.get("edad")} años y vivies en {usuario.get("pais")} ")

"""
2. Buscador de Precios (Control de Errores)
Tienes el siguiete catálogo de una cafetería:
- Escribe un programa que: Pida al usuario el nombre de un producto.
- Usa una estructura if - else para veificar si el producto existe en el diccionario.
- Si existe: Imprime el precio. 
- Si no existe: Imprime "Lo sentimos, no tenemos ese producto en el menú".

"""

# menu = {"cafe": 1.5, "te": 1.2, "tostada": 2.0, "zumo": 2.5}

# name_product = input("Ingresa el nombre del producto: ")

# for producto in menu :
#     if producto == name_product:
#         print(f"el precio de {name_product} es : {menu.get(producto)}") 
#         break
# else:
#         print("Lo sentimos, no tenemos ese producto en el menú")

# Opcion Optima
# if name_product in menu:
#     print(f"El precio de {name_product} es: {menu[name_product]}")
# else:
#     print("Lo sentimos, no tenemos ese producto.")

"""
3. El Filtro de Edades
Dado el siguiente diccionario de personas y sus edades:
Crea un script qu erecorra el diccionario (usando un bucle for) e implima solo los nombres
de las personas que son mayores de edad (18 años o más).

"""

# personas = {"Juan": 15, "Elena": 22, "Marcos": 17, "Lucia": 30, "Ricardo": 12}

# mayores = [ user for user, edad in personas.items() if edad >= 18]

# print("Las personas mayores de edad son: ", mayores)

"""
4. contador de Caractere
Pide al usuario qu eintroduzca una palabra. Tu programa debe crear un diccionario donde:
- La clave sea cada letra de la palabra.
- El valor sea el número de veces que aparece esa letra.
Ejemplo: Si el ususario escribe "casa", el resultado debería ser {"c": 1, "a": 2, "s": 1}.

"""

# palabra = input("Ingresa una palabra: ")
# contador = {}
# cont = 0
# for letra in palabra:
#     cont += 1
# print("contador: ", contador)

# Opción Optima
# for letra in palabra:
#     # Si no existe, devuelve 0 y le suma 1. Si existe, trae el valor y suma 1.
#     contador[letra] = contador.get(letra, 0) + 1

# print("Resultado:", contador)

"""
==============================================================
                        SEGUNDA PARTE
==============================================================

"""

"""
1. Contador de Frecuencia de Palabras
Escribe un programa que pida al usuario una frase y devuelva un diccionario donde las 
claves sean las palabras y los valores sean la cantidad de veces que esa palabra aparece 
en la frase.
    Pista: Usa el método .split() para separar la frase en una lista de palabras.
    Condición: Ignora si las palabras están en mayúsculas o minúsculas (trátalas todas 
    como minúsculas).

"""
# print("Ingresa una frase: ")
# frase = input()
# # Lower devuelve una lista
# frase = frase.lower()
# palabras = frase.split()

# contador = {}

# for palabra in palabras:
#     if palabra in contador:
#         contador[palabra] += 1
#     else:
#         contador[palabra] = 1
# # Solucion Optima
# # for palabra in palabras:
# #     contador[palabra] = contador.get(palabra, 0) + 1

# print(contador)


"""
2. Gestión de Inventario

Imagina que tienes el inventario de una tienda en un diccionario:
 productos = {"manzanas": 50, "peras": 20, "naranjas": 35}

Crea un programa que:
    Pregunte al usuario qué producto desea comprar.
    Pregunte cuántas unidades necesita.
    Si hay suficiente stock, descuenta la cantidad del diccionario y muestra el nuevo total.
    Si no hay suficiente stock, muestra un mensaje de error indicando cuánto hay disponible.
    Si el producto no existe, informa al usuario.

"""

# productos = {"manzanas": 50, "peras": 20, "naranjas": 35}

# print("Ingresa el producto que deseas comprar: ")
# producto = input()
# # Evalua si el producto se encuentra en el diccionario
# if producto in productos:

#     print("Ingresa la cantidad que deseas comprar: ")
#     unidades = int(input())

#     # Evalua si las unidades alcanzan a la demanda
#     if unidades <= productos.get(producto):

#         productos.update({producto: productos.get(producto) - unidades})
#         print("Sobran: ", productos.get(producto))

#     else:
#         print("El producto no da abasto para su pedido, tenemos en existencia: ", productos.get(producto))
# else:
#     print("El pronucto no se encuentra")

# # Solucion Optima
# if producto in productos:
#     unidades = int(input("Cantidad: "))
#     if unidades <= productos[producto]:
#         productos[producto] -= unidades # Resta directa
#         print(f"Venta exitosa. Quedan: {productos[producto]}")
#     else:
#         print(f"No hay abasto. Solo hay: {productos[producto]}")
"""
3. Clasificación de Calificaciones

Tienes un diccionario con los nombres de varios estudiantes y una lista de sus notas:
 estudiantes = {"Ana": [8, 9, 7], "Luis": [5, 4, 6], "Marta": [10, 10, 9]}

Escribe un script que genere un nuevo diccionario que contenga el nombre del estudiante como
 clave y su promedio de notas como valor. Además, el programa debe imprimir quién es el 
 estudiante con el promedio más alto.

"""

# estudiantes = {"Ana": [8, 9, 7], "Luis": [5, 4, 6], "Marta": [10, 10, 9]}
# voleta = {}
# for nombre in estudiantes:  
#     promedio = 0
#     for calificacion in estudiantes.get(nombre):

#         promedio += calificacion

#     voleta[nombre] = promedio

# print(voleta)

# p_mas_alto = ""
# for alumno in voleta:
#     if alumno > p_mas_alto:
#         p_mas_alto = alumno

# print("El alumno con el promedio más alto es: ", p_mas_alto)

# # Solucion Optima
# estudiantes = {"Ana": [8, 9, 7], "Luis": [5, 4, 6], "Marta": [10, 10, 9]}
# boleta = {}

# for nombre, notas in estudiantes.items():
#     # Usamos sum() y len() para promedios rápidos
#     boleta[nombre] = sum(notas) / len(notas)

# # Para el máximo, comparamos los valores de la boleta
# mejor_estudiante = max(boleta, key=boleta.get) 

# print(boleta)
# print(f"El mejor es {mejor_estudiante} con {boleta[mejor_estudiante]}")

"""
Nivel 3: El reto de "Agrupar" (Lógica de Contador Avanzada)
Este es el nivel "Final Boss" basado en lo que te costó del ejercicio 4. En lugar de contar 
letras, vamos a clasificar objetos.
El Escenario: Tienes una lista de productos con su categoría, pero están todos mezclados:
productos = [
    {"nombre": "Manzana", "cat": "Fruta"},
    {"nombre": "Lechuga", "cat": "Verdura"},
    {"nombre": "Plátano", "cat": "Fruta"},
    {"nombre": "Zanahoria", "cat": "Verdura"},
    {"nombre": "Naranja", "cat": "Fruta"}
]
Tu reto: Crea un programa que genere un nuevo diccionario donde las claves sean las 
categorías y los valores sean listas con los nombres de los productos.

Resultado esperado: 
{"Fruta": ["Manzana", "Plátano", "Naranja"], "Verdura": ["Lechuga", "Zanahoria"]}

    Pista para el Nivel 3: Es igual que el contador de letras. Si la categoría no está en tu
    diccionario nuevo, créala con una lista que contenga el primer 
    nombre: mi_dict[categoria] = [nombre]. Si ya está, usa .append() para agregar el nombre 
    a la lista existente.

"""
# productos = [
#     {"nombre": "Manzana", "cat": "Fruta"},
#     {"nombre": "Lechuga", "cat": "Verdura"},
#     {"nombre": "Plátano", "cat": "Fruta"},
#     {"nombre": "Zanahoria", "cat": "Verdura"},
#     {"nombre": "Naranja", "cat": "Fruta"}
# ]

# productos_update = {}
# # Recorremos las listas
# for articulo in productos:

    
#     if articulo.get("cat") in productos_update:

#         productos_update[articulo.get("cat")].append(articulo.get("nombre"))

#     else:

#         productos_update[articulo.get("cat")] = [articulo.get("nombre")]

# for articulo in productos:
#     categoria = articulo.get("cat")
#     nombre = articulo.get("nombre")
    
#     if categoria in productos_update:
#         # Accedemos a la lista existente y añadimos el nombre
#         productos_update[categoria].append(nombre)
#     else:
#         # Creamos una lista nueva con el primer nombre
#         productos_update[categoria] = [nombre]

# # Solucion Optima 
# for articulo in productos:
#     cat = articulo["cat"]
#     nombre = articulo["nombre"]
    
#     if cat not in productos_update:
#         productos_update[cat] = [] # Creamos lista vacía
    
#     productos_update[cat].append(nombre) # Añadimos siempre

# print(productos_update)

"""
==============================================================
                        TERCERA PARTE
==============================================================

"""


"""
1. El Limpiador de Datos (Normalización)
A veces recibes datos de usuarios que escriben mal ( con espacios extra o mayúculas locas.)
El Escenario: Tienes un diccionario de correos electrónicos, pero están "sucios".

Tu reto: Crea un nuevo diccionario llamado correos_limpios donde:
 - Las claves (correos) esten todas en minúsculas y sin espacios alos lados.
 - Los valores (nombres) tengan slolo la primera letra en mayúscula y sin espacios.
 - Resultado esperado: { "juand@gmail.com" : "Juan", ... }

"""
correos_sucios = {
    "juan@Gmail.com ": "JUAN",
    " marta@outlook.com" : "marta",
    "LUIS@GMAIL.COM" : "Luis"
}

# correos_limpios = {clave.lower(): valor.lower() for clave, valor in correos_sucios.items()}
# for clave, valor in correos_sucios.items():
#     if " " in clave:

