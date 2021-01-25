"""
Na (1 pkt.):
- Zaimplementuj klasy: Rectangle, Square, Circle dziedziczące z klasy Figure
oraz definiujące jej metody:
    - Rectangle powinien mieć dwa atrybuty odpowiadające bokom (a i b)
    - Klasa Square powinna dziedziczyć z Rectangle.
    - Circle ma posiadać tylko atrybut r (radius).
- Przekształć metody area i perimeter we własności (properties).
---------
Na (2 pkt.):
- Zwiąż ze sobą boki a i b klasy Square (tzn. modyfikacja boku a lub boku b
powinna ustawiać tę samą wartość dla drugiego atrybutu).
- Zaimplementuj metody statyczne pozwalające na obliczenie
pola (get_area) i obwodu (get_perimeter) figury
na podstawie podanych parametrów.
- Zaimplementuj classmethod "name" zwracającą nazwę klasy.
---------
Na (3 pkt.):
- Zaimplementuj klasę Diamond (romb) dziedziczącą z Figure,
po której będzie dziedziczyć Square,
tzn. Square dziediczy i z Diamond i Rectangle.
- Klasa wprowadza atrybuty przekątnych (e i f) oraz metody:
-- are_diagonals_equal: sprawdź równość przekątnych,
-- to_square: po sprawdzeniu równości przekątnych zwróci instancję
klasy Square o takich przekątnych lub None (jeżeli przekątne nie są równe).
- Zwiąż ze sobą atrybuty a, b, e i f w klasie Square.
"""

from math import pi, sqrt
from numbers import Number

class Figure:
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    @classmethod
    def name(cls):
        return cls.__name__

    def __str__(self):

        return (
            f'{self.name()}: area={self.area:.3f}, '
            f'perimeter={self.perimeter:.3f}'
        )


class Circle(Figure):

    def __init__(self, r):
        self.r = r

    @property
    def area(self):
        return pi * self.r * self.r

    @property
    def perimeter(self):
        return 2 * pi * self.r

    @staticmethod
    def get_area(r):
        return pi * r * r

    @staticmethod
    def get_perimeter(r):
        return 2 * pi * r

class Rectangle(Figure):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    @property
    def perimeter(self):
        return 2 * self.a + 2 * self.b

    @staticmethod
    def get_area(a, b):
        return a * b

    @staticmethod
    def get_perimeter(a, b):
        return 2 * a + 2 * b


class Diamond(Figure):

    def __init__(self, e, f):
        self.e = e
        self.f = f

    @property
    def area(self):
        return (self.e * self.f)/2

    @property
    def perimeter(self):
        return 4 * sqrt(((self.e/2)**2 + (self.f/2)**2))

    def are_diagonals_equal(self):
        return self.e == self.f

    def to_square(self):
        if self.are_diagonals_equal() is True:
            return (Square(self.e / sqrt(2)))
        else:
            return None

    @staticmethod
    def get_area(e, f):
        return (e * f)/2

    @staticmethod
    def get_perimeter(e, f):
        return 4 * sqrt(((e/2)**2 + (f/2)**2))


class Square(Rectangle, Diamond):

    def __init__(self, a):
        self.a = a
        self.b = self.a
        self.e = self.a * sqrt(2)
        self.f = self.e

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        if not isinstance(a, Number):
            print("Not number value!")
        else:
            self.__a = a
            self.__b = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        if not isinstance(b, Number):
            print("Not number value!")
        else:
            self.__a = b
            self.__b = b

    @staticmethod
    def get_area(a):
        return a * a

    @staticmethod
    def get_perimeter(a):
        return 4 * a


if __name__ == '__main__':
    kolo1 = Circle(1)
    assert str(kolo1) == 'Circle: area=3.142, perimeter=6.283'

    rec_1 = Rectangle(2, 4)
    assert str(rec_1) == 'Rectangle: area=8.000, perimeter=12.000'

    # print("Square")
    sqr_1 = Square(4)
    assert str(sqr_1) == 'Square: area=16.000, perimeter=16.000'

    diam_1 = Diamond(6, 8)
    assert str(diam_1) == 'Diamond: area=24.000, perimeter=20.000'

    diam_2 = Diamond(1, 1)
    assert str(diam_2) == 'Diamond: area=0.500, perimeter=2.828'

    sqr_3 = diam_2.to_square()
    assert str(sqr_3) == 'Square: area=0.500, perimeter=2.828'