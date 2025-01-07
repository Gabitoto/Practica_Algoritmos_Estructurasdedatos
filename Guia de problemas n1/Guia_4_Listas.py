import random as r
from tabulate import tabulate as t


# Ejercicio numero 1:
"""Escriba un programa en Python donde cree una lista con los primeros 20 números pares.
   Genere la lista de al menos dos maneras diferentes."""

"""list = []

i = 2
while i <= 20:

    if i % 2 == 0:
        list.append(i)
    i += 1

print(list)
"""
"""list = []
for i in range(0,42,2):
    list.append(i)
print(list)"""

"""list = [ x for x in range(0,40,2)]
print(list)"""

# Ejercicio numero 2: 
"""Escriba un programa en Python donde cree una lista con los primeros 20 números múltiplos de 3.
Genere la lista de al menos dos maneras diferentes."""

"""multiplos = [3*i for i in range(1,21)]

print(multiplos)

multiplos3 = []

for i in range(1,21):
    multiplos3.append(3*i)

print(multiplos3)"""

# Ejercicio numero 3:
"""Diseñe e implemente un programa en Python que ordene una lista con 10 valores de manera creciente y lo muestre por pantalla"""

"""lista = [r.randint(1,11) for i in range(1,11)]
lista.sort()

print(lista)

lista = []

for i in range(1,11):
    lista.append(r.randint(1,20))

lisord = sorted(lista, reverse=True)

print(lisord)"""

# Ejercicio numero 4: 
"""Escriba un programa en Python donde cree una lista con 15 elementos aleatorios entre 0 y 9.
Informe la cantidad de números únicos que contiene (sin repeticiones)."""

"""lista1 = [r.randint(0,9) for x in range(15)]
print(lista1)


for i in lista1:
    if lista1.count(i) == 1:
        print(i)
"""    



"""lista2 = []
for i in range(0,15):
    lista2.append(r.randint(0,9))

for j in lista2[::-1]:
    if lista2.count(j) == 1:
        print(j)

print(lista2)"""

# Ejercicio numero 5:
"""Leer N datos numéricos. Obtener la media (M) y la desviación estándar (DS) de la lista. """

"""x = int(input("Ingrese el numero de elementos que poseera la lista: "))

lista1 = []

for num in range(x):
    a = int(input("Ingrese numeros enteros: "))
    lista1.append(a)

prom = sum(lista1)/x
DESPUES VER QUE ONDA desv_standar = np.std(lista1)

print(f"Los datos son {lista1} y su media es {prom} mientras que su desviasion estandar es {round(desv_standar,2)}")"""

# Ejercicio numero 6:
"""Escriba un programa que lea dos numeros naturales y obtenga el maximo comun divisor (MDC) de los mismos"""

"""a = int(input("Ingrese un valor A: "))
b = int(input("Ingrese un valor B: "))

if b == 0:
    mcd = a
    print(mcd)
else:
    while b != 0:
        a,b = b,a % b
        mcd = a"""
#################
"""while b != 0:
    r = a % b
    a = b
    b = r
    mcd = a


print(mcd)"""

# Ejercicio numero 7:



# Ejercicio numero 8:
"""Leer el dni y las calificaciones (una calificación por alumno) de un grupo de alumnos que asistieron a una evaluación parcial de Fundamentos de Programación y almacenarlos en una lista.
Los datos finalizan con el dni 0.
Se desea obtener como información de salida:
a. Un listado de los DNI de los alumnos aprobados.
b. Las 2 mayores calificaciones y los DNI de los alumnos que las obtuvieron."""

"""matriz = []
condicion = True  
indice = 0      
while condicion == True:
    dni = int(input(f"Ingrese el dni: "))
    if dni==0:
        condicion = False
        break
    valor = int(input(f"Ingrese el valor de nota: "))
    if valor>6:
        matriz.append([])
        matriz[indice].insert(0,dni)
        matriz[indice].insert(1,valor)
        indice+=1
    
print(t(matriz))

aux1= [0,0]
aux2= [0,0]

for f in range(len(matriz)):
    if matriz[f][1] > aux1[1]:
        aux1 = matriz[f]
    elif matriz[f][1] > aux2[1]:
        aux2 = matriz[f]
print(aux1,aux2)"""
 

# Ejercicio numero 9:

