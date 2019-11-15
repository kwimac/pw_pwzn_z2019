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

import math


class Figure:
    area = None
    perimeter = None

    @staticmethod
    def get_area(**kwargs):
        raise NotImplemented

    @staticmethod
    def get_perimeter(**kwargs):
        raise NotImplemented

    def __str__(self):
        return (
            f'{self.name()}: area={self.area:.3f}, '
            f'perimeter={self.perimeter:.3f}'
        )

    @classmethod
    def name(cls):
        return cls.__name__


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    @staticmethod
    def get_area(r):
        return math.pi * r ** 2

    @property
    def area(self):
        return self.get_area(self.r)

    @staticmethod
    def get_perimeter(r):
        return 2 * math.pi * r

    @property
    def perimeter(self):
        return self.get_perimeter(self.r)


class Diamond(Figure):
    def __init__(self, e, f):
        self.e = e
        self.f = f

    @property
    def area(self):
        return self.get_area(self.e, self.f)

    @staticmethod
    def get_area(e, f):
        return e * f / 2

    @property
    def perimeter(self):
        return self.get_perimeter(self.e, self.f)

    @staticmethod
    def get_perimeter(e, f):
        return 2 * math.sqrt(e ** 2 + f ** 2)

    def are_diagonals_equal(self):
        return self.e == self.f

    def to_square(self):
        if self.are_diagonals_equal():
            return(Square.create_from_diagonal(self.e))


class Rectangle(Figure):
    def __init__(self, a, b, *args, **kwargs):
        self.a = a
        self.b = b

    @staticmethod
    def get_area(a, b):
        return a * b

    @property
    def area(self):
        return self.get_area(self.a, self.b)

    @staticmethod
    def get_perimeter(a, b):
        return 2 * (a + b)

    @property
    def perimeter(self):
        return self.get_perimeter(self.a, self.b)


class Square(Rectangle, Diamond):
    _side = None
    _diagonal = None

    def __init__(self, a, *_, **__):
        e = f = self._side_to_diagonal(a)
        super().__init__(a, a)
        Diamond.__init__(self, e, f)

    @staticmethod
    def get_area(a, *_, **__):
        return a * a

    # korzystając z dziedziczenia:
    # @classmethod
    # def get_area(cls, a, *_, **__):
    #     return Rectangle.get_area(a, a)

    @staticmethod
    def get_perimeter(a, *_, **__):
        return 4 * a

    # korzystając z dziedziczenia:
    # @classmethod
    # def get_perimeter(cls, a, *_, **__):
    #     return Rectangle.get_perimeter(a, a)

    # Wersja na 1 pkt
    # @property
    # def b(self):
    #     return self.a
    #
    # @b.setter
    # def b(self, b):
    #     self.a = b

    @staticmethod
    def _diagonal_to_side(diagonal):
        return diagonal / 2 * math.sqrt(2)

    @staticmethod
    def _side_to_diagonal(side):
        return side * math.sqrt(2)

    def _update_params_from_side(self, a):
        self._side = a
        self._diagonal = self._side_to_diagonal(a)

    a = b = property(lambda self: self._side, _update_params_from_side)

    def _update_params_from_diagonal(self, e):
        self._side = self._diagonal_to_side(e)
        self._diagonal = e

    e = f = property(lambda self: self._diagonal, _update_params_from_diagonal)

    @classmethod
    def create_from_diagonal(cls, e):
        return cls(cls._diagonal_to_side(e))


if __name__ == '__main__':
    circle_1 = Circle(1)
    assert str(circle_1) == 'Circle: area=3.142, perimeter=6.283'

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
