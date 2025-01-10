"""Implementar una clase que modele a un cuadrado. El único atributo que posee es su lado.
 Dotar de operaciones al Cuadrado para ingresar el lado, mostrarlo, calcular y mostrar el
 área, calcular y mostrar el perímetro.
 Evaluar los métodos donde es necesario hacer una validación de datos e implementar."""

from tabulate import tabulate


class cuadrado:
    def __init__(self):
        self.a = 0

    def ingresar(self):
        numero = int(input("Agrega un numero para crear el cuadrado= "))
        self.a = numero
        return print(self.a)
    
    def mostrar(self):
        tabla = []
        for i in range(self.a):
            fila = []
            for j in range(self.a):
                fila.append("x")
            tabla.append(fila)
        return tabulate(tabla)
        # return [["x" for _ in range(self.a)] for _ in range(self.a)]
    

    def calcular(self):
        pass

    def area(self):
        pass

    def perimetro():
        pass

if __name__ == "__main__":
    main = cuadrado()
    main.ingresar()
    print(main.mostrar())