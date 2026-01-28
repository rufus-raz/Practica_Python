import os
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

# SEGUNDA RONDA
# A
frutas = ["manzana", "banana", "cereza", "pera"]
frutas[1] = "kiwi"
frutas.append("naranja")
print(frutas[2])
# B
amigos = ["Axel", "Juan", "Alejandra", "Anahi", "Lilybeth"]
ord_alfabetico = sorted(amigos)
print(ord_alfabetico)
# C
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
pri_3 = numeros[: 3] # pri_3 = numeros[1: 4] 
ult_2 = numeros[-2:] # ult_2 = numeros[-2::]
invertida = numeros[::-1]
print(invertida)
# D
colores = ["rojo", "azul", "verde", "rojo", "amarillo", "azul"]
colores.remove("azul")
n_rojo = colores.count("rojo") # n_rojo = int(colores.count("rojo"))
colores.clear()
print(colores)
# E
edades = [12, 18, 25, 15, 30, 8]
m_8 = [edad for edad in edades if edad >= 18]
# F
palabras = ["python", "es", "genial"]
tranfom = [f"{p.upper()}!" for p in palabras] # [palabra.upper() + "!" for palabra in palabras]
print(tranfom)

# TERCERA RONDA
# 1
letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
cada_dos_letras = letras[::2]
#de_i_a_c_hacia_atras = sorted(letras[-8: -1], reverse = True)
de_i_a_c_hacia_atras = letras[8:1:-1]
ultimos_5_elementos = sorted(letras[-5:], reverse = True)
print(de_i_a_c_hacia_atras)

# 2
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

numero_6 = matriz[1][2]
numero_5_x = matriz.copy()
numero_5_x[1][1] = "x"
diagonal = []
for i in range(3):
    diagonal.append(matriz[i][i])


datos = [5, 12, 3, 20, 7, 15, 2]
Tranformador_binario = [ "ALTO" if valor >= 10 else "BAJO" for valor in datos]

puntajes = [45, 82, 93, 55, 102, 82, 74]
alto = sorted(puntajes, reverse = True)
print(alto[0])
print(alto[1])
print(datos.pop(len(alto)-1))

"""
============================================================
                        El Slicing
============================================================

"""
#*  lista[inicio: fin: paso]
# inico: El indice donde empeizas(incluido)
# fin: El indice donde terminas ( excluido)
# poso(Step): Cuantos elementos saltas y en que direccion
# lista[:: 2] -> "Dame todo, pero de dos en dos"
# lista[::-1] -> "Dame todo, pero con paso -1" (esto invierte la lista)
# lista[5:2:-1] -> Empieza en el 5, terminaantes del 2, caminando hacia atras

#* Si hay listas anidadas, usa copy.deepcopy()


def Palindromo (cadena):
    if cadena:
        if cadena == cadena[::-1]:
            print("Es palindromo")
        else:
            print("No es palindromo")
    else:
        print("No hay que comparar")

original = [[1, 1], [2, 2]]
copia_1 = original.copy() # Apunta al mismo espacio de memoria de el que esta copiando
import copy
copia_2 = copy.deepcopy(original) # Reserva la informacion en otro espacio de memoria diferente al de el original

original[0][0] = 99
print(original)
print(copia_1)
print(copia_2)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# expreciones = [lista[1: len(lista)- 1]]
expreciones = lista[1:-1]
print(expreciones)

numeros = list(range(20)) 

n_impares = [numeros[1::2]]
multipos_de_4 = [numeros[4::4]]
print(multipos_de_4)

#* Codigo optimo
# 1. Palíndromo elegante
def es_palindromo(cadena):
    if not cadena: return "Vacío"
    # Comparamos directamente, devuelve True o False
    return cadena == cadena[::-1]

# 2. Slicing Pro
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
centro = lista[1:-1] # Más limpio que usar len()

# 3. Múltiplos descendentes (El reto del Step)
numeros = list(range(20))
# Saltos de -4 empezando desde el múltiplo más alto
mult_4_desc = numeros[16:0:-4] 
# Resultado: [16, 12, 8, 4]

#* Quinta ronda
inventario = [
    ["Laptop", 1200, 5],
    ["Mouse", 25, 50],
    ["Teclado", 80, 10],
    ["Monitor", 300, 0], # Agotado
    ["USB", 15, 100]
]

stock = [unidades for unidades in inventario if unidades[2] > 0]

for producto in stock:
    producto[1] = producto[1] * .9

producto_caro = [e[0] for e in sorted(stock)]
print(producto_caro[:1])
print(inventario)

#* Forma optima
# 1. Filtrar (Como tú lo hiciste)
stock = [p for p in inventario if p[2] > 0]

# 2. Transformar (Usando f-strings para que se vea bonito)
for p in stock:
    p[1] *= 0.9

# 3. Ordenar por PRECIO (índice 1)
# lambda x: x[1] le dice a sorted que use el precio para comparar
stock_ordenado = sorted(stock, key=lambda x: x[1])

# 4. Extraer el nombre del MÁS CARO (el último de la lista)
mas_caro = stock_ordenado[-1][0]

print(f"El producto con stock más caro es: {mas_caro}")

"""
Simulador de Cola del banco

"""
try:
    fila = ["Luis", "Ramiro", "Eliseo", "Matias"]

    Desicion = True
    while Desicion:
        print("1. Agregar cliente", "2. Atender", "3. Colarse", "4. Estado" , "5. Terminar Jornada", sep= "\n")
        des = int(input(":"))
        os.system('cls')
        match des:
            case 1:
                print("Agregar cliente")
                cliente = input("Ingresa el nombre del cliente: ")
                fila.append(cliente)
            case 2:
                print("Atender cliente")
                if fila:
                    atendido = fila.pop(0)
                    print(f"Atendiendo a {atendido}")
                else:
                    print("No hay nadie en la fila.")
            case 3:
                print("Colarse")
                cliente = input("Ingresa el nombre del cliente: ")
                fila.insert(0, cliente)
            case 4:
                print("Estado")
                print(fila)
            case 5:
                print("Terminar Jornada")
                break
            case _:
                print("Esa opcion no esta en el menu")

        input()
        os.system('cls')
except NameError as e:
    print(f"Ocurrio un error inesperado: {e}")


#* Version refactorizada
import os

fila = ["Luis", "Ramiro", "Eliseo", "Matias"]

while True:
    try:
        print("--- CAJERO AUTOMÁTICO ---")
        print(f"Clientes en espera: {len(fila)}")
        print("1. Agregar cliente\n2. Atender\n3. Colarse (VIP)\n4. Ver Fila\n5. Salir")
        
        opcion = input("Seleccione una opción: ")

        os.system('cls' if os.name == 'nt' else 'clear')

        match opcion:
            case "1":
                nombre = input("Nombre del cliente: ")
                if nombre.strip(): # Evita nombres vacíos
                    fila.append(nombre)
                else:
                    print("Nombre no válido.")
            case "2":
                if fila:
                    print(f"✅ Atendiendo a: {fila.pop(0)}")
                else:
                    print("❌ No hay clientes en la fila.")
            case "3":
                nombre = input("Nombre del cliente VIP: ")
                fila.insert(0, nombre)
                print(f"⚠️ {nombre} se ha colado al principio.")
            case "4":
                print("Fila actual:", " -> ".join(fila) if fila else "Vacía")
            case "5":
                print("Cerrando sistema...")
                break
            case _:
                print("Opción no válida.")
        
        input("\nPresione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')

    except KeyboardInterrupt: # Por si el usuario presiona Ctrl+C
        print("\nSaliendo forzosamente...")
        break