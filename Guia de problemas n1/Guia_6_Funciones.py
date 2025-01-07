import math
import random as r
from tabulate import tabulate as t


# Ejercicio numero 1:
"""Diseñe e implemente una funcion que reciba como parametro un numero natural e indique todos sus divisores"""

"""def Divisores(a):
    for i in range(1,a+1):
        if a % i == 0:
            lista_divisores.append(i)
    return lista_divisores

lista_divisores=[]
b = int(input("Ingrese el numero que desea averiguar sus divisores: "))
call = Divisores(b)
print(call)"""

# Ejercicio numero 2:
"""Diseñe una funcion que ingrese un numero natural y diga si es un numero primo marcandolo como True o False"""

"""def Es_primo(a):
    con = 0
    for x in range(2,a):
        if a % x == 0:
            con += 1
    if con == 0:
        return True
    else:
        return False

numero = int(input("Ingrese un numero natural para saber si es primo o no: "))

primo = Es_primo(numero)
print(f"El numero {numero} es {primo}")"""

# Ejercicio numero 3:
"""Escriba una función para calcular el mínimo común múltiplo (m.c.m.) de dos números enteros dados."""

"""def Mcm(a,b):
    condicion = True
    if num1 > num2:
        mcm = num1
    else:
        mcm = num2
    while condicion:
        if mcm % num1 ==0 and mcm % num2 == 0:
            condicion = False
        else:
            mcm += 1
    return mcm

num1 = int(input("Ingrese un numero 1: "))
num2 = int(input("Ingrese un numero 2: "))

maxcummul= Mcm(num1,num2)
print(f"El MCM de los numeros {num1} y {num2} es {maxcummul}")"""

# Ejercicio numero 4:
"""Diseñe e implemente una función en Python que multiplique una cantidad variable de números ingresados por el usuario y devuelva el resultado"""

"""def multiplicar(*args):
    # Si no hay argumentos, devolver None
    if not args:
        return None
    
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

# Solicitar entrada del usuario
entrada = input("Ingrese números separados por espacios: ")
numeros = list(map(float, entrada.split()))

# Llamar a la función con los números ingresados
resultado = multiplicar(*numeros)

# Mostrar el resultado
if resultado is not None:
    print(f"El resultado de multiplicar los números ingresados es: {resultado}")
else:
    print("No se ingresaron números para multiplicar.")"""


# Ejercicio numero 5:
"""La serie de Fibonacci se calcula de la forma siguiente: 1 + 1 + 2 + 3 + 5 + 8 + 13 +...Donde cada término i se calcula sumando los 2 anteriores: ti=ti-1+ti-2, y los 2 términos iniciales valen 1.
Escriba una función para calcular los primeros n números de la serie de Fibonacci y luego escriba un programa cliente que la utilice."""

"""def fibonacci_s(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    
    serie = [0,1]
    for i in range(2,n):
        numero = serie[-1]+serie[-2]
        serie.append(numero)
    
    return serie

n = int(input("Ingrese el numero que desea calcular con la serie: "))
print(f"La serie de Fibonacci hasta el término {n} es {fibonacci_s(n)}")"""

# Ejercicio numero 6:

"""def calculo_hipoxia(a, umbral = 72, dias_criticos = 2):
    cont_p_h = 0
    for p in a:
        paciente_con_hipoxia = sum(1 for medicion in p if medicion < umbral)
        if paciente_con_hipoxia >= dias_criticos:
            cont_p_h += 1
    return cont_p_h

tabla_paciente = [[r.randint(60,100) for dato in range(7)] for i in range(65)]

pacientes_finales = calculo_hipoxia(tabla_paciente)

print(t(tabla_paciente))
print(pacientes_finales)"""

# Ejercicio numero 7: 

