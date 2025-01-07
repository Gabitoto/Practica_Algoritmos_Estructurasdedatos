# import math


#Determine la validez en Python de os siguientes identificadores:
#X-da = no valido
#float = palabra reservada
#def = palabra reservada
#x,7 = no valida
#3Total = no valido
#var56x = valido
#x7 = valido
#x/7 = no valido

#2- de hecho

#3- de hecho

#4-Diseñe e implemente un programa que defina y muestre por consola los valores de:

"""x = int(input("Valor entero: "))
c = float(input("Valor float: "))
v = complex(3,5)
b = format(input("Valor en notacion: "))
n = input("Ingrese String: ")
m = bool(input("Ingrese bool: "))
print(x,c,v,b,n,m)"""

#5-"Calculadora de pies a metros"

"""print("Calculadora de pies a metros")
print()
pies = int(input("Ingrese el valor en pies que desea convertir: "))
res = pies * 0.3048
print(f"La conversion de {pies} pies a metros es de {round(res,2)} metros")"""

#6-Saludador
"""print("Saluda a tu nuvo programa")
print()
name = input("Ingrese su nombre: ")
print(f"Bienvenido {name} a este maravilloso programa!!!")"""


#7-Calculadora de Radio y Perimetro

"""print("Calculador de Perimetro y Area")
print()
radio = float(input("Ingrese el radio de su circulo en cm: "))
area = math.pi * radio **2
perimetro = 2 * math.pi * radio
print(f"El rado ingresado es {radio} cm para el cual el area es {area} cm2 y el perimetro es {perimetro} cm")
"""

#8- Calculador de IMC

"""print("calculadora de IMC")
print()
peso = float(input("Ingrese su peso en Kg: "))
altura = float(input("Ingrese su altura en mt: "))
imc = round((peso / (altura ** altura)),2)
print(f"Tu índice de masa corporal es {imc} donde {imc} es el índice de masa corporal calculado redondeado con dos decimales.")
"""

#9- Editor de Fecha

"""print("Ingrese la fecha en formato aaaammdd: ")
fecha_entero = int(input("Ingrese la fecha: "))
año = fecha_entero // 10000
mes_dia = fecha_entero % 10000
mes = mes_dia // 100
dia = mes_dia % 100
print(f"La fecha es: {dia} del {mes} de {año}")"""

#10- Calculador de combustible

"""print("Calculador de combustible")
print()
km_in = float(input("ingrese el kilometraje inicial--> "))
km_fi = float(input("ingrese el kilometraje final--> "))
gasto = 2
precio = 150
precio_promo = 150*0.80
km_final = km_fi-km_in
gasto_final= km_final*gasto
precio_final= gasto_final*precio
precio_promo_final = gasto_final*precio_promo
print(f"los km recorrido son: {km_final} se consumio un total de {gasto_final} litros")
print(f"Los precios son en dias normales {precio_final} pesos y en promo es {precio_promo_final}")"""

