"""
    Escribe un programa que pida al usuario una frase y devuelva un diccionario donde las claves sean las 
    palabras y los valores sean la cantidad de veces que esa palabra aparece en la frase.

    Pista: Usa el método .split() para separar la frase en una lista de palabras.

    Condición: Ignora si las palabras están en mayúsculas o minúsculas (trátalas todas como minúsculas)."""

# Variables

frase = input("Ingresa una frase: ")
frase = frase.lower()
palabras = frase.split()


contador = {}

for palabra in palabras:

    if palabra not in contador:
        contador[palabra] = 0
    contador[palabra]+= 1

print(contador)