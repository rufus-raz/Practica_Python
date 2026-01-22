# Practica

puntajes = [45, 88, 92, 70, 55, 100, 32]

# Guarda en una nueva lista los puntajes mayores o iguales a 60
Filtrar = [puntaje for puntaje in puntajes if puntaje >= 60 ] 
# Luego ordena esa nueva lista de mayor a menor
Ordenar = sorted(Filtrar, reverse = True) # sorded es una funcion que ordena una lista sin modificar la original, como parametro recibe una 
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