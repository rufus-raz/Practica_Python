# Practica

puntajes = [45, 88, 92, 70, 55, 100, 32]

Filtrar = [puntaje for puntaje in puntajes if puntaje >= 60 ]

Ordenar = sorted(Filtrar, reverse = True)

Promedio = sum(Ordenar) / len(Ordenar) if Ordenar else 0