"""
Uzupełnij klasę Calculator tak by obsługiwała podstawowe operacje (podane jako string)
oraz pamięć (atrybut klasy) z interfejsem: dodaj do pamięci (memory), wyczyść pamięć.
Atrybut memory ma być nienadpisywalny (1 pkt).
Część 2: jeżeli drugi argument działania nie jest podany (None)
użyj wartość z pamięci kalkulatora. Obłsuż przypadki skrajne. (1 pkt)
"""
from operator import add, mul, sub, truediv


class Calculator:
    operations = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv,
    }

    def __init__(self):
        self._memory = None
        self._short_memory = None

    def run(self, operator, arg1, arg2=None):
        """
        Returns result of given operation.

        :param operator: sign of operation to perform
        :type operator: str
        :param arg1: first argument, must be a numeric value
        :type arg1: float
        :param arg2: optional, second argument, must be a numeric value
        :type arg2: float
        :return: result of operation
        :rtype: float
        """
        if operator in self.operations:
            arg2 = arg2 or self.memory
            if arg2:
                self._short_memory = self.operations[operator](arg1, arg2)
                return self._short_memory

    @property
    def memory(self):
        return self._memory

    def memorize(self):
        """Saves last operation result to memory."""
        self._memory = self._short_memory

    def clean_memory(self):
        """Cleans memorized value"""
        self._memory = None

    def in_memory(self):
        """Prints memorized value."""
        print(f"Zapamiętana wartość: {self.memory}")


if __name__ == '__main__':
    calc = Calculator()
    b = calc.run('+', 1, 2)
    calc.memorize()
    calc.in_memory()
    c = calc.run('/', 9)
    assert c == 3