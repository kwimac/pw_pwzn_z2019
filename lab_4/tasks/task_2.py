"""
Częśćć 1 (1 pkt): Uzupełnij klasę Vector tak by reprezentowała wielowymiarowy wektor.
Klasa posiada przeładowane operatory równości, dodawania, odejmowania,
mnożenia (przez liczbę i skalarnego), długości
oraz nieedytowalny (własność) wymiar.
Wszystkie operacje sprawdzają wymiar.
Część 2 (1 pkt): Klasa ma statyczną metodę wylicznia wektora z dwóch punktów
oraz metodę fabryki korzystającą z metody statycznej tworzącej nowy wektor
z dwóch punktów.
Wszystkie metody sprawdzają wymiar.
"""
import math


def check_dim(dim1, dim2):
    try:
        if dim1 is not dim2:
            raise ValueError
        else:
            return True
    except ValueError:
        print("Niezgodność wymiarów wektorów")


class Vector:
    dim = None  # Wymiar vectora
    def __init__(self, *args):
        self.vector = tuple(args)
        self.__dim = len(self.vector)

    @property
    def dim(self):
        return self.__dim

    def __add__(self, arg1):
        output_vector = []
        if check_dim(self.dim, arg1.dim):
            for i in range(0, self.dim):
                output_vector.append(self.vector[i] + arg1.vector[i])
        return Vector(*output_vector)

    def __sub__(self, arg1):
        output_vector = []
        if check_dim(self.dim, arg1.dim):
            for i in range(0, self.dim):
                output_vector.append(self.vector[i] - arg1.vector[i])
        return Vector(*output_vector)

    def __mul__(self, arg1):
        if isinstance(arg1, int) or isinstance(arg1, float):
            output_vector = [element * arg1 for element in self.vector]
            return Vector(*output_vector)
        else:
            multiplication = 0.0
            if check_dim(self.dim, arg1.dim):
                for i in range(0, self.dim):
                    multiplication += self.vector[i] * arg1.vector[i]
            return multiplication

    def __eq__(self, arg2):
        return self.dim == arg2.dim and self.vector == arg2.vector

    def __len__(self):
        output_len = 0.0
        for element in self.vector:
            output_len += element ** 2

        return int(math.sqrt(output_len))

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
        output_vector = []
        if check_dim(len(beg), len(end)):
            for i in range(0, len(beg)):
                output_vector.append(end[i] - beg[i])
        return tuple(output_vector)

    @classmethod
    def from_points(cls, beg, end):
        """"""
        """
        Generate vector from given points.

        :param beg: Begging point
        :type beg: list, tuple
        :param end: End point
        :type end: list, tuple
        :return: New vector
        :rtype: tuple
        """
        vector = cls.calculate_vector(beg, end)
        return Vector(*vector)


if __name__ == '__main__':
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
