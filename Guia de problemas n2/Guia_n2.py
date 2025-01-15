"""Implementar una clase que modele a un cuadrado. El único atributo que posee es su lado.
 Dotar de operaciones al Cuadrado para ingresar el lado, mostrarlo, calcular y mostrar el
 área, calcular y mostrar el perímetro.
 Evaluar los métodos donde es necesario hacer una validación de datos e implementar."""

from re import X
from tabulate import tabulate

class Cuadrado:
    def __init__(self):
        self.lado = 0

    def ingresar(self):
        while True:
            try:
                numero = int(input("Agrega un número positivo para crear el cuadrado: "))
                if numero > 0:
                    self.lado = numero
                    break
                else:
                    print("El número debe ser positivo.")
            except ValueError:
                print("Por favor, ingresa un número entero válido.")

    def mostrar(self):
        tabla = [["x" for _ in range(self.lado)] for _ in range(self.lado)]
        return tabulate(tabla, tablefmt="plain")

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

if __name__ == "__main__":
    cuadrado = Cuadrado()
    cuadrado.ingresar()
    print("\nRepresentación del cuadrado:")
    print(cuadrado.mostrar())
    print(f"\nÁrea del cuadrado: {cuadrado.area()}")
    print(f"Perímetro del cuadrado: {cuadrado.perimetro()}")

"""Implementar una clase que modele un punto compuesto por dos coordenadas ‘x’ y ‘y’. El
 punto debe contar con operaciones para: proporcionar un valor al punto al momento de
 instanciarlo, proporcionar valores a sus atributos y para retornarlos.
 Evaluar los métodos donde es necesario hacer una validación de datos e implementar."""
 
class Punto:
    def __init__(self, x=0, y=0):
        self.set_x(x)
        self.set_y(y)

    def set_x(self, x):
        if isinstance(x, (int, float)):
            self.x = x
        else:
            raise ValueError("La coordenada x debe ser un número.")

    def set_y(self, y):
        if isinstance(y, (int, float)):
            self.y = y
        else:
            raise ValueError("La coordenada y debe ser un número.")

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def ingresar(self):
        while True:
            try:
                x = float(input("Agrega un número para la coordenada x: "))
                y = float(input("Agrega un número para la coordenada y: "))
                self.set_x(x)
                self.set_y(y)
                print(f"Las coordenadas son: ({self.x}, {self.y})")
                break
            except ValueError:
                print("Por favor, ingresa números válidos.")

if __name__ == "__main__":
    puntoA = Punto()
    puntoA.ingresar()
    print(f"Coordenada x: {puntoA.get_x()}")
    print(f"Coordenada y: {puntoA.get_y()}")
