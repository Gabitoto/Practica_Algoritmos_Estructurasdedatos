import random as rd

# Ejercicio nº 1
# Definir una función que tome como argumento una lista y devuelva el mayor de sus elementos.

"""def most_number(lista):
    lista_ord = sorted(lista)
    M = 0
    for x in lista_ord:
        if x > M:
            M = x
    return M

listita = [(rd.randint(1,100)) for x in range(8)]
for x in listita:
    print(x)
numero_alto = most_number(listita)
print(f"el numero mas alto es {numero_alto}")"""

# Ejercicios nº 2
# Definir una función que calcule la longitud de una lista o una cadena dada.

"""def distancia(entrada):
    count = 0
    for x in entrada:
        count += 1
    return count

variable1 = [1,4,5,3,2,5,6]
variable2 = "Hola Mundo Cruel"

numero = distancia(variable1)
num = distancia(variable2)

print(numero,num)"""

# Ejercicio nº 3
# Escribir una función que reciba una cadena de caracteres y determine la cantidad de vocales que posee.

"""def vocales(cadena):
    count= 0
    for x in cadena:
        if x in "aeiouAEIOUàèìòùÀÈÌÒÙáéíóúÁÉÍÓÚ":
            count += 1
    return count

cadenita = "hola loco que onda?"
number = vocales(cadenita)

print(number)"""

# Ejercicio nº 4
# Escribir dos funciones que realicen operaciones matemáticas básicas: una debe realizar la suma de todos los elementos de una lista y la otra multiplicarlos. 
# Por ejemplo: para la lista [1,2,3,4] la primera función debería devolver 10 y la segunda debería devolver 24.

"""def sumatoria(lista):
    sum = 0
    for x in lista:
        sum += x
    return sum

def multidoppler(lista):
    mult = 1
    for x in lista:
        mult *= x
    return mult

listaza = [1,2,3,4,5]
var = sumatoria(listaza)
var2 = multidoppler(listaza)

print(var,var2)"""

# Ejercicio nº 5
# Escribir una función que tome una lista de palabras y devuelva la más larga de ellas.

