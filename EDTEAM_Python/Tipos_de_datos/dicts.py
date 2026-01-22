# Diccionarios

# Inicialización de un diccionario
usuario = {
    "nombre" : "Carlos",
    "apellido" : "Ramirez",
    "edad" : 29,
    "colores" : ["Azul", "Verde", "Rojo"]
}

print(usuario)
print(type(usuario))

print(usuario["nombre"]) # Acceso a un valor mediante su llave
print(len(usuario)) # Longitud del diccionario
print(len(usuario["colores"])) # Longitud de la lista dentro del diccionario

# Creación de un diccionario vacío
jugador = dict(equipo = "Real Madrid", goles = 30, equipos = [1, 2, 3]) 
print(jugador)
