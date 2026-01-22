# Macht

# * Sirve para comparar dos valores y determinar cuál es mayor, menor o si son iguales

staus = "Solido"

match staus:
    case "Solido":
        print("La maateria tiene forma y volumen definidos.")
    case "Liquido":
        print("La materia tiene volumen definido pero no forma definida.")
    case "Gaseoso":
        print("La materia no tiene ni forma ni volumen definidos.")
    case "Solido" | "Liquido":
        print("La materia es sólida o líquida.") # Uso de operador OR
    case _:
        print("Estado de la materia desconocido.")