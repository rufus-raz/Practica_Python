# Practica

puntajes = [45, 88, 92, 70, 55, 100, 32]

# Guarda en una nueva lista los puntajes mayores o iguales a 60
Filtrar = [puntaje for puntaje in puntajes if puntaje >= 60 ] 
# Luego ordena esa nueva lista de mayor a menor
Ordenar = sorted(Filtrar, reverse = True) # sorted es una función que ordena una lista sin modificar la original, como parametro recibe una 
# lista y un booleando reverse que indica si se ordena de mayor a menor (True) o de menor a mayor (False)

# Finalmente calcula el promedio de los punajes de la lista ordenada, si la lista no esta vacia
Promedio = sum(Ordenar) / len(Ordenar) if Ordenar else 0

# Segunda Practica

logs = ["ERROR:404", "INFO:200", "ERROR:500", "DEBUG:log", "ERROR:403"]

# Guarda en una nueva lista solo los mensajes que comeienzan con "ERROR"
Errores = [log for log in logs if log.startswith("ERROR")] # startwith es un metodo de string que verifica si una cadena comienza con un prefijo
# especifico

# Luego extrae solo los códigos de error como enteros
# Interpretacion: Se divide cada cadena en dos partes usando ":" como separador y se toma la segunda parte (el código de error)
Enteros = [int(error.split(":")[1]) for error in Errores] # split es un metodo de string que divide una cadena en una lista usando un separador
# especifico

# Finalmente encuentra el código de error máximo, si la lista no esta vacia
Error_maximo = max(Enteros) if Enteros else None # max es una funcion que devuelve el valor maximo de una lista, si la lista esta vacia devuelve
# un None

#* Versión Maestra (todo en un solo paso)
error_maximo = max([int(log.split(":")[1]) for log in logs if log.startswith("ERROR")], default=None)
# Interpretacion: Primero filtra los logs que comienzan con "ERROR", luego extrae los códigos de error como enteros y finalmente encuentra el 
# código de error máximo, devolviendo None si no hay errores.

#*1. El Desempaquetado
log = "ERROR:404"
categoria, codigo = log.split(":") # Desempaqueta la lista resultante de split en dos variables
 
# Controlado los cortes con maxplit
lotg = "ERROR: 404: Archivo no encontrado"
# Solo corta en el primer ":" y deja el resto intacto
tipo, resto = log.split(":", 1) # maxsplit indica el número maximo de divisiones a realizar
# tipo = "ERROR", resto -> "404: Arhivo no encontrado"

#*2. List Comprehension: Más allá de un simple if
#  Solo números que sean pares Y mayores a 10
numeros = [2, 12, 15, 20, 8, 30]
filtrados = [n for n in numeros if n % 2 == 0 and n > 10] # Usando 'and' para combinar condiciones
# filtrados = [n for n in numeros if n % 2 == 0 if n > 10]

# El if - else (Transformación)
# Si el número es >= 60 pner "Aprobado", si no, "Reprobado"
notas = [45, 80, 100]
resultado = ["Aprobado" if n >= 60 else "Reprobado" for n in notas] 
# Interpretación: Recorre cada nota en la lista 'notas' y aplica la condición para asignar "Aprobado" o "Reprobado"

#*3. Funciones que "ven" dentro de la lista: key
logs = ["ERROR:404", "ERROR:500", "ERROR:403"]
# "Dime cuál es el máximo, pero para comprar usa solo lo que está después del :"
error_pro = max(logs, key = lambda  x: int(x.split(":")[1])) # max recibe un parametro key que es una función que se aplica a cada elemento para obtener el valor de comparación
# Interpretación: La función max utiliza una función lambda como clave para comparar los elementos de la lista
# La función lambda toma cada log, lo divide por ":", convierte la segunda parte a entero y usa ese valor para la comparación
print(error_pro) # "ERROR:500" (Te devuelve el elemento completo, no solo el número) 

#* Key
# LIstas de Strings(Cadenas)
#  Por longitud:
frutas = ["pera", "manzana", "uva", "kiwi"]
# El más largo
print(max(frutas, key = len)) # "manzana"

# Ingorando mayúsculas:
nombres = ["ana", "Zulema", "beto"]
print(sorted(nombres, key = str.lower)) # ['ana', 'beto', 'Zulema]
# sorted ordena la lista sin modificar la original, usando str.lower como clave para ignorar mayusculas

# Listas de Tuplas (Datos agrupados)
productos = [("Laptop", 1200), ("Mouse", 25), ("Teclado", 80)]
# Busca el producto más barato (min) usando el precio (índice 1)
barato = min(productos, key = lambda p: p[1])
print(barato) # ("Mouse", 25)
# Ordenar de mayor a menor precio
caros_primero = sorted(productos, key = lambda p: p[1], reverse = True)

# Listas de Diccionarios (El estándar en APIs)
usuarios = [
    {"nombre": "Carlos", "puntos": 50},
    {"nombre": "Elena", "puntos": 95},
    {"nombre": "Mario", "puntos": 10}
]
# Ordenar por puntos
ranking = sorted(usuarios, key = lambda u: u["puntos"])

# #* El nivel Pro: operator.itemgetter
# from operator import intemgetter
# # Cuando trabajas con miles de datos, usar labda pueder un poco más lento. Python ogrece el módulo operator que es más rapido y limpio.
# usuarios = [
#     {"nombre": "Cartos", "puntos": 50},
#     {"nombre": "Elena", "puntos": 95}
# ]

