# Strings

"""
        CARACTERISTICAS PRINCIPALES
- Inmutabilidad: NO puedes hacer algo como texto[0] = 'A'. Debes de crear una nueva cadena.
- Indexación y Slicing: Cada carácter tiene un aposición (índice) que empieza en 0.
- Iterabilidad: Pudes recorrer una cadena con un blice for com si fuera una lista.
- Multilínea: Se pueden definir usand comilla triples.

"""

"""
=======================================================
                        Métodos
=======================================================

"""

""" Métodos de Formato """

#*      .upper() / .lower()
# Conviete a mayúsculas o minúsculas.
cadena = "Marioneta"
cadena_M = cadena.upper() # Convierte cada caracter en su caracter en mayúscula.
cadena_m = cadena.lower() # Convierte cada caracter en su caracter en minúscula.


#*      .capitalize()
# Primera letra e mayúscula.
cadena = "palabra"
cadena = cadena.capitalize()


#       .strip()
# Elimina espacios en blanco al inico y al final.
cadena = " socorro "
cadena = cadena.strip()


#*      .title()
# Pone en mayúscula la primera letra de cada palabra.
cadena = "hola mundo, bienvenido a méxico"



""" Métodos de Búsqueda y Modificación """


#      .replace(viejo, nuevo)
# Reemplaza una subcadena por otra.
cadena = "Suburvia moda para la vida real"
cadena_modificada = cadena.replace("Suburvia", "Ropa")


#*      .split(separador)
# Divide la cadena en una lista basada en un separador (por defecto, espacios).
cadena = "Cadena con espacios a proposito"
cadena = cadena.split()


#      .join(lista)
# Une los elementos de una lista en una sola cadena.
lista = ["Hola", "mundo"]
cadena = ""
cadena = " ".join(lista)
print(cadena)


#*      .find(sub)
# Duvuelve el índice de la primera aparición de lo que busques
print(cadena.find("m"))


""" Métodos de Validación (Los "is..")"""
#Devuelve True si...


#*      .isdigit()
# T o d o s los caracteres son dígitos (números).

#*      .isalpha()
# T o d o s los caracteres son letras del alfabeto.

#*      .isalnum()
# La cadena es alfanum+erica (letras y números).

#*      .isspace()
# La cadena solo contiene espacios en blanco, tabulaciones o saltos de línea.

#*      .islower() / .isupper()
# T o d o el texto está en minúsculas o mayúsculas respectivamente.