"""def Columna_mes(tabla,i,a):
    #la funcion toma la tabla luego el indice del mes que queremos evaluar y el año desde cual analiza y devuelve una tupla con la temperatura maxima y el año.
    lista_c = []
    año = a
    for d in tabla:
        año += 1
        lista_c.append((d[i],año))
    año_max = max(lista_c)    
    return año_max

def Analisis_periodo(a,b):
    #Debe analizar un perido dado de un año y devolver un porcentaje de ese periodo. Donde a y b son == tabla[i][j]
    mes1 = a
    mes2 = b
    diferencia = mes1 - mes2
    porcentaje = (diferencia/mes1)*100
    return round(porcentaje,2)

def Prom_temp_max(tabla,año):
    #Calcula el promedio de las temperaturas maximas de un año.
    copia_tabla = tabla.copy()
    temp_max_6 = []
    for k in range(6):
        temp_max_6.append(max(copia_tabla[año]))
        copia_tabla[año].remove(max(copia_tabla[año]))
    
    promedio = sum(temp_max_6)/6
    return round(promedio,2),temp_max_6


tabla_1990_1999 = [[round(r.uniform(24,35),1) for _ in range(12)] for _ in range(10)]
print(t(tabla_1990_1999))

print(Columna_mes(tabla_1990_1999,1,1989))
print(Analisis_periodo(a = tabla_1990_1999[5][0],b = tabla_1990_1999[5][6]))
print(Prom_temp_max(tabla_1990_1999,1))"""

# Ejercicio numero 8:

#from Operaciones_naturales import *

# Programa Cliente:

"""n = int(input("Ingrese un numero natural entero para ser analizado: "))

print(Es_par(n))
print(Es_primo(n))
print(Divisores(n))
print(Factorial(n))"""

# Ejercicio numero 9: 

"""def Recaudacion_anual(tabla1,tabla2):
    # Esta funcion debe de calcular la recaudación anual en USD  y en PESOS de la sucursal requerida, tabla1 = TablaUSD[i] y tabla2 = TablaPESOS[i].
    sucursal_USD = sum(tabla1)
    sucursal_PESOS = sum(tabla2)
    return (sucursal_USD,sucursal_PESOS)
    
def Calculo_mes(tabla1,i):
    # Esta funcion calcula una sumatoria de una columna y devuelve un numero, tabla = Tabla o matriz y i = columna.
    col = []
    for n in tabla1:
        col.append(n[i])
    maximo = max(col)
    indice_M = col.index(maximo)+1    
    return (indice_M,maximo) 

tabla_USD = [[0 for _ in range(12)] for _ in range(8)]
tabla_PS = [[0 for _ in range(12)] for _ in range(8)]

while True:
    sucursal = int(input("Ingrese la sucursal (1 a 8): "))
    if sucursal == -1:
        break
    mes = int(input("Ingrese el mes que desea cargar (1-12): "))
    
    sucursal -= 1
    mes -= 1
    
    moneda = input("Ingrese en la moneda que desea pagarlo (USD o PESOS): ")
    if moneda == "USD":    
        monto = int(input("Ingrese el monto: "))
        tabla_USD[sucursal][mes] += monto
    elif moneda == "PESOS":
        monto = int(input("Ingrese el monto: "))
        tabla_PS[sucursal][mes] += monto

sucursal_analisis = int(input("Ingrese la sucursal que desea analizar en pesos y dolares (1-8): "))-1
print(Recaudacion_anual(tabla_USD[sucursal_analisis],tabla_PS[sucursal_analisis]))

print(Calculo_mes(tabla_USD,4))"""

# Ejercicio numero 10: 


"""def Condicion_alumno(tabla):
    # La funcion debe de tomar una lista y verificar si el alumno esta promocionado o libre.
    listaaux = []
    for nombre,parcial1,parcial2,trabajos_apro in tabla:
        if ((parcial1+parcial2)/2) >= 6 and trabajos_apro > 5:
            estado = "Regular"
            listafinal = [nombre,estado]
            listaaux.append(listafinal)
        else:
            estado="Libre"
            listafinal = [nombre,estado]
            listaaux.append(listafinal)
    return t(listaaux)


tabla_quimica = []
for n in range(1,11):
    nombre=r.choice(["Lucas","Eliseo","Keila","Alan","Facundo","Brian"]) 
    parcial1=r.randint(1,10)
    parcial2=r.randint(1,10)
    trabajos_apro=r.randint(1,10)
    
    listorti= (nombre,parcial1,parcial2,trabajos_apro)
    tabla_quimica.append(listorti)

print(t(tabla_quimica))
print(Condicion_alumno(tabla_quimica))"""