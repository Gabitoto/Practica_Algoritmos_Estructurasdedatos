"""Problemas complementarios:

1. Escriba un programa que escriba la tabla de multiplicar de un número ingresado por el usuario.
 El usuario también establece si la tabla se muestra en forma ascendente o descendente.

2. Escriba un programa que solicite al usuario ingresar una contraseña numérica.
 La contraseña se encuentra almacenada en el programa. El usuario tiene hasta tres intentos para ingresarla en forma correcta.
 Ante cada intento se mostrará un mensaje de error o de éxito. Si se superan los tres intentos se mostrará otro mensaje de error y se terminará el programa.

3. Una cooperadora escolar recibe aportes voluntarios y de montos variables de sus alumnos.
 La escuela tiene 3 cursos de jardín y desea hacer un análisis de los aportes por curso y por cada uno de los meses del año pasado.
Para ello se leen los datos de cada aporte: Curso, Mes, Monto: donde curso es un número de 1 a 3, mes es un número de 1 a 12 y monto es el valor monetario del aporte;
 estos datos terminan al ingresar un 0 para el dato curso.
 Un mismo alumno puede hacer varios aportes en el año. Se desea informar: 
 a) el total aportado en cada curso en todo el año;  
 b) el total recaudado sumando aportado en los meses de marzo y agosto sin importar el curso.

4. Se lee el código de un paciente y luego los 30 valores consecutivos de concentración de glucosa en sangre registrados en ayunas durante un mes.
 Mediante un programa se desea determinar cuántas veces supero el paciente el umbral de 110 mg/dl y cuál fue la mayor diferencia entre registros de días consecutivos. 

5. Un grupo de investigadores analiza el comportamiento de 17 ratones de laboratorio a quienes se le suministró una hormona de crecimiento y se les midió el peso durante 56 días a cada uno.
 Para ello se ingresan ordenadamente: el nº de ratón y luego los 56 valores de peso obtenidos en el período; luego el siguiente nº de ratón y sus 56 valores de peso; así sucesivamente.
 Escriba un programa que calcule e informe: 
 a) los gramos de peso ganados en cada semana para cada ratón. 
 b) ¿Cuántos ratones superaron el peso de 580 gr al final de período? 
 c) El nº del ratón que logró el mayor peso."""

# Ejercicio numero 1:

"""print("Imprima la tabla de multiplicar: ")
option = input("Elija si quiere que se vea Ascendente-A- o descendente-B- :  ")
if option == "A" or option == "a":
    num = int(input("Elija el numero: "))
    for i in range(1,10+1):
        tabla = num * i
        print(f"{num} x {i} = {tabla}")
if option == "B" or option == "b":
    num= int(input("Elija un numero: "))
    for i in range(10,0,-1):
        tabla = num * i
        print(f"{num} x {i} = {tabla}")"""

###############################

"""print("Imprima la tabla de multiplicar: ")
option = input("Elija si quiere que se vea Ascendente -A- o descendente -B- :  ")
if option == "A" or option == "a":
    num = int(input("Elija el numero: "))
    i = 1
    while i <= 10:
        tabla = i * num
        print(f"{i}x{num}={tabla}")
        i += 1
if option == "B" or option == "b":
    num= int(input("Elija un numero: "))
    i = 10
    while i >= 1:
        tabla = i * num
        print(f"{i}x{num}={tabla}")
        i -= 1"""

# Ejercicio numero 2:

"""contra = int(input("Ingrese la contraseña: "))
for i in range(1,3 + 1):
    if contra == 1234:
        print("Bienvenido señor")
        break
    else:
        print("contraseña incorrecta")
        contra = int(input("Ingrese la contraseña: "))
        continue"""

###########################

"""contra = int(input("--> "))
intentos = 3
while intentos > 1:
    if contra == 1234:
        print("Contraseña correcta.")
        break
    elif contra != 1234:
        intentos -= 1
        print(f"Error te quedan {intentos} intentos.")
        contra = int(input("--> "))
if intentos == 1:
    print("Usted a sido bloqueado")
else:
    print("Bienvenido loco") """

##################################

"""contra = "17052002"
con = 3

password = input("Ingrese su contraseña: ")

while password != contra:
    con -= 1
    if con == 0:
        print("BLOQUEADO")
        break
    elif con > 0:
        print(f"Le quedan {con} intentos.")
        password = input("Ingrese nuevamente su contraseña: ")
if password == contra:
    print("Bienvenido")"""

# Ejercicio numero 3:
"""curso = 3
while curso != 0:
    curso =int(input("Ingrese el curso: "))
    if curso == 1:
        sumatoria1 = 0
        sumatoriaux = 0
        for i in range(1,11):
            sumatoria1 += int(input("Ingrese el monto: "))
            if i == 2 or i == 6:
                sumatoriaux += int(input("Ingrese monto Marzo o Agosto: "))
    if curso == 2:
        sumatoria2 = 0
        sumatoriaux2 = 0
        for i in range(1,11):
            sumatoria2 += int(input("Ingrese el monto: "))
            if i == 2 or i == 6:
                sumatoriaux2 += int(input("Ingrese monto Marzo o Agosto: "))
    if curso == 3:
        sumatoria3 = 0
        sumatoriaux3 = 0
        for i in range(1,11):
            sumatoria3 += int(input("Ingrese el monto: "))
            if i == 2 or i == 6:
                sumatoriaux3 += int(input("Ingrese monto Marzo o Agosto: "))

sumatoria_T= (sumatoria1+sumatoriaux) + (sumatoria2+sumatoriaux2) + (sumatoria3+sumatoriaux3)
sumatoriaux_T= sumatoriaux+sumatoriaux2+sumatoriaux3
print(f"El total del año de los cursos es {sumatoria_T} y el de los meses de Marzo y Agosto {sumatoriaux_T}")"""

#############################################

"""
total_c1 = 0
total_c2 = 0
total_c3 = 0
total_3_8 = 0

for curso in range(1,4):
    if curso == 1:
        for mes in range(1,11):
            total_c1 += int(input(f"Monto del mes: "))
            if mes == 2 or mes == 6:
                total_3_8 += int(input(f"Monto del mes: "))
    if curso == 2:
        for mes in range(1,11):
            total_c2 += int(input(f"Monto del mes: "))
            if mes == 2 or mes == 6:
                total_3_8 += int(input(f"Monto del mes: "))
    if curso == 3:
        for mes in range(1,11):
            total_c3 += int(input(f"Monto del mes: "))
            if mes == 2 or mes == 6:
                total_3_8 += int(input(f"Monto del mes: "))            
print(f"El total por curso en los meses de agosto y marzo es {total_3_8}")
print(f"Curso 1: {(total_c1+(total_3_8/3))}\nCurso 2: {(total_c2+(total_3_8/3))}\nCurso 3: {(total_c3+(total_3_8/3))}.")
"""

# Ejercicio numero 4:

"""umbral = 110
diferencia_mayor = 0
con = 0
for dia in range(1,30):
    valor_actual = int(input(f"Ingrese valor actual de glucosa en el dia {dia}: "))

    if dia > 1:
        diferencia = abs(valor_actual - valor_anterior)

        if diferencia > diferencia_mayor:
            diferencia_mayor = diferencia

    if valor_actual > umbral:
        con += 1

    valor_anterior = valor_actual

print(f"El numero de veces que supero los 110 mg/dl es {con}")
print(f"La mayor diferencia entre dias consecutivos es {diferencia_mayor}.")"""

#Ejercicio numero 5:

"""sup580=0
num_mayor=0
peso_mayor=0

for i in range(1,4):
  peso=0
  print("Nuevo raton")
  for j in range(1,3):
    gan_sem=0
    for k in range(1,4):
      pesaje = int(input("Pesaje semana {j}, dia {k}: "))
      if j==1 and k==1:
        peso+=pesaje
      else:
        gan_sem += pesaje - peso
        peso=pesaje

    print("El raton {i} obtiene una ganancia en la semana {j} de:", gan_sem)
  print("El raton obtiene una peso de:", peso)

  if(peso>580):
    sup580+=1
  if(peso>peso_mayor):
    peso_mayor=peso
    num_mayor=i

print("El raton con mayor peso es el {num_mayor} con un pesaje de {peso_mayor}")"""

#######################################################################






# Ejercicio numero 6: 

"""ventas_s1 = 0
ventas_s2 = 0
ventas_s3 = 0
ventas_s4 = 0
articulo6_s1 = 0

while True:
    option = int(input("Ingrese a que sucursal desea ingresar(1,2,3,4) o si desea salir (0): "))

    if option == 1:
        for i in range(1,8):
            if i == 6:
                articulo6_s1 = int(input(f"Ingrese la cantidad de unidades vendidas del articulo {i}: "))
                ventas_s1 += articulo6_s1
            ventas_s1 += int(input(f"Ingrese la cantidad de unidades vendidas del producto {i}: "))
    if option == 2:
        for i in range(1,4):
            ventas_s2 += int(input(f"Ingrese la cantidad de unidades vendidas del producto {i}: "))
    if option == 3:
        for i in range(1,4):
            ventas_s3 += int(input(f"Ingrese la cantidad de unidades vendidas del producto {i}: "))
    if option == 4:
        for i in range(1,4):
            ventas_s4 += int(input(f"Ingrese la cantidad de unidades vendidas del producto {i}: "))
    if option == 0:
        print("Hasta luego...")
        break

print(f"El total de ventas de las diferentes sucursales es: 1-{ventas_s1} 2-{ventas_s2} 3-{ventas_s3} 4-{ventas_s4}.")
print(f"La cantidad total vendida en la sucursal 1 del articulo 6 es de {articulo6_s1}.")"""
            
#####################################

"""ventas_s1 = 0
ventas_s2 = 0
ventas_s3 = 0
ventas_s4 = 0
articulo_6_s1 = 0

for sucursales in range(1,5):
    for articulos in range(1,7):
        ventas = int(input("Ingrese la cantidad de ventas: "))

        if sucursales == 1:
            ventas_s1 += ventas
        elif sucursales == 2:
            ventas_s1 += ventas
        elif sucursales == 3:
            ventas_s1 += ventas
        else:
            ventas_s1 += ventas
        if sucursales == 1 and articulos == 6:
            articulo_6_s1 += ventas

print(f"Resultados")
print(f"El total de articulos vendidos en la sucursal 3 es de {ventas_s3}.")
print(f"El total de ventas del articulo 6 de la sucursal 1 es de {articulo_6_s1}")"""








    




     



    












