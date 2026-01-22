
#* Diccionarios

#* Inicialización
mi_diccionario = {
    "nombre": "Alex",
    "edad": 25,
    "ciudad": "Madrid"
}

#* Metodos
# Acceso y Manipulación
# get(key): Es la forma segura de opbtener un valor. Si la llave existe, devuelve None
# en lugar de lanzar un error
# update({key: value}): Actualiza el diccionario con nuevos pares o modifica los existentes.
# pop(key): Elimina la llave espesificada y devuelve su valor.

# Inspección de Datos
# keys(): Devuelve una lista (vista) con todas las llaves del diccionario.
# values(): Devuelve una lista con todos los valores
#items(): Devuelve pares de (llave, valor) en formato de tuplas

# Limpieza
# clear(): Elimina todos los elementos, dejando el diccionario vacío {}
# copy(): Crea una copia superficial del diccionario.

#* Ejemplo
inventario = {"manzanas": 40, "peras": 30}

# Agrear un porducto nuevo
inventario["naranjas"] = 20

# Consultar de forma segura
syok_uvas = inventario.get("uvas", 0)

# Ver todo el inventario
for fruta, cantidad in inventario.items():
    print(f"Hay {cantidad} unidades de {fruta}")

#* Caracteristicas Clave
# - Las llaves son únicas: No puedes tener dos llaves iguales; si intentas agregar un arepetida,
# el valor se sobrescribirá
# - Mutable: Puedes cambiar, agregar o eiminar elementos después de crear el diccionario
# - Tipos mixtos: Las llaves suelen ser strings o números, pero los valores pueden ser cualquier
# cosa: listas, otros diccionarios o dunciones

#* Pythonic

# La Anatomia básica sige este patrón:
# * {nueva_llave: nuevo_valor for elemento in iterable if condicion}
# - nueva_llave: El nombre o transformación que quieres para la clave.
# - nuevo_valor: El valor que quieres asignar a esa clave.
# - for elemetno in iterable : El ciclo que recorre los datos originales.
# - if condicion: (Opcional) Un filtro para incluir solo ciertos elementos.

#* Ejemplos para entender lapotencia
"""

1. Transformar una lista en un diccionario
Imagina que tienes una lista de ciudades y quieres crear un diccionario donde la ciudad 
sea la llave y su longitud (número de letras) sea el valor.

"""
# forma tradicional:
ciudades = ["Madeid", "Bogorá", "México", "LIma"]
longitudes = {}

for c in ciudades:
    longitudes[c] = len(c)

# Con comprensión de diccionario:
longirudes = {c: len(c) for c in ciudades}

"""
2. Fltrar y transformar al mismo tiempo
Supogamos que tienes un diccionario con precios y quieres crear uno nuevo que solo incluya
los prductos caros ( más de $100) y, de paso, aplicarles un 10% de descuento.

"""
precios = {"laptop": 1200, "mouse": 25, "monitor": 200, "teclado": 80}
# Solo aplicamos el descuento a los que cuestan más de 100
ofertas = {k: v * 0.9 for k, v in precios.items() if v > 100}

#* ¿Cuando usarlas? 
# - Cuanod quieres limpiar datos: Por ejemplo. pasar todas las llaves a minúsculas.
# - Cuando quieres invertir un diccionario: Inrecambiar llaves por valores
# {v: k for k, v, in dict.items()}
# - Para mejorar el rendimiento: Las comprensiones suslen ser un poco más rápidas que los 
# bucles for tradicionales.