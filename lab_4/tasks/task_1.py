"""
Część 1 (1 pkt): Uzupełnij klasę Calculator
tak by obsługiwała podstawowe operacje (podane jako string)
oraz pamięć (memory, atrybut klasy) z interfejsem: dodaj do pamięci , wyczyść pamięć.
Atrybut memory ma być nienadpisywalny.
Część 2 (1 pkt): jeżeli drugi argument działania nie jest podany (None)
użyj wartość z pamięci kalkulatora. Obsłuż przypadki skrajne.
"""


class Calculator:
    def __init__(self):
        self.__memory = None
        self.operation_dict = {'+': self.__add__, '-': self.__sub__, '*': self.__mul__, '/': self.__divmod__}
        self.__short_memory = None

    def __add__(self, arg1, arg2):
        return arg1 + arg2

    def __sub__(self, arg1, arg2):
        return arg1 - arg2

    def __mul__(self, arg1, arg2):
        return arg1 * arg2

    def __divmod__(self, arg1, arg2):
        return arg1 / arg2

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
        if self.operation_dict.get(operator):
            if type(arg1) is float or int:  # sprawdzanie czy arg1 jest intem lub floatem
                if arg2 is None and self.__short_memory is not None:  # jeśli arg2 to none a pamięć nie jest pusta
                    if self.__short_memory == 0 and operator == '/':  # jeśli operacja to dzielenie i w pamięci jest 0 to błąd
                        print("Memorized number is 0. You can't divide by 0!")
                    else:  # w innym przypadku zapisz do pamieci tymczasowej
                        self.__short_memory = self.operation_dict.get(operator)(arg1, self.__short_memory)
                elif arg2 is not None and (type(arg2) is float or int):  # jeśli arg2 nie jest nonem i arg2 jest floatem lub intem
                    if arg2 == 0 and operator == '/':  # jeśli operacja to dzielenie i w pamięci jest 0 to błąd
                        print("You can't divide by 0!")
                    else:  # w innym przypadku zapisz do pamieci tymczasowej
                        self.__short_memory = self.operation_dict.get(operator)(arg1, arg2)
                else:
                    print("arg2 is not a number or nothing in memory!")
            else:
                print("arg1 is not a number!")
            return self.__short_memory

    def memorize(self):
        self.__memory = self.__short_memory

    def clean_memory(self):
        """Cleans memorized value"""
        self.__memory = None

    def in_memory(self):
        """Prints memorized value."""
        print(f"Zapamiętana wartość: {self.__memory}")


if __name__ == '__main__':
    calc = Calculator()
    b = calc.run('+', 1, 2)
    calc.memorize()
    calc.in_memory()
    c = calc.run('/', 9)
    assert c == 3
