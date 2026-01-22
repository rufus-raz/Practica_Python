# Tuplas

# Las tuplas son inmutables
# No se puededen modificar una vez creadas
names = ("Carlos", "Juan", "Vladimir")
print(names[0])

# Desempaquetado de tuplas
name1, name2, name3 = names
print(names)

# tupas anidadas
new_tuple = (names, (1, 2, 3, 4, 5))
print(new_tuple)

# Acceso a elementos de tuplas anidadas
print(new_tuple[1], [2])

# Méetodos de tuplas
print(names.count("Juan")) # Cuaenta cuantas veces aparece un elemento
print(names.index("Vladimir")) # Indica la posición de un elemento