# # Es equivalente al lambda anterior, pero más eficiente
# ganador = max (usuarios, key = intemgetter("puntos"))
# # Interpretación: intemgetter("puntos") crea una función que extrae el valor asociado a la clave "puntos" de cada diccionario
# # intemgetter: Es una función del módulo operator que devuelve una función que puede extraer elementos de objetos indexados como listas o diccionarios

# Practica 1
estudiantes = [
    {"nombre": "Ana", "notas": [8, 9, 7]},           # Promedio: 8.0
    {"nombre": "Juan Gabriel", "notas": [5, 6, 4]},   # Promedio: 5.0
    {"nombre": "Maria", "notas": [10, 10, 9]},       # Promedio: 9.6
    {"nombre": "Luis", "notas": [7, 8, 8]}           # Promedio: 7.6
]

# El mejor promedio
mejor_promedio = max(estudiantes, key = lambda e: sum(e["notas"]) / len(e["notas"]))
# Interpretación: La función max utiliza una función lambda como clave para comparar los promedios de las notas de cada estudiante.
# lambda e: sum(e["notas"])/ len(e["notas"]) calcula el promedio de las notas de cada estudiante.
print(mejor_promedio)
# Nombre más largo
nombre_largo = max(estudiantes, key = lambda e: len(e["nombre"]))
# Interpretación: La función max utiliza una función lambda como clave para comparar la longitud de los nombres de cada estudiante.
# labda e: len(e["nombre"]) obtiene la longitud del nombre de cada estudiante.
print(nombre_largo)
# Ordenar por nota más alta
Exito = sorted(estudiantes, key = lambda e: max(e["notas"]), reverse = True)
# Interpretación: La función sorted ordena la lista de estudiantes utilizando una función lambda como clave para comparar la nota 
# más alta de cada estudiante.
# lambda e: max(e["notas"]) obtiene la nota más alta de cada estudiante.
print(Exito)
# Versión con "List Comprehension" (Solo si quieres extraer los nombres):
nombres_exito = [e["nombre"] for e in sorted(estudiantes, key=lambda e: max(e["notas"]), reverse=True)]
# Resultado: ['Maria', 'Ana', 'Luis', 'Juan Gabriel']

#* Filtrado
# Creando el "Cuadro de Honor"
cuadro_honor = [ e for e in estudiantes if sum(e["notas"]) / len(e["notas"]) >= 9]
print("Estuidiantes en el Cuadro de Honor:")
for est in cuadro_honor:
    print(est["nombre"])
# Creando la lista de "Recuperación"
recuperacion = [ e for e in estudiantes if sum(e["notas"]) / len(e["notas"]) < 6]
print(" Estudiantes en Recuperación:")
for est in recuperacion:
    print(est["nombre"])
# combiinando todo
# 1. Filtramos y obtenemos la lista
honor = [e for e in estudiantes if sum(e["notas"]) / len(e["notas"]) >= 9]
# 2. Ordenamos el resultado
honor_ordenado = sorted(honor, key = lambda e : sum(e["notas"]) / len(e["notas"]), reverse = True)
print("Cuadro de Honor Ordenado:")
for est in honor_ordenado:
    print(est["nombre"])

nombre_largo = [e["nombre"] for e in sorted(estudiantes,key = lambda e: len(e["nombre"]), reverse = True) if len(e["nombre"]) >= 5]
# Interpretación: Primero ordena los estudiantes por la longitud de su nombre en orden descendente
# Luego filtra los nombres que tienen 5 o más caracteres y crea una lista con esos nombres.
""" El orden de los factores sí altera el rendimiento:"""
# Es más eficiente filtrar primero y luego ordenar, especialmente con listas grandes
filtrados = [e for e in estudiantes if len(e["nombre"]) >= 5]
nombre_largo = [e["nombre"] for e in sorted(filtrados, key = lambda e: len(e["nombre"]), reverse = True)]

#* Transformación(Mapping)
etiquetas = [f"Alumno: {e['nombre']} - Promedio: {sum(e['notas']) / len(e['notas']):.1}" for e in estudiantes ]
# Interpretación: Imprimimos un mensaje que integra en una lista al alumno y su promedio

# Filtrado
filtro = [e for e in estudiantes if sum(e["notas"]) / len(e["notas"]) >= 7]
Ordenamineto = sorted(filtro, key = lambda e : sum(e["notas"]) / len(e["notas"]), reverse = True)
Transformacion = [f"CERTIFICADO: {e['nombre']} | Calificación Final: {sum(e['notas']) / len(e['notas']):.1f}" for e in Ordenamineto]
print(Transformacion)

# Tu lógica impecable (con el ajuste de comillas):
filtro = [e for e in estudiantes if sum(e["notas"]) / len(e["notas"]) >= 7]

Ordenamineto = sorted(filtro, key = lambda e : sum(e["notas"]) / len(e["notas"]), reverse = True)

Transformacion = [f"CERTIFICADO: {e['nombre']} | Calificación Final: {sum(e['notas']) / len(e['notas']):.1f}" for e in Ordenamineto]

# Lo imprimimos bonito
for certificado in Transformacion:
    print(certificado)