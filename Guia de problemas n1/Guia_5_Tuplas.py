# import random as r
# from tabulate import tabulate as t

# Ejercicio numero 1:
"""A partir de una tupla numérica, devuelva la suma de sus elementos."""

"""tupla1 = (1,2,4,6,8,10,12)
sumatoria = sum(tupla1)
print(sumatoria)
"""
##############################

"""lista2 = []

num =int(input("Ingrese el numero de elementos que va a poseer la tupla: "))
for x in range(num):
    value = int(input("Ingrese un numero entero natural: "))
    lista2.append(value)

tupla2 = tuple(lista2)
sumatoria2 = sum(tupla2)
print(sumatoria2)"""

# Ejercicio numero 2:
"""Escriba un programa en Python para evaluar si una tupla tiene elementos que se repiten o no."""

"""lista1 = []

num =int(input("Ingrese el numero de elementos que va a poseer la tupla: "))
for x in range(num):
    opt = input("Ingrese el tipo de elemento que desea agregar(st,in,fl): ").lower()
    if opt == "st":
        value =(input("Ingrese el elemento: "))
        lista1.append(value)
    elif opt == "in":
        value =int(input("Ingrese el elemento: "))
        lista1.append(value)
    elif opt == "fl":
        value =float(input("Ingrese el elemento: "))
        lista1.append(value)
    else:
        print("Vuelva a intentarlo!!!")
        opt= input("Ingrese el tipo de elemento que desea agregar(st,in,fl): ").lower()

tupla = tuple(lista1)"""

"""tupla = (2,3,4,4,5,6,7,5)
repeticion=[]
for i in tupla[::-1]:
    if tupla.count(i) != 1:
        repeticion.append(i)

print(f"Los elementos que se repiten son: {tuple(repeticion)}.")"""

# Ejercicio numero 3:

"""ADN=("A","C","T","G")

listado = [r.choices(ADN) for i in range(5000)]

lista = [o for l in listado for o in l]

proporciones = []
for n in ADN:
    calc = lista.count(n) / len(lista)
    proporciones.append([n,round(calc,2)])

cant = 0
for c in lista:
    if c == "T":
        cant += 1
        
prop_CG = 0
for p in range(len(lista)-1):
    if lista[p] == "C" and lista[p+1] == "G":
        prop_CG += 1

print(lista)
print(f"Las proporciones de cada cadena es de: {proporciones}")
print(f"La cantidad total de T es de {cant}")
print(f"La cantidad total de CG es de {prop_CG}.")"""

# Ejercicio numero 4:
"""Genere una secuencia de 1000 números aleatorios entre 0 y 1, con dos decimales. Obtenga un listado donde se registre la cantidad de veces que aparece cada uno de los valores, como pares: (valor, cant.)."""

"""secuencia = [round(r.random(),2) for i in range(50)]

registro = []

for i in secuencia[::-1]:
    c = secuencia.count(i)
    if (c,i) not in registro:
        registro.append((c,i))

lista_final = sorted(registro, key=lambda x: x[1])
#registro.sort(key=lambda x:x[1])
print(lista_final)
"""

 


