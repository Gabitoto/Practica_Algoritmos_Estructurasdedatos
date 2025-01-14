"""Implementar una clase que modele a un cuadrado. El único atributo que posee es su lado.
 Dotar de operaciones al Cuadrado para ingresar el lado, mostrarlo, calcular y mostrar el
 área, calcular y mostrar el perímetro.
 Evaluar los métodos donde es necesario hacer una validación de datos e implementar."""

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