import csv
# from tabulate import tabulate as t


# Ejercicio numero 1: 
"""Lea el archivo personal.txt que contiene un listado con los nombres  y apellidos de los agentes de la Facultad de Ingeniería de la UNER, y muestre el contenido del mismo por consola."""

"""with open("personal.txt","r+") as archivo:
  for n in archivo:
    print(n)
"""

# Ejercicio numero 2:
"""Con la información obtenida en el ejercicio anterior escribir un archivo, correos.txt, con las direcciones de correo electrónico de los agentes. 
Este correo se forma con la primera letra del nombre seguido del apellido y el dominio "@ingenieria.edu.ar"""

"""with open("personal.txt", "r+") as archivo:
  listado_email = []
  for n in archivo:
    linea=n.rstrip("\n")
    names = linea.split(sep=" ")
    email= linea[0]+names[1]+"@ingenieria.edu.ar"
    listado_email.append(email)
  
out = open("Condicion.txt",'w') 
for i in listado_email:
  out.write(i+"\n")
  
out.close()"""

# Ejercicio numero 3: 

"""with open("ECG.txt", "r+") as archivo:
  listaux = []
  for r in archivo:
    line = r.rstrip("\n")
    numer = int(line)
    listaux.append(numer)
  prom = sum(listaux)/10000
  umbral = 20 * prom
  con = 0
  for u in listaux:
    if u > umbral:
      con += 1
  
  print(prom,con)
  
archivo.close()"""

# Ejercicio numero 4: 

"""with open("PALABRAS.txt", "r+") as archivo:
  listaaux = []
  for l in archivo:
    lines = l.rstrip("\n")
    listaaux.append([lines])
  
  for i in range(len(listaaux)):
    for p in listaaux[i][1::-1]:
      if p[-1] in "aeiou":
        listaaux[i] = p + "s"
      else:
        listaaux[i] = p + "es"

  archivo.seek(0)
  for w in listaaux:
    archivo.write(w + '\n')

archivo.close()  """   


# Ejercicio numero 5: 

"""def Expor_mes_pais(tabla,mes):
  # Funcion que sirve para verificar que pais tuvo la mayor exportacion y en que mes.
  resultado = 0
  for c in tabla:
    resultado += c[mes]
  return resultado


with open("export.txt", "r+") as archivo:
  lista1 = []
  for lines in archivo:
    l = lines.rstrip("\n")
    n1,n2,n3=l.split()
    n2 = n2[2:4]
    lista1.append([int(n1),int(n2),int(n3)])
  archivo.seek(0)
  print(lista1)
  
  tabla_final = [[0 for _ in range(12)] for _ in range(10)]
  for n1,n2,n3 in lista1:
    tabla_final[n1-1][n2-1] += n3
  print(t(tabla_final))
  
  for m in tabla_final:
    print(f"El total exportado en el 2021 del pais {tabla_final.index(m)+1} es de {sum(m)}")
  
  print(Expor_mes_pais(tabla_final,2))

archivo.close()"""

# Ejercicio numero 6:

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
serie = fibonacci_s(n)
nombredelarchivo = input("Ingrese el nombre del archivo: ") + ".txt"

archivo = open(nombredelarchivo, "w")
for x in range(len(serie)):
  x = str(serie[x])
  archivo.write(x + "\n")"""
  
"""with open(nombre_archivo, 'w') as archivo:
    for numero in serie_fibonacci:
        archivo.write(str(numero) + '\n')"""

"""archivo.close()"""

# Ejercicio numero 7:
""" Genere un archivo donde esten los datos obtenidos y la condicion del paciente"""

"""def Calculo_IMC(peso,altura):
  # Calculador de IMC devuelve la condicion de una persona.
  calculo = peso / (altura**2)
  if calculo < 18.5:
    return "BAJO PESO"
  elif 18.5 < calculo < 24.9:
    return "PESO NORMAL"
  elif 25 < calculo < 29.9:
    return "SOBREPESO"
  elif 30 < calculo < 34.9:
    return "OBESIDAD TIPO 1"
  elif 35 < calculo < 39.9:
    return "OBESIDAD TIPO 2"
  elif calculo >= 40:
    return "OBESIDAD TIPO 3"

