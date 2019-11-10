from math import pi

"""
Na (1 pkt.):
- Zaimplementuj klasy: Rectangle, Square, Circle dziedziczące z klasy Figure
oraz definiujące jej metody:
    - Rectangle powinien mieć dwa atrybuty odpowiadające bokom (a i b)
    - Klasa Square powinna dziedziczyć z Rectangle.
    - Circle ma posiadać tylko atrybut r (radius).
- Przekształć metody we własności (properties).
---------
Na (2 pkt.):
- Zwiąż ze sobą boki a i b klasy Square (tzn. modyfikacja boku a lub boku b
powinna ustawiać tę samą wartość dla drugiego atrybutu).
- Zaimplementuj metody statyczne pozwalające na obliczenie pola
figury na podstawie podanych parametrów.
- Zaimplementuj classmethod "name" zwracającą nazwę klasy.
---------
Na (3 pkt.):
- Zaimplementuj klasę Diamond (romb) dziedziczącą z Figure,
po której będzie dziedziczyć Square,
tzn. Square dziediczy i z Diamond i Rectangle.
- Klasa wprowadza atrybuty przekątnych (e i f) oraz metody:
-- are_diagonals_equal: sprawdź równość przekątnych,
-- to_square: po sprawdzeniu równości przekątnych zwróci instancję
klasy Square o takich przekątnych.
- Zwiąż ze sobą atrybuty e i f (w klasie Diamond) oraz a, b, e i f
(w klasie Square)
"""
from unittest.test.test_result import __init__


class Figure:

    @ property
    def area(self):
        raise NotImplementedError

    @property
    def perimeter(self):
        raise NotImplementedError

    @property
    def name(self):
        raise NotImplementedError

    def __str__(self):
        return (
            f'{self.name}: area={self.area:.3f}, '
            f'perimeter={self.perimeter:.3f}'
        )


class Circle(Figure):
    radius = None
    @property
    def r(self):
        return self.radius

    def __init__(self,r):
        self.radius = r

    @property
    def perimeter(self):
        return 2 * pi * self.r

    @property
    def name(self):
        return "Circle"

    @property
    def area(self):
        return pi * self.r**2

    def __str__(self):
        return (super().__str__())





class Rectangle(Figure):
    bokA = None
    bokB = None

    def __init__(self,a,b):
        self.bokA = a
        self.bokB = b

    @property
    def a(self):
        return self.bokA

    @property
    def b(self):
        return self.bokB

    @property
    def perimeter(self):
        return 2 * self.a + 2 * self.b

    @property
    def name(self):
        return "Rectangle"




class Square(Rectangle):

    def __init__(self,a):
        self.bokA = a
        self.bokB = a




class Diamond:
    pass


if __name__ == '__main__':
    kolo1 = Circle(1)

    print(str(kolo1))
    assert str(kolo1) == 'Circle: area=3.142, perimeter=6.283'

    rec_1 = Rectangle(2, 4)
    assert str(rec_1) == 'Rectangle: area=8.000, perimeter=12.000'

    # print("Square")
    sqr_1 = Square(4)
    assert str(sqr_1) == 'Square: area=8.000, perimeter=16.000'

    diam_1 = Diamond(6, 8)
    assert str(diam_1) == 'Diamond: area=24.000, perimeter=20.000'

    diam_2 = Diamond(1, 1)
    assert str(diam_2) == 'Diamond: area=0.500, perimeter=2.828'

    sqr_3 = diam_2.to_square()
    assert str(diam_2) == 'Square: area=0.500, perimeter=2.828'