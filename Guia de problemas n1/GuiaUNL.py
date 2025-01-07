# Ejercicios de Logica:

############################## GUIA NUMERO 2 ####################

# Ejercicio numero 9: determine si un año es bisiesto o no:

"""año = int(input("Ingrese el año que desea evaluar: "))

bisiesto = (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

if bisiesto:
    print("El año", año, "es bisiesto")
else:
    print("El año", año ,"no es bisiesto")"""

# Ejercicio numero 10: 

"""x = int(input("Ingrese un valor de X: "))
if x <= 2:
    fx = 5
elif 2 < x < 5:
    fx= (x**2)-6*x+10
else:
    fx= 4*x-15
print("el valor de F(x) es: ",fx)"""

# Ejercicio numero 11: 

"""a=int(input("Ingrese un numero entero positivo A: "))
b=int(input("Ingrese un numero entero positivo B: "))
c=int(input("Ingrese un numero entero positivo C: "))

if a > b and a > c:
    print("El numero 1 es el mayor")
elif b > a and b > c:
    print("El numero 2 es el mayor")
elif c > a and c > b:
    print("El numero 3 es el mayor")
elif a == b and b == c:
    print("Los 3 numeros son iguales")
else:
    print("Error")"""

# Ejercicio numero 12:

"""print("Determine el tipo de triangulo dependiendo de sus lados: ")

a=int(input("Ingrese la base del triangulo A: "))
b=int(input("Ingrese el lado izquierdo B: "))
c=int(input("Ingrese el lado derecho C: "))

if a == b and b == c:
    print("Es un triangulo Equilatero.")
elif b == c and (a != b and a != c):
    print("Es un triangulo Isosceles.")
elif a != b and b != c:
    print("Es un triangulo Escaleno.")
else:
    print("Error en los datos vuelva a intentarlo")"""

# Ejercicio numero 13: 

"""a= 3 
b= 4
c= 2

discriminante= b**2-4*a*c 

if discriminante > 0:
    print("Las raices on reales y diferentes.")
elif discriminante == 0:
    print("Las raices son reales e iguales")
elif discriminante < 0:
    print("Las raices son complejas y diferentes.")
"""

# Ejercicio numero 14:
"""import random as r

numero = r.randint(1,1000)
print(numero)

if numero < 10:
    print("El numero es de un digito")
elif numero > 10 and numero < 100:
    print("El numero es de dos digitos")
else:
    print("El numero es de 3 digitos")"""

# Ejercicio numero 15:

"""print("Venta de Productos: ")

opcion = input("Seleccione el producto que desea comprar 1 , 2 o 3: ")
if opcion == "1":
    importe= int(input("Ingrese el importe que desea pagar por el primer producto: "))
    if importe >= 10000:
        neto = importe * 0.9
        print(f"El importe que debe pagar con un descuento del 10 % es {neto}")
    else:
        print(f"El importe a pagar es {importe}")
elif opcion == "2":
    importe = int(input("Ingrese el importe que desea pagar por el segundo producto: "))
    if importe >= 5000:
        neto= importe * 0.95
        print(f"El importe a pagar con un descuento del 5% es {neto}")
    else:
        print(f"El importe a pagar es {importe}")
elif opcion == "3":
    importe = int(input("Ingrese el importe que desea pagar por el segundo producto: "))
    if importe >= 3000:
        neto = importe * 0.98
        print(f"El importe a pagar con un descuento del 2% es {neto}")
    else:
        print(f"El importe a pagar es {importe}")
else:
    print("El dato ingresado es incorrecto")"""

##############################################################################################

""""def es_cuadrado_perfecto(numero):
    #Esta funcion verifica si el numero ingresado por el usuario es un cuadrado perfecto
    raiz = int(numero**0.5)
    if raiz * raiz != int(numero):
        return False
    else:
        return True
    
x = int(input("Ingrese un numero: "))
cuadrado = es_cuadrado_perfecto(x)
print(cuadrado)"""

############################################### GUIA N° 3 ################################################



############################################### EXAMEN PARCIAL FIQ #############################################

# Problema numero 1:

"""def Palabra_mas_larga(string):
    # Funcion que recorre un string y retorna la palabra mas larga.
    palabra = string.split(" ")
    larga = ""
    for x in palabra:
        if len(x) > len(larga):
            larga = x
    return larga

palabrota = input("Ingrese la oracion: ")

resultado = Palabra_mas_larga(palabrota)
print(resultado) """

# Problema numero 2: 

"""def Contador_cadenas(lista):
    # Funcion que retorna una lista con el numero de elementos que contiene cada cadena componente de la primera lista.
    listaux = []
    for x in lista:
        contador = 0
        for i in x:
            if i in "123456789":
                f = int(i)
                contador += f
        listaux.append(contador)
    return listaux

listita = ["ruta78","juegonumero68","trucovale4", "argentina6-1uruguay","Holaloco"]

lista_final = Contador_cadenas(listita)
print(lista_final)"""

# Problema numero 3: 

"""def Es_primo(lista):
    # Funcion que retorna si un numero entero es un numeros primo.
    lista_final = []
    for k in lista:
        if k <= 1:
            pass
        else: 
            cont = 0
            for x in range(2,k):
                if k % x == 0:
                    cont += 1
            if cont >= 1:
                lista_final.append("No es primo")
            else:
                lista_final.append(k)
    return lista_final

lista_oficial = [1,2,3,6,9,7,11,23,678,48]
final = Es_primo(lista_oficial)    
print(final)"""


"""def fun_e3(mi_entrada):
    lista= []
    for i in mi_entrada:
        if 1 == i:
            pass
        else:
            es_primo = True
            for x in range(2,i):
                if i % x == 0:
                    es_primo = False
            if es_primo:
                lista.append(i)
    return lista

mi_entrada= [1,2,3,4,7,21,97]
print(fun_e3(mi_entrada)) """

# Problema numero 4:

def Encuentra_caracteres(lista):
    # Funcion que retorna una lista con los doce elementos que poseen los siguientes caracteres: # , . , V
    lista_final = []
    for x in lista[-1:-13:-1]:
        for i in x:
            if i in ".V#":
                lista_final.append(x)
    return lista_final

lista = ["#gato", "nada", ".1", ".2", ".3", ".4", ".5"," V6", ".7"," V8", ".9", ".10", ".11", "V12", ".13"]
final = Encuentra_caracteres(lista)
print(final)


# Problema numero 5:

"""def Validacion(n):
    # Funcion que recibe un numero entero positivo y retorna True unicamente si tiene mas de 10 cifras, es multiplo de 21 y la cifra de las decenas es un 8
    if n % 21 == 0 and n == len([1 for _ in range(n+1)]):
        numeros = str(n)
        for c in numeros[-2:-3:-1]:
            if int(c) == 8:
                return True
    else:
        return False        

numero = int(input("Ingrese un numero entero positivo: "))

objeto = Validacion(numero)
print(objeto)"""