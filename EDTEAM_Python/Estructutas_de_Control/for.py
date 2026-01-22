# For

#* El ciclo for se utiliza para iterar sobre una secuencia
#* de forma tipica, los parentesis indican (inicio, fin, paso)
#* El valor de fin no se incluye en la iteración
#* El valor de paso es opcional, si no se especifica, el valor por defecto es 1

#* Nota: En Python, el ciclo for itera sobre elementos de una secuencia
#* Sintaxis: for elemento in secuencia

# for clasico
for i in range(0,10,2):
    print("El valor de i es:", i) 

#* Cada elemento de la secuencia se asigna a la variable 'elemento'
#* y se ejecuta el bloque de código indentado

# for sobre listas
frutas = ["manzana", "banana", "cereza"]
# Para cada elemento en lista frutas
for fruta in frutas:
    print("Fruta: ", fruta)

# for sobre cadenas de texto
palabra = "Python"
for letra in palabra:
    print("Letra: ", letra)