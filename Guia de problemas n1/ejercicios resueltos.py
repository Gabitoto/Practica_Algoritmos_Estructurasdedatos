import random as rd
import cmath 

# Ejercicio nº 1
# Definir una función que tome como argumento una lista y devuelva el mayor de sus elementos.

def most_number(lista):
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
print(f"el numero mas alto es {numero_alto}")

# Ejercicios nº 2
# Definir una función que calcule la longitud de una lista o una cadena dada.

def distancia(entrada):
    count = 0
    for x in entrada:
        count += 1
    return count

variable1 = [1,4,5,3,2,5,6]
variable2 = "Hola Mundo Cruel"

numero = distancia(variable1)
num = distancia(variable2)

print(numero,num)

# Ejercicio nº 3
# Escribir una función que reciba una cadena de caracteres y determine la cantidad de vocales que posee.

def vocales(cadena):
    count= 0
    for x in cadena:
        if x in "aeiouAEIOUàèìòùÀÈÌÒÙáéíóúÁÉÍÓÚ":
            count += 1
    return count

cadenita = "hola loco que onda?"
number = vocales(cadenita)

print(number)

# Ejercicio nº 4
# Escribir dos funciones que realicen operaciones matemáticas básicas: una debe realizar la suma de todos los elementos de una lista y la otra multiplicarlos. 
# Por ejemplo: para la lista [1,2,3,4] la primera función debería devolver 10 y la segunda debería devolver 24.

def sumatoria(lista):
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

print(var,var2)

# Ejercicio nº 5
# Escribir una función que tome una lista de palabras y devuelva la más larga de ellas.


def mas_larga(lista):
    maslarga = ""
    contador = 0
    for _ in lista:
        count=0
        for x in _:
            count += 1
        if count > contador:
            maslarga = _

    
    return maslarga

listatita = ["mama","Lucas","Hernandez"]
final = mas_larga(listatita)
print (f"la palabra mas larga es {final}")

# Ejercicio nº 6
# Escribir una función que permita calcular las raíces de una ecuación cuadrática.

def calcular_raices(a, b, c):
    if a == 0:
        return "Esto no es una ecuación cuadrática, ya que 'a' es 0."
    
    discriminante = b**2 - 4*a*c
    
    if discriminante > 0:
        raiz1 = (-b + discriminante**0.5) / (2*a)
        raiz2 = (-b - discriminante**0.5) / (2*a)
        return f"Las raíces son reales y diferentes: {raiz1} y {raiz2}"
    elif discriminante == 0:
        raiz = -b / (2*a)
        return f"Hay una raíz real (repetida): {raiz}"
    else:
        raiz1 = (-b + cmath.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - cmath.sqrt(discriminante)) / (2*a)
        return f"Las raíces son complejas: {raiz1} y {raiz2}"

c = float(input("Ingresa el valor de 'c': "))
b = float(input("Ingresa el valor de 'b': "))
a = float(input("Ingresa el valor de 'a': "))

resultado = calcular_raices(a, b, c)
print(resultado)


# Ejercicio nº 7
# Escribir una función que pida dos palabras y determine si las mismas riman o no. Considere que las dos palabras riman si coinciden en sus tres últimas letras.

def riman(a,b):
    palabrita1 = a[-2:]
    palabrita2 = b[-2:]
    if palabrita1.lower() == palabrita2.lower():
        return (f"Las palabras {a} y {b} riman")
    else:
        return (f"Las palabras {a} y {b} NO riman")

a = "Oso"
b = "Perezoso"
final= riman(a,b)
print(final)


# Ejercicio nº 8
# Escribir una función que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable. 
# El programa debe mostrar por pantalla la frase “Tu índice de masa corporal es <imc>”, donde <imc> es el índice de masa corporal calculado (redondee el valor a dos decimales).

print("Calcular su IMC nunca fue tan facil!!!")
print("Ingrese su peso y altura y deje que nosotros se lo calculemos")
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en m: "))
calculo = peso / (altura**2)
if calculo < 18.5:
    print("BAJO PESO")
elif 18.5 < calculo < 24.9:
    print("PESO NORMAL")
elif 25 < calculo < 29.9:
    print("SOBREPESO")
elif 30 < calculo < 34.9:
    print("OBESIDAD TIPO 1")
elif 35 < calculo < 39.9:
    print("OBESIDAD TIPO 2")
elif calculo >= 40:
    print("OBESIDAD TIPO 3")
else:
    print("ERROR-Intentelo de vuelta")
print(calculo)

# FINAL #