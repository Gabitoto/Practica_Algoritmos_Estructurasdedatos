import numpy as np


# Ejercicio numero 0:

"""palabra = input("Ingrese la palabra que desea analizar: ")

con_v = 0
con_c = 0
con_l = 0

for v in palabra.lower():

    if v in "aeiouáéíóú":
        con_v += 1

print(f"La cantidad de vocales es de {con_v}")

for c in palabra.lower():

    if c not in "aeiouáéíóú" and ((65 <= ord(c) <= 90) or ( 97 <= ord(c) <= 122)):
        con_c += 1 

print(f"La cantidad de consonantes es de {con_c}")

for f in palabra:
    if f.isalpha():
        con_l += 1

print(f"La cantidad de letras es de {con_l}")"""

# Ejercicio numero 1: 

"""nombre = input("Ingrese su nombre: ")

print(f"Saludos {nombre}!!!!")"""

# Ejercicio numero 2: 

"""palabra = input("Ingrese una palabra: ")
letra = input("Ingrese una letra que desea buscar: ")
con = 0
for l in palabra:
    if l in letra:
        con += 1
print(f"El numero de veces que aparece la letras {letra} en la palabra : {palabra} es de {con}.")"""

# Ejercicio numero 3:

"""print("Lea la cadena de texto y DECIDA: ")

palabra = input("Ingrese una cadena de texto --> ")

print("Menu")
print("1-Pasar a Mayusculas")
print("2-Pasar a Minusculas")
print("3-Solo la inicial con mayuscula")
print("4-exit")

while True:
    option=int(input("Ingrese la opcion que quiera: "))

    if option == 1:
        a = palabra.upper()
        print(a)
    elif option == 2:
        a = palabra.lower()
        print(a)
    elif option == 3:
        #a = palabra[0].upper()+palabra[1:]
        a = palabra.capitalize()
        print(a)
    else:
        print("Hasta Luego!!!!!")
        exit()"""
        
# Ejercicio numero 4:

"""palabra = input("Ingrese la palabra deseada: ")

for i in palabra.lower():

    if palabra == palabra[::-1]:
        print(f"La palabra {palabra} es palindromo.")
        break
    else:
        print(f"La palabra {palabra} no es palindormo.")
        exit()"""


# Ejercicio numero 5: 

"""siemprelista = []

muestra = (input("Ingrese la muestra de numeros separados por coma (ej:23,45,43,43,21,etc): "))
siemprelista = muestra.split(sep= ",", maxsplit= -1 )

lista1 = []

for i in siemprelista:
    if i == str(i):
        i = int(i)
        lista1.append(i)

media = sum(lista1)/len(lista1)
desv_stand = np.std(lista1)

print(f"El promedio del array es :{round(media,2)} mientras que su desvio estandar es: {round(desv_stand,2)}.")"""

# Ejercicio numero 6:

"""secuencia = "ATGCAAATTGTGTGTGCATAATTTATATAGGCTAGAATAGAATCGCTA"
cantidad_gc = secuencia.count("GC")
porcentaje = (cantidad_gc/len(secuencia))*100
print(round(porcentaje,2))"""


# Ejercicio numero 7: 

""" 
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
nom_org = input("Ingrese el nombre de la empresa a la que pertenece o institucion: ")

email = nombre[0].lower()+apellido.lower()+"@"+nom_org.lower()+".com"
print(email)
"""

# Practicas de String: 

"""a = "Loco,papa,total,war"

b,c,d,e=  a.split(sep=",")

print(f"b = {b} c = {c} d = {d} e = {e}.")"""

"""a = ":"
fecha = a.join(["19","4","2024"])
print(fecha)"""

"""a = "El loco vino y me quiso apuñalar, alto loco"
b = a.replace("loco","Hijo de mil puta")
print(f"{a}\n{b}")"""

"""a = "Nabin está entusiasmado por el nuevo programa de televisión; espera que este programa sea entretenido y educativo."
print(a.replace("programa","software"))"""

