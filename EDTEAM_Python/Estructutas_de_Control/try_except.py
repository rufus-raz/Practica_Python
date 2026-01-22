# Try Except

#* try: Permite ejecutar un bloque de código y capturar excepciones si ocurren.
#* except: Permite manejar las excepciones capturadas y definir acciones a tomar.
#* finaly: Se ejecuta independientemente de si hay o no errores.

name = "hola mundo"
raise Exception("Error creado a propósito")
try:
    print(name)
    raise Exception("Error creado a propósito")
except NameError:
    print("name no esta definido")
else:
    print("no hubo error")
finally:
    print("Esto siempre se ejecuta")