# Programa Cliente:

print("Ingrese el numero de pacientes que quiere en el sistema: ")
n_p = int(input("numero de pacientes: "))

tabla_final= []
for filas in range(n_p):
  nombre= input("Ingrese el nombre: ")
  apellido= input("Ingrese el apellido: ")
  edad= int(input("Ingrese la edad: "))
  dni= int(input("Ingrese el DNI: "))
  peso= float(input("Ingrese el peso: "))
  altura= float(input("Ingrese el altura en m: "))
  condicion = Calculo_IMC(peso,altura)
  tabla_final.append((nombre,apellido,str(edad),str(dni),str(peso),str(altura),condicion))



with open("Datos_pacientes.txt", "w") as archivo:
  for nombre,apellido,edad,dni,peso,altura,condicion in tabla_final:
    archivo.write(nombre+" "+apellido+" "+dni+" "+peso+" "+altura+" "+"su condicion es: "+condicion+"\n")

archivo.close()"""

# Ejercicio numero 8: 

"""def Orden(tabla,dato):
  # Ordena los numero max de una tabla por lista para eso ingresamos la tabla a analizar y el dato o columna a comparar:
  columna_especifica = [(fila[dato],fila) for fila in tabla[1:]] #creamos una lista de los datos y su fila correspondiente.
  columna_especifica.sort(key=lambda x: x[0], reverse=True) #La ordenamos en el orden que querramos
  fila_max_5 = [tupla[1] for tupla in columna_especifica[:5]] #y finalmente extraemos solo la fila que esta ordenadas.
  return fila_max_5  

tabla_covid = []

with open("covid.csv","r") as covid:
  encabezado = covid.readline()
  encabezado = encabezado.rstrip("\n")
  listaencabezado = encabezado.split(sep=",")
  tabla_covid.append(listaencabezado)
  for line in covid:
    linea = line.rstrip("\n")
    fila = linea.split(sep=",")
    pais = fila[0]
    dato1 = int(fila[1])
    dato2 = int(fila[2])
    dato3 = int(fila[3])
    dato4 = int(fila[4])
    tabla_covid.append([pais,dato1,dato2,dato3,dato4])
covid.close()


with open("Ranking5Covid.txt", "w") as papper:
  max_5 = Orden(tabla_covid,4)
  for f in max_5:
    papper.write(f[0] +" "+ str(f[4]) + "\n")
papper.close()"""
  
# Ejercicio numero 9:

"""listado_CP = []

with open("CP.csv","r") as fucking:
  interprete = csv.reader(fucking,delimiter=",")
  for fila in interprete:
        # fila posee separado los datos de cada columna del archivo y 
        # al estar en un ciclo fila tomará los valores de cada fila del arhcivo
        dato0 = int(fila[0])
        dato1 = int(fila[1])
        dato2 = int(fila[2])
        dato3 = int(fila[3])
        listado_CP.append([dato0,dato1,dato2,dato3])

fucking.close()

lista_X_Y = []

with open("Desplazamientos.txt", "w", newline="") as desplazamiento:
  # creamos al escritor del archivo CSV
  escritor = csv.writer(desplazamiento, delimiter=";")
  # Calculamos la posicion
  for fila in listado_CP:
    calculo_x = (433/2)*(((fila[2]+fila[3])-(fila[0]+fila[1]))/(fila[0]+fila[1]+fila[2]+fila[3]))
    calculo_y = (238/2)*(((fila[0]+fila[2])-(fila[1]+fila[3]))/(fila[0]+fila[1]+fila[2]+fila[3]))
    lista_X_Y.append([calculo_x,calculo_y])
  # escribimos toda la lista de datos en varias filas
  escritor.writerows(lista_X_Y)
  
desplazamiento.close()"""

# Ejercicio numero 10: 

"""cantidad_consultas = []

with open("cantidad-consultas-medicas-ambulatorias.csv", "r",encoding="utf-8") as consultas:
  interprete = csv.reader(consultas, delimiter= ",")
  columna = next(interprete)
  for f in interprete:
    id = int(f[0])
    unidad = f[1]
    a13 = int(f[2])
    a14 = int(f[3])
    a15 = int(f[4])
    a16 = int(f[5])
    a17 = int(f[6])
    a18 = int(f[7])
    cantidad_consultas.append([id,unidad,a13,a14,a15,a16,a17,a18])
consultas.close()

# Creamos una tabla que muestre la sumatoria de consultas por año.
registros_por_año = [0 for _ in range(6)]
for c in cantidad_consultas:
  registros_por_año[0] += c[2]
  registros_por_año[1] += c[3]
  registros_por_año[2] += c[4]
  registros_por_año[3] += c[5]
  registros_por_año[4] += c[6]
  registros_por_año[5] += c[7]

tabla_total = [["2013","2014","2015","2016","2017","2018"],registros_por_año]

# Recorremos filas y columnas para obtener los maximos de cada año. 
listaSum=[]
col=len(cantidad_consultas[0])
for c in range(2,8):
      max=0
      nom=''
      for f in range(91):
        if max < cantidad_consultas[f][c]:
          max = cantidad_consultas[f][c]
          nom = cantidad_consultas[f][1]
      listaSum.append([nom,max])

# Recorremos filas y columnas por año para ver que unidades tuvieron menos de 1000 consultas: 
lista1000=[[] for _ in range(6)]
col=len(cantidad_consultas[0])
for c in range(2,8):
      for f in range(91):
        if 1000 > cantidad_consultas[f][c]:
          lista1000[c-2].append(cantidad_consultas[f][1])
for _ in lista1000:
  print(_)

# Creamos un archivo con el top 10 de unidades:

lista_de_totales = []
for filas in range(len(cantidad_consultas)):
  cant = 0
  for c in range(2,8):
    cant += cantidad_consultas[filas][c]
  lista_de_totales.append([cantidad_consultas[filas][1],cant])
  
# Ordenamos la lista de top 10:

lista_de_totales.sort(key=lambda x: x[1] ,reverse=True)

# Creamos el archivo top10.txt:

with open("Top10Consultas.txt", "w") as topcito:
  for lines in lista_de_totales[:10]:
    dato1 = lines[0]
    dato2 = str(lines[1])
    topcito.write(dato1 + " " + dato2 + "\n")
topcito.close()"""

# Ejercicio numero 11:

"""def Condicion_alumno(promedio,n1,n2,n3):
    # La funcion debe de tomar un promedio y verificar si el alumno esta promocionado o libre.
    if promedio < 60:
      return "Libre"
    if promedio >= 80 and n1 >= 75 and n2 >= 75 and n3 >= 75:
      return "Promocionado"
    if promedio >= 60 and n1 >= 60 and n2 >= 60 and n3 >= 60:
      return "Regular"
    else:
      return "Libre"
    

tabla_alumnos = []  
with open("alumnos.txt", "r") as archivo:
  interprete = csv.reader(archivo, delimiter=",")
  encabezado = next(interprete)
  for filas in interprete:
    dni = int(filas[0])
    nombre = filas[1]
    apellido = filas[2]
    nota1 = int(filas[3])
    nota2 = int(filas[4])
    nota3 = int(filas[5])
    tabla_alumnos.append([dni,nombre,apellido,nota1,nota2,nota3])
archivo.close()

tabla_notas = []
for g,b,a,c,c1,c2 in tabla_alumnos:
  prom= (c+c1+c2)/3
  condicion = Condicion_alumno(prom,c,c1,c2) 
  tabla_notas.append([g,b,a,c,c1,c2,round(prom,2),condicion])

tabla_alumnos_final = []
encabezado.extend(["PROMEDIO","CONDICION"])
tabla_alumnos_final.append(encabezado)
for lines in tabla_notas:
  tabla_alumnos_final.append(lines)
  
print(t(tabla_alumnos_final))

with open("alumnos.txt", "w", newline="") as newarchivo:
  escritor = csv.writer(newarchivo,delimiter=",")
  escritor.writerows(tabla_alumnos_final)
newarchivo.close()"""

# Ejercicio numero 12:


tabla_aeroportuaria = []
with open("operaciones_aeroportuarias.csv", "r") as operation:
  interprete = csv.reader(operation, delimiter= ",")
  for _ in interprete:
    tabla_aeroportuaria.append([])