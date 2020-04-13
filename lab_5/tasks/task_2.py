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
import numbers
import math


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
    __r = None

    def __init__(self, r):
        self.__r = r

    def get_r(self):
        return self.__r

    def set_r(self, r):
        if not isinstance(r, numbers.Number):
            print("Not number value!")
        else:
            self.__r = r

    r = property(get_r, set_r)

    @property
    def area(self):
        return math.pi * self.r ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.r

    @staticmethod
    def get_area(r):
        return math.pi * r ** 2

    @staticmethod
    def get_perimeter(r):
        return 2 * math.pi * r


class Rectangle(Figure):
    __a = None
    __b = None

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_a(self):
        return self.__a

    def set_a(self, a):
        if not isinstance(a, numbers.Number):
            print("Not number value!")
        else:
            self.__a = a

    def get_b(self):
        return self.__b

    def set_b(self, b):
        if not isinstance(b, numbers.Number):
            print("Not number value!")
        else:
            self.__b = b

    a = property(get_a, set_a)
    b = property(get_b, set_b)

    @property
    def area(self):
        return self.a * self.b

    @property
    def perimeter(self):
        return 2 * (self.a + self.b)

    @staticmethod
    def get_area(a, b):
        return a * b

    @staticmethod
    def get_perimeter(a, b):
        return 2 * (a + b)


class Diamond(Figure):
    __e = None
    __f = None

    def __init__(self, e, f):
        self.e = e
        self.f = f

    def get_e(self):
        return self.__e

    def set_e(self, e):
        if not isinstance(e, numbers.Number):
            print("Not number value!")
        else:
            self.__e = e

    def get_f(self):
        return self.__f

    def set_f(self, f):
        if not isinstance(f, numbers.Number):
            print("Not number value!")
        else:
            self.__f = f

    e = property(get_e, set_e)
    f = property(get_f, set_f)

    @property
    def area(self):
        return (self.e * self.f) / 2

    @property
    def perimeter(self):
        return 4 * math.sqrt(((self.e) / 2) ** 2 + ((self.f) / 2) ** 2)

    def are_diagonals_equal(self):
        return self.e == self.f

    def to_square(self):
        if self.are_diagonals_equal():
            a_calculated = self.f / math.sqrt(2)
            sq = Square(a_calculated)
            return sq
        else:
            return None


class Square(Rectangle, Diamond):
    def __init__(self, a):
        super().__init__(a, a)
        self.e = math.sqrt(2)*a
        self.f = self.e

    def get_a(self):
        return self.__a

    def set_a(self, a):
        if not isinstance(a, numbers.Number):
            print("Not number value!")
        else:
            self.__a = a
            self.__b = a

    def get_b(self):
        return self.__b

    def set_b(self, b):
        if not isinstance(b, numbers.Number):
            print("Not number value!")
        else:
            self.__b = b
            self.__a = b

    a = property(get_a, set_a)
    b = property(get_b, set_b)

    @staticmethod
    def get_area(a):
        return a ** 2

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