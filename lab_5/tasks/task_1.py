"""
Uzupełnij klasę Calculator o obsługę wyjątków (1pkt).
Podnoszone wyjątki:
- błędna operacja - WrongOperation
- błędne argumenty (nie liczba) - NotNumberArgument
- pusta pamięć (zarówno przy pytaniu o pamięć
jak i operację z argumentem domyślnym) - EmptyMemory
- dzielenie przez zero jest przekształcane w CalculatorError
"""
from operator import add, mul, sub, truediv
import numbers


class CalculatorError(Exception):
    def __init__(self, error_information=None):
        print(f'Wystąpił błąd : {error_information}')


class WrongOperation(CalculatorError):
    def __init__(self):
        super().__init__('Nie jest dostępna taka operacja!')


class NotNumberArgument(CalculatorError):
    def __init__(self):
        super().__init__('Błędny argument - podany argument nie jest liczbą!')


class EmptyMemory(CalculatorError):
    def __init__(self):
        super().__init__('Pusta pamięć!')


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
        if operator not in self.operations:
            raise WrongOperation
        if arg2 is None:
            arg2 = self.memory
        if arg2 is None:
            raise EmptyMemory
        if not isinstance(arg2, numbers.Number):
            raise NotNumberArgument
        if not isinstance(arg1, numbers.Number):
            raise NotNumberArgument
        try:
            self._short_memory = self.operations[operator](arg1, arg2)
        except ZeroDivisionError as exc:
            raise CalculatorError('Dzielenie przez 0!') from exc
        else:
            return self._short_memory

        # except (WrongOperation, EmptyMemory, NotNumberArgument):
        #     return None

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
        if not self.memory:
            raise EmptyMemory
        print(f"Zapamiętana wartość: {self.memory}")


if __name__ == '__main__':
    b = None
    calc = Calculator()

    try:
        b = calc.run('+', 1, 'a')
    except CalculatorError as exc:
        assert type(exc) == NotNumberArgument
        assert b is None

    try:
        b = calc.run('^', 2, 3)
    except CalculatorError as exc:
        assert type(exc) == WrongOperation
        assert b is None

    try:
        calc.in_memory()
    except CalculatorError as exc:
        assert type(exc) is EmptyMemory
    else:
        raise AssertionError

    try:
        b = calc.run('/', 2)
    except CalculatorError as exc:
        assert type(exc) == EmptyMemory
        assert b is None
    else:
        raise AssertionError

    try:
        b = calc.run('/', 1, 0)
    except CalculatorError as exc:
        assert type(exc.__cause__) == ZeroDivisionError
        assert b is None
    else:
        raise AssertionError