"""año = [[] for x in range(6)]

for mes in range(len(año)):
    dia_mes = 0
    while dia_mes <= 5:
        monto_dia = int(input(f"Ingrese el monto del dia {dia_mes} del mes {mes+1}: "))
        if monto_dia == 0:
            break
        else:
            año[mes].append(monto_dia)
        dia_mes += 1

lista_mes_auxiliar = []
for mes in range(len(año)):
    total_mes = sum(año[mes])
    print(f"Lo recaudado del mes {mes + 1} es de {total_mes}")
    lista_mes_auxiliar.append(total_mes)

minimo_monto_mes = min(lista_mes_auxiliar)
mes_menor_aporte = lista_mes_auxiliar.index(minimo_monto_mes)+1
print(f"El mes que menos se recaudo fue el mes {mes_menor_aporte} con un valor de {minimo_monto_mes}.")
print(año)
"""
##################################################################

"""# Inicializar una lista para almacenar los totales mensuales
total_por_mes = [0] * 12

# Leer y procesar los datos de entrada
while True:
    # Leer el monto y la fecha
    monto = float(input("Ingrese el monto del aporte (0 para terminar): "))
    if monto == 0:
        break
    dia = int(input("Ingrese el día del aporte: "))
    mes = int(input("Ingrese el mes del aporte (1-12): "))
    
    # Sumar el monto al total del mes correspondiente
    total_por_mes[mes - 1] += monto

# a. Informar el total recaudado por mes
for i in range(12):
    print(f"Total recaudado en el mes {i+1}: {total_por_mes[i]}")

# b. Encontrar el mes de menor aporte
menor_aporte = min(total_por_mes)
mes_menor_aporte = total_por_mes.index(menor_aporte) + 1
print(f"El mes con el menor aporte es el mes {mes_menor_aporte} con un total de {menor_aporte}")
"""

# Ejercicio numero 10:

"""Una empresa distribuidora comercializa 25 artículos. Posee 4 sucursales y desea analizar el desempeño de las mismas.
Para ello se ingresan los datos correspondientes a las ventas efectuadas en cierto período:
código sucursal (1…4), código artículo (1…25), cantidad unidades vendidas. El ingreso de datos finaliza con el código de sucursal 0.
Determine e informe:
a. Las cantidades de unidades vendidas por la empresa de cada artículo. 
b. El total de unidades vendidas por la sucursal 3, sumando todos los artículos. 
c. La cantidad vendida por la sucursal 1 del artículo 6. 
d. La sucursal que vendió más unidades del artículo 8."""

# Creamos la tabla inicializada en cero.
tabla_principal = [[0 for _ in range(25)] for _ in range(4)]

# Creamos un ciclo que nos permita ingresar los datos en la zona que querramos.

while True:
    codigo_sucursal = int(input("Ingrese la sucursal en la cual vendio (1 al 4): "))
    if codigo_sucursal == 0:
        print(t(tabla_principal))
        break
    codigo_articulo = int(input("Ingrese el codigo del articulo (1 al 25): "))
    cantidad_unidad_vendida = int(input("Ingrese la cantidad vendida: "))
    # Acomodamos los indices para que comiencen en 0:
    codigo_sucursal -= 2
    codigo_articulo -= 1
    # Ubicamos lo agregado:
    tabla_principal[codigo_sucursal][codigo_articulo] += cantidad_unidad_vendida
    
# punto A: Las cantidades de unidades vendidas por la empresa de cada artículo.

lista_de_cant_totales = [0 for _ in range(25)]

for prod in range(len(tabla_principal)):
    for x in range(25):
        lista_de_cant_totales[x] += tabla_principal[prod][x]
    
for o in range(len(lista_de_cant_totales)):
    print(f"La cantidad del articulo {o+1} es {lista_de_cant_totales[o]}")    

# punto B: El total de unidades vendidas por la sucursal 3, sumando todos los artículos.

total_sucursal_3 = sum(tabla_principal[2])
print(total_sucursal_3)

# punto C: La cantidad vendida por la sucursal 1 del artículo 6.

cant_ven_art_6 = tabla_principal[0][7]
print(cant_ven_art_6)

# punto D: La sucursal que vendió más unidades del artículo 8.

listaux = []
sucursal_mas_vendio = [max(listaux),listaux.index(max(listaux))]
for prod in tabla_principal:
    art_8 = prod[9]
    listaux.append(art_8)

print(sucursal_mas_vendio)




###############################################################

#indexar una lista:

"""lista = [20,39,87,65,43]

for var in range(len(lista)):
    print(f" {var} = {lista[var]} ")

# Agregar insertando algo:

lista.insert(1,30)


print(lista)"""

"""lista = [20,4,32,65,43,2]
lista.pop(0)
print(lista)

for i in range(len(lista)):
    print(f"{i}={lista[i]}")"""



