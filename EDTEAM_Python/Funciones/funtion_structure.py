# Funciones

#* def: Define una función.
#* return: Devuelve un valor desde una función.
#* scope: Ámbito de una variable (local o global), es el alcance donde una variable es accesible.

"""def nombre_funcion(parametros):"""
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a        
print(fibonacci(10)) # Output: 55


#* lambda: Crea funiones anónimas (sin nombre).
"""lambda argumentos: expresión"""
square = lambda x: x * x
print(square(5)) # Output: 25

#* map: Aplica una función a todos los elementos de un iterable.
numbers = [1, 2, 3, 4, 5]
"""map(función, iterable)"""
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers) # Output: [1, 4, 9, 16, 25]

#* Multiples return values: Una función puede devolver múltiples valores como una tupla.
def min_max(numbers):
    return min(numbers), max(numbers)
minimum, maximum = min_max(numbers)
print(minimum, maximum)

#* Parámetros y argumentos:
# Parámetros son los valores que se definen en la función.
# Argumentos son los valores que se pasan a la función cuando se llama.
def greet(name, message="Hello"): # Parámetro con valor por defecto
    return f"{message}, {name}"
print(greet("Alice")) # Output: Hello, Alice
print(greet("Bob", "Hi")) # Output: Hi, Bob
print(greet(message="Good morning", name="Charlie")) # Output: Good morning, Charlie
# Llamada con argumentos nombrados

#* args y kwargs:
# args: permite pasar múltipes argumentos posicionales a una función.
# kwargs: permite pasar múltiples argumetos nombrados a una función.
def func_with_args(*args, **kwargs):
    print("Positional arguments: ", args)
    print("keyword arguments: ", kwargs)

func_with_args(1, 2, 3, name="Alice", age=30)

days ={
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

#* Uso de kwargs para obtener el nombre del día de la semana
def get_day_name(**kwargs): # Keyword arguments
    day_number = kwargs.get("day_number", 1) # Valor por defecto 1
    return days.get(day_number, "Invalid day number") # Valor por defecto si no existe
print(get_day_name(day_number= 3))