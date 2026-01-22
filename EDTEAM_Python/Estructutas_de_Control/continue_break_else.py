# Continue

#* Continue => Permite saltar a la siguiente iteración del ciclo
#* Break => Permite salir completamente del ciclo
#* Else en ciclos => Se ejecuta cuando el ciclo finaliza normalmente

lista_numeros = [1, 2, 3, 4, 5, 6, 7 , 8, 9, 10]

# Continue
for numero in lista_numeros:
    if numero == 1:
        print("Se omite el numero 1")
        continue
    print("Numero actual: ", numero)
#* Omite el el proceso de la iteración cuando se coloca el continue y pasa a la siguiente iteración

# Break
for numero in lista_numeros:
    if numero == 1:
        print("Se omite el numero 1")
        break
    print("Numero actual: ", numero)
#* Cuando el ciclo encuentra el break, sale completamente del ciclo

# Else en ciclos
for numero in lista_numeros:
    if numero == 1:
        print("Es la primera iteración")
    print("Numero actual: ", numero)
else:
    print("El ciclo ha finalizado correctamente")
#* El bloque else se ejecuta cuando el ciclo finaliza normalmente