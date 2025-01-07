
"""1. Escriba un programa en Python donde el usuario ingrese un número natural positivo y muestre por consola todos los valores impares desde 1 hasta el número ingresado.

2.  Escriba un programa en Python donde el usuario ingrese números naturales, se sumen y se muestre el resultado por pantalla. Para que el usuario deje de añadir números a la suma debe ingresar el valor -1

3. Escriba un programa que pregunte cuántos números se van a introducir, pida esos números e informe el mayor, el menor y la media.

4. Escriba un programa que pida un número entero mayor que cero y calcule su factorial.

5. Diseñe e implemente un programa en Python que lea un número entero e informe si es primo o no.

6. Escriba un programa en Python que informe los números primos menores que 100.

7. Escriba un programa en Python que informe los primeros 100 números primo.

8. Una Empresa paga a sus 100 operarios semanalmente de acuerdo con la cantidad de horas trabajadas, a razón de X pesos la hora hasta 40 hs. y un 50% más por todas las horas que pasan de 40. Informar el total de salario a cobrar por cada trabajador.


9. Exhibir en pantalla 50 datos numéricos generados al azar entre 1 y 5000. Obtener como salida los siguientes parámetros estadísticos:

a) la media
b) los 2 mayores
c) el menor de la lista.
10. Una película ha costado 150 millones de dólares. La primera semana, la película tiene un costo de 31 millones de dólares. Cada semana que pasa, la factura es el 20% inferior a la de la semana anterior.
Escriba un programa que indique el número de semanas que se puede permitir la película para su producción."""


#Ejercicio numero 1: 

"""num = int(input("Ingrese un numero natural positivo: "))
for i in range(1,num+1,2):
    print(f"Impar --> {i}")"""

"""num = int(input("Ingrese un numero natural entero --> "))
for i in range(1,num+1):
    if i%2 != 0:
        print(f"Son impares --> {i}")"""


#Ejercicio numero 2:

"""print("Calculador y sumador")
print()
x = int(input("agregue numeros: "))
suma = 0
while x != -1:
    suma = x + suma
    print(suma)
    x = int(input("agregue numeros: "))
print(f"La suma es: {suma}")"""

#Ejercicio numero 3: 

"""print("Informe de altos bajos y media")
print()
cant = int(input("Ingrese la cantidad de numeros que va ingresar: "))
x = int(input("ingrese un numero --> "))
m = x
M = x
suma = x
for i in range(cant-1):
    x = int(input("ingrese un numero --> "))
    if x < m:
        m = x
    if x > M:
        M = x
    suma += x
p = suma / cant
print(f"los valores son {m},{M},{p}")"""

#Ejercicio numero 4

"""x = int(input("Numero entero mayor que cero --> "))
num = 1
fact = 1
while num <= x:
    fact *= num
    num += 1
print(f"El factorial de {x} es {fact}")"""

#Ejercicio numero 5:

"""num = int(input("Ingrese un numero para ver si es primo: "))
num_d = 0
for i in range(1,num+1):
    if num % i == 0:
        num_d += 1
if num_d <= 2:
    print(f"El numero {num} es primo")
else:
    print(f"El numero {num} no es primo ya que posee {num_d} divisores")"""
#################################
"""num = int(input("Ingrese un numero cualquiera: "))
if num > 1:
    con = 0
    for i in range(2,num):
        resto = num % i
        if resto == 0:
            con += 1
    if con == 0:
        print(f"El numero {num} es primo")
    else:
        print(f"El {num} no es primo")
else:
    print(f"El {num} no es primo")"""
###############################
"""num = int(input("numero cualquiera: "))
if num > 1:
    con = 0
    i = 2
    while i < num and con == 0:
        resto = num % i
        if resto == 0:
            con += 1
        i += 1
    if con == 0:
        print(f"El numero {num} es primo")
    else:
        print(f"El numero {num} no es primo")
else:
    print(f"El numero {num} no es primo")"""



#Ejercicio numero 6:

"""for num in range(1,100):
    can_d = 0
    i = 2
    while i < num and can_d == 0:
        resto = num % i
        if resto == 0:
            can_d += 1
        i += 1
    if can_d == 0:
        print(f"El numero {num} es primo")"""
    


#Ejercicio numero 7:



"""x = 1
cant_p = 0
while cant_p <= 100:
    cant_d = 0
    for i in range(1,x+1):
        if x % i == 0:
            cant_d += 1
    if cant_d <= 2:
        print("es primo",x)
        cant_p += 1 
    x += 1"""


#Ejercicio numero 8:

"""operarios = 100
pesos = int(input("Ingrese el valor de la hora: "))
horas = int(input("Ingrese las hora: "))

if horas <= 40:
    for i in range(1,operarios+1):
        pago = horas * pesos
        print(pago)
if horas > 40:
    for i in range(1,operarios+1):
        horas_e = horas - 40
        pago = (horas * pesos) + (horas_e * (pesos * 1.5))
        print(pago)"""


# Ejercicio numero 9:

"""
Exhibir en pantalla 50 datos numéricos generados al azar entre 1 y 5000.
 Obtener como salida los siguientes parámetros estadísticos:
a) la media
b) los 2 mayores
c) el menor de la lista.
"""

import random

"""maxi = random.randint(1,5000)
max2 = maxi
mini = maxi
suma = 0
con = 0
numeroale = random.randint(1,5000)
if numeroale > maxi:
    maxi = numeroale
else:
    max2 = numeroale
    mini = numeroale
while con <= 48:
    numeroale = random.randint(1,5000)
    print(numeroale)
    suma += numeroale
    if numeroale > maxi:
        max2 = maxi
        maxi = numeroale
    elif numeroale > max2:
        max2 = numeroale
    elif mini > numeroale:
        mini = numeroale
    con += 1
media = suma / 50
print(f"El Maximo es {maxi}")
print(f"El Segundo maximo es {max2}")
print(f"El Minimo es {mini}")
print(f"La Media es {media}")"""

###############################################

"""x = random.randint(1,5000)
menor = x
suma = x
mayor = x
mayor2 = x
print(x)
for i in range(49):
    x = random.randint(1,5000)
    print(x)

    suma += x

    
    if mayor < x:
        mayor2 = mayor
        mayor = x
    elif mayor2 < x:
        mayor2 = x
    elif x < menor:
        menor = x

print(f"El menor es {menor}")
print(f"La media es {suma/50}")
print(f"El mayor es {mayor}")
print(f"El segundo mayor es {mayor2}")"""


# Ejercicio numero 10:

"""Una pelicula a costado 150 millones de dolares.
La primera semana, la pelicula tiene un costo de 31 millones de USD. Cada semana que pasa, la factura es de 20% inferior a la de la semana anterior.
Escriba un programa que indique el numero de semanas que se puede permitir la pelicula para su producción."""

"""presupuesto = 150000000
costo_I = 31000000
costo_S = costo_I
semana = 0

while costo_S <= presupuesto:
    semana += 1
    presupuesto = presupuesto - costo_S
    costo_S = costo_S - (costo_S * 0.2)

print(f"La cantidad de semana que se puede producir la pelicula es de {semana} semanas.")"""

####################################

"""presupuesto = 150000000
costo_I = 31000000
costo_S = costo_I
semana = 0

while costo_S <= presupuesto:
    semana += 1
    presupuesto -= costo_S
    costo_S -= (costo_S * 0.2)  # Corrección aquí
    # También se podría escribir como: costo_S *= 0.8 para hacerlo más claro

print(f"La cantidad de semana que se puede producir la película es de {semana} semanas.")"""