#1- Ingrese numero el informe si es par, impar, multiplo de 5 de 3 o de ambos.

"""print("Ingrese un numero y verifique si es par, impar, multiplo de 5 de 3 o de ambos.")
print()
num = int(input("Ingrese un numero entero natural: "))
if num % 2 == 0:
    print(f"El numero {num} es par")
else:
    print(f"El numero {num} es impar")
if num % 5 == 0:
    print(f"El numero {num} es multiplo de 5")
else:
    print(f"EL numero {num} no es multiplo de 5")
if num % 3 == 0:
    print(f"El numero {num} es multiplo de 3")
else:
    print(f"El numero {num} no es multiplo de 3")
if num % 5 == 0 and num % 3 == 0:
    print(f"El numero {num} es multiplo de 5 y de 3")
else:
    print(f"El numero {num} no es multiplo de 5 y de 3 a la vez")"""

#2- Calculadora de precio por edad:

"""print("Ingrese su edad para retirar su ticket: ")
age = int(input("Ingrese el dato aqui --> "))
if age < 4:
    print(f"Su entrada es GRATUITA!!!!")
elif 4 < age <=18:
    print(f"Su edad ingresada es {age} por lo que su entrada es de $150 USD")
elif age > 18:
    print(f"Su edad ingresada es {age} por lo que su entrada costara $250 USD")
else:
    print("Dato incorrecto vuelva a intentar!!!")"""

#3-Calculador de IMC:

"""print("Calcular su IMC nunca fue tan facil!!!")
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
print(calculo)"""

#4- Debo votar?

"""print("Progama para saber si debo votar este 2023...")
print()
age = int(input("Ingrese la fecha de nacimiento en ddmmaaaa --> "))
año_nac = age % 10000
votacion = 2023
calculo = votacion - año_nac
if calculo >= 16:
    print(f"tu edad es de {calculo} por lo que podes votar.")
else:
    print(f"tu edad es de {calculo} por lo que no podes votar.") """

#5- Cual es el mayor? 

"""a = int(input("Ingrese un numero --> "))
b = int(input("Ingrese un numero --> "))
c = int(input("Ingrese un numero --> "))

if a < b:
    aux = a
    a = b
    b = aux
if a < c:
    aux = a
    a = c
    c = aux 
if b < c:
    aux = b
    b = c
    c = aux
print(a,b,c)"""
