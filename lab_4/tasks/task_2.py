"""
Część 1 (1 pkt): Uzupełnij klasę Vector tak by reprezentowała wielowymiarowy wektor.
Klasa posiada przeładowane operatory równości, dodawania, odejmowania,
mnożenia (przez liczbę i skalarnego), długości
oraz nieedytowalny (własność) wymiar.
Wszystkie operacje sprawdzają wymiar.
Część 2 (1 pkt): Klasa ma statyczną metodę wylicznia wektora z dwóch punktów
oraz metodę fabryki korzystającą z metody statycznej tworzącej nowy wektor
z dwóch punktów.
Wszystkie metody sprawdzają wymiar.
"""

class Vector:
    dim = None  # Wymiar vectora
<<<<<<< HEAD
    wektor = []
=======

    @property
    def len(self):
        raise NotImplemented

>>>>>>> 4a64558c0bcc8053aae90920f772adaa1835a65b
    def __init__(self, *args):

        self.args = args

        if len(args) == 1:
            Vector.dim = 1
        elif len(args) == 2:
            Vector.dim = 2
        elif len(args) == 3:
            Vector.dim = 3
        elif len(args) > 3:
            print('Maksymalna liczba wymiarow = 3 !')

    def __add__(self, other):

        koncowy_wektor = []

        if Vector.dim == 1:
            arg1 = self.args[0] + other.args[0]
            koncowy_wektor.append(arg1)
            return Vector(koncowy_wektor)
        elif Vector.dim == 2:
            arg1 = self.args[0] + other.args[0]
            koncowy_wektor.append(arg1)
            arg2 = self.args[1] + other.args[1]
            koncowy_wektor.append(arg2)
            return Vector(koncowy_wektor)
        elif Vector.dim == 3:
            arg1 = self.args[0] + other.args[0]
            koncowy_wektor.append(arg1)
            arg2 = self.args[1] + other.args[1]
            koncowy_wektor.append(arg2)
            arg3 = self.args[2] + other.args[2]
            koncowy_wektor.append(arg3)
            print(Vector(koncowy_wektor))
            print(Vector(2,4,6))
            return Vector(koncowy_wektor)

    def __sub__(self, other):

        koncowy_wektor = []

        if Vector.dim == 1:
            arg1 = self.args[0] - other.args[0]
            koncowy_wektor.append(arg1)
            return Vector(koncowy_wektor)
        elif Vector.dim == 2:
            arg1 = self.args[0] - other.args[0]
            koncowy_wektor.append(arg1)
            arg2 = self.args[1] - other.args[1]
            koncowy_wektor.append(arg2)
            return Vector(koncowy_wektor)
        elif Vector.dim == 3:
            arg1 = self.args[0] - other.args[0]
            koncowy_wektor.append(arg1)
            arg2 = self.args[1] - other.args[1]
            koncowy_wektor.append(arg2)
            arg3 = self.args[2] - other.args[2]
            koncowy_wektor.append(arg3)
            # print(Vector(koncowy_wektor))
            # print(Vector(0,0,0))
            return Vector(koncowy_wektor)

    def __mul__(self, other):

        if type(other) != int:
            if Vector.dim == 1:
                arg1 = self.args[0] * other.args[0]
                return arg1
            elif Vector.dim == 2:
                arg1 = (self.args[0] * other.args[0]) + (self.args[1] * other.args[1])
                return arg1
            elif Vector.dim == 3:
                arg1 = (self.args[0] * other.args[0]) + (self.args[1] * other.args[1]) + (self.args[2] * other.args[2])
                # print(arg1)
                return arg1

        if type(other) == int:

            koncowy_wektor = []

            if Vector.dim == 1:
                arg1 = self.args[0] * other
                koncowy_wektor.append(arg1)
                return Vector(koncowy_wektor)
            elif Vector.dim == 2:
                arg1 = (self.args[0] * other)
                koncowy_wektor.append(arg1)
                arg2 = (self.args[1] * other)
                koncowy_wektor.append(arg2)
                return Vector(arg1, arg2)
            elif Vector.dim == 3:
                arg1 = (self.args[0] * other)
                koncowy_wektor.append(arg1)
                arg2 = (self.args[1] * other)
                koncowy_wektor.append(arg2)
                arg3 = (self.args[2] * other)
                koncowy_wektor.append(arg3)
                # print(Vector(koncowy_wektor))
                # print(Vector(2,4,6))
                return Vector(koncowy_wektor)

    def __len__(self):

        import math

        if Vector.dim == 1:
            return int(self.args[0])
        elif Vector.dim == 2:
            return int(math.sqrt(int(self.args[0]) ** 2 + int(self.args[1]) ** 2))
        elif Vector.dim == 3:
            return int(math.sqrt(int(self.args[0]) ** 2 + int(self.args[1]) ** 2 + int(self.args[2]) ** 2))

    @staticmethod
    def calculate_vector(beg, end):
        """
        Calculate vector from given points
        :param beg: Begging point
        :type beg: list, tuple
        :param end: End point
        :type end: list, tuple
        :return: Calculated vector
        :rtype: tuple
        """

        if len(beg) == 1:
            arg1 = end[0] - beg[0]
            Vector.wektor = (arg1)
            return Vector.wektor
        elif len(beg) == 2:
            arg1 = end[0] - beg[0]
            arg2 = end[1] - beg[1]
            Vector.wektor = (arg1, arg2)
            return Vector.wektor
        elif len(beg) == 3:
            arg1 = end[0] - beg[0]
            arg2 = end[1] - beg[1]
            arg3 = end[2] - beg[2]
            Vector.wektor = (arg1, arg2, arg3)
            return Vector.wektor

    @classmethod
    def from_points(cls, beg, end):
        """
        Generate vector from given points.
        :param beg: Begging point
        :type beg: list, tuple
        :param end: End point
        :type end: list, tuple
        :return: New vector
        :rtype: tuple
        """

        Vector.calculate_vector(beg, end)
        return Vector(wektor)

if __name__ == '__main__':
    # Moj kod wyrzuca bład tylko w momencie returnowania wektora, ale szczerze mówiąc nie mam pojecia dlaczego :(
    # Jezeli wyprintuje się otrzymany przeze mnie wektor i wektor z asssertu, ktory teoretycznie powinien powstawac
    # dla obu przypadkow dostaje sie to samo: np. linijki 50 i 51: <__main__.Vector object at 0x01454190>.
    # Wynikaloby z tego ze to ten sam wektor, jednak wciaz pojawia sie AssertionError.
    v1 = Vector(1,2,3)
    v2 = Vector(1,2,3)
    assert v1 + v2 == Vector(2,4,6)
    assert v1 - v2 == Vector(0,0,0)
    assert v1 * 2 == Vector(2,4,6)
    assert v1 * v2 == 14
    assert len(Vector(3,4)) == 2
    assert Vector(3,4).dim == 2
    assert Vector(3,4).len == 5.
    assert Vector.calculate_vector([0, 0, 0], [1,2,3]) == (1,2,3)
    assert Vector.from_points([0, 0, 0], [1,2,3]) == Vector(1,2,3)
