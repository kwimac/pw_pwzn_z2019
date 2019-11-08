"""
Częśćć 1 (1 pkt): Uzupełnij klasę Vector tak,
by reprezentowała wielowymiarowy wektor.
Klasa posiada przeładowane operatory równości, dodawania, odejmowania,
mnożenia (przez liczbę i skalarnego), długości
oraz nieedytowalny (własność) wymiar.
Wszystkie operacje sprawdzają wymiar.
Część 2 (1 pkt): Klasa ma statyczną metodę wylicznia wektora z dwóch punktów
oraz metodę fabryki korzystającą z metody statycznej tworzącej nowy wektor
z dwóch punktów.
Wszystkie metody sprawdzają wymiar.
"""
from operator import add, eq, sub


class Vector:
    _dim = None  # Wymiar wektora

    def __init__(self, *args):
        self.vector = args
        self._dim = len(self.vector)

    @property
    def dim(self):
        return self._dim

    def __len__(self):
        return self.dim

    def __iter__(self):
        return iter(self.vector)

    @property
    def len(self):
        return sum([elem * elem for elem in self.vector]) ** 0.5

    def check_dim(self, other):
        return self.dim == len(other)

    def __eq__(self, other):
        if self.check_dim(other):
            return all(map(eq, self.vector, other))

    def __add__(self, other):
        if self.check_dim(other):
            return self.__class__(*list(map(add, self.vector, other)))

    def __sub__(self, other):
        if self.check_dim(other):
            return self.__class__(*list(map(sub, self.vector, other)))

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(*[other * elem for elem in self.vector])
        if self.check_dim(other):
            return sum(x * y for x, y in zip(self.vector, other))

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
        if len(beg) == len(end):
            return tuple(y-x for x, y in zip(beg, end))

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
        return cls(*cls.calculate_vector(beg, end))


if __name__ == '__main__':
    v1 = Vector(1, 2, 3)
    v2 = Vector(1, 2, 3)
    assert v1 + v2 == Vector(2, 4, 6)
    assert v1 - v2 == Vector(0, 0, 0)
    assert v1 * 2 == Vector(2, 4, 6)
    assert v1 * v2 == 14
    assert len(Vector(3, 4)) == 2
    assert Vector(3, 4).dim == 2
    assert Vector(3, 4).len == 5.
    assert Vector.calculate_vector([0,  0,  0], [1, 2, 3]) == (1, 2, 3)
    assert Vector.from_points([0,  0,  0], [1, 2, 3]) == Vector(1, 2, 3)
