
#* Listas

#* Inicialización
lista = ["valor 1", "valor 2", "valor 3", "valor 4"]

#* Métodos
# Agregar elemetos
# - append( elemento): Agrega un solo elemto al final de la lista.
# - insert( índice, elemento): Inseta un elemetno en una posición especidica. Los elementos
# a la derecha se desplazan.
# - extend( iterable): Agrega todos los elementos de otro conjunto (como otra lista) al 
# al final de al actual.

# Eliminar elementos
# - remove(valor): Busca la primer aparición de valor espesificado y la elimina. Si no
# exicte, lanza un error.
# - pop(indice): Elimina el elemento en la posición indicada y te lo devuelve (por si 
# quieres usarlo). Si no pones índice, elimina el último.
# - clear(): Elimina todos los elemetnos, dejando la lista vacía[].

# Orden y búsqueda
# - sort(): Ordena la lista de forma ascendente (o alfabética) permanentemente. Puedes
# usar reverse = True para orden descendente.
# - reverse(): Invierte el orden de los elemento tal como están.
# - index(valor): Devuelve la posición (índice) de la primera vez que aparece ese valor.
# - count(valor): Cuenta cuántas veces se repite un elemento en la lista.

#* Funciones integradas (Built - in)
# - len(lista): Devuelve la cantidad total de elmentos (longitud).
# - max(lista): Devuelve el valor más grande.
# - min(lista): Devuelve el valor más pequeño
# - sum(lista): Suma todos los elementos (si son numéricos).
# - sorted(lista): Devuelve una copia ordenada de la lista sin modificar la original.

frutas = ["manzana", "pera"]
frutas.append("naranja")        # [",anzana", "pera", "naranja"]
frutas.insert(1, "uva")         # ["manzana", "uva", "pera", "naranja"]
frutas.sort()                   # ["manzana", "naranja", "pera", "uva"]

print(len(frutas))              # Salida: 4

"""
1. Slicing (Rebanado)
El slicing te permite obtener una subsección de la lista sin moidficar la original. La 
sintaxis básica es: lista[inicio:fin:paso].
- inicio: El índice donde empieza la rabanada (incluido).
- fin: El índice donde termina (no incluido).
- paso: Cuántos elementos saltar (por defecto es 1).

"""
#* Ejemplos
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8 , 9]
# Extraer del índice 2 al 5
print(numeros[2:6])         # Resultado: [2, 3, 4, 5]
# Extraer desde el inicio hasta el 3
print(numeros[:4])          # Resultado: [0, 1, 2, 3]
# Extraer cada dos números (paso 2)
print(numeros[::2])         # Resultado: [0, 2, 4, 6, 8]
# Invertir la ista completa (truco clásico)
print(numeros[::-1])        # Resultado: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

"""
2. List Comprehensions (Comprensión de lista)
Es ua forma muy compacta de crear una lista aplicando una operación a cada elemento de una
lista existente. Es mucho más rápido y limpio que usar un blucle for tradicional
La estructura es: [nueva_espresion for elemento in lista_original if condicion]

"""
# forma tradicional (4 lineas)
cuadrados = []
for x in range(5):
    cuadrados.append(x**2)
# Resultado: [0, 1, 4, 9, 16]

# Con List Comprehension (1 linea)
cuadrados = [x**2 for x in range(5)]
# Resultado: [0, 1, 4, 9, 16]

#* Agregando un filtro (if)
pares = [x for x in range(10) if x % 2 == 0]
# Resultado: [0, 2, 4, 6, 8]