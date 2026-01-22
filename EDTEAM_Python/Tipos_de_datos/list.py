# Arrays, listas

# Colores para la consola
MAGEN = '\033[35m'
GREEN = '\033[32m'
BLUE = '\033[34m'
YELLOW = '\033[33m'
CIAN = '\033[36m'
RED = '\033[31m'
RESET = '\033[0m'

# Inicialización de la lista frutas
frutas = ["Manzana", "Banana", "Cereza", "Durazno"]

# Acceso a elementos
print(f"{GREEN}frutas: {RESET}", frutas)
 # Imprime el element en la posición 2
print(f"{BLUE}Elemento en posición 2: {RESET}", frutas[2])
 # Imprime desde la posición 0 hasta la 3
print(f"{BLUE}Elementos desde la posición 0 hasta la 1: {RESET}", frutas[0:2])
 # Imprime el último elemetnto de la lista
print(f"{BLUE}Último elemento: {RESET}", frutas[-1]) 
# Copia de la lista frutas
frutas2 = frutas.copy()
print(f"{GREEN}Frutas2: {RESET}", frutas2)

# Modificación de la lista
 # Agrega un elemeneto al final de la lista
frutas2.append("Kiwi")
 # Inserta un elemento en la posición 1
frutas2.insert(1, "Naranja")
 # Modifica el elemento de la posición 0
frutas2[0] = "Fresa"

print(f"{YELLOW}frutas2 modificada: {RESET}", frutas2)

# Modificación de conjunto de elementos
frutas2[2:4] = ["Uno", "Dos"]
print(f"{YELLOW}frutas2 modificada: {RESET}", frutas2)

# Concatenacion de listas
new_list = frutas + frutas2
print(f"{MAGEN}Concatenación de listas: {RESET}",new_list)

# Otras operaciones
print(f"{MAGEN}Longitud de la lista new_list: {RESET}", len(new_list))
print(f"{MAGEN}Cantidad de 'Manzana' en new_list: {RESET}", new_list.count("Manzana"))
print(f"{MAGEN}Índice de 'Durazno' en new_list: {RESET}", new_list.index("Durazno"))

# Eliminación de elementos
frutas2.remove("Naranja")
print(f"{RED}frutas2 después de eliminar 'Naranja': {RESET}", frutas2)

# Inicialización de una lista de números
numeros = [1, 2, 3, 4, 5]

# Lista que contiene dos listas, una de frutas y otra de números
new_lista = [frutas, numeros]
print(f"{CIAN}Lista que contiene dos listas: {RESET}", new_lista)
print(f"{GREEN}Lista en indice 0 (frutas): {RESET}", new_lista[0])
print(f"{GREEN}lista en indice 1 (números): {RESET}", new_lista[1])

# Acceso a elementos de las listas anidadas
print(f"{BLUE}Elemento en índice [0][2] (Cereza): {RESET}",new_lista[0][2])



