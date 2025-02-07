"""Implementar una clase que modele a un cuadrado. El único atributo que posee es su lado.
 Dotar de operaciones al Cuadrado para ingresar el lado, mostrarlo, calcular y mostrar el
 área, calcular y mostrar el perímetro.
 Evaluar los métodos donde es necesario hacer una validación de datos e implementar."""

"""from re import X
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
    print(f"Perímetro del cuadrado: {cuadrado.perimetro()}")"""

"""Implementar una clase que modele un punto compuesto por dos coordenadas ‘x’ y ‘y’. El
 punto debe contar con operaciones para: proporcionar un valor al punto al momento de
 instanciarlo, proporcionar valores a sus atributos y para retornarlos.
 Evaluar los métodos donde es necesario hacer una validación de datos e implementar."""
 
"""class Punto:
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
    print(f"Coordenada y: {puntoA.get_y()}")"""

"""Implementar la clase Persona. Una persona posee un nombre y un apellido. La clase debe
 asegurarse que sus campos estén capitalizados y los mismos (campos o atributos) deben
 estar “ocultos”.
 Añadir métodos setters y getters. Opcional: Utilizar propiedades (property) para ocultar
 setters y getters.
 Crear una unidad de prueba para validar tipo de datos"""

"""class Persona:
    def __init__(self,nombre,apellido):
        self.__name = nombre.capitalize()
        self.__surname = apellido.capitalize()
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip():  # Validación simple
            self.__name = nuevo_nombre.strip().capitalize()
        else:
            raise ValueError("El nombre debe ser una cadena de texto no vacía.")

    @property
    def surname(self):
        return self.__surname
    
    @surname.setter
    def surname(self,new_surname):
        if isinstance(new_surname,str) and new_surname.strip():
            self.__surname = new_surname.strip().capitalize()
        else:
            raise ValueError("El apellido debe ser una cadena de texto no vacia.")

import unittest

class TestPersona(unittest.TestCase):
    def test_nombre_correcto(self):
        p = Persona("lucas", "gabirondo")
        self.assertEqual(p.name, "Lucas")
        self.assertEqual(p.surname, "Gabirondo")

    def test_setter_nombre_valido(self):
        p = Persona("lucas", "gabirondo")
        p.name = "maria"
        self.assertEqual(p.name, "Maria")

    def test_setter_apellido_valido(self):
        p = Persona("lucas", "gabirondo")
        p.surname = "lopez"
        self.assertEqual(p.surname, "Lopez")

    def test_nombre_invalido(self):
        p = Persona("lucas", "gabirondo")
        with self.assertRaises(ValueError):
            p.name = ""  # Vacío

        with self.assertRaises(ValueError):
            p.name = 123  # No es string

    def test_apellido_invalido(self):
        p = Persona("lucas", "gabirondo")
        with self.assertRaises(ValueError):
            p.surname = " "  # Solo espacios

        with self.assertRaises(ValueError):
            p.surname = None  # No es string

if __name__ == '__main__':
    unittest.main()"""





    

 