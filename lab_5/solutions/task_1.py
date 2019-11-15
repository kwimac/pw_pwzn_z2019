"""
Uzupełnij klasę Calculator o obsługę wyjątków (1pkt).
Podnoszone wyjątki:
- błędna operacja - WrongOperation
- błędne argumenty (nie liczba) - NotNumberArgument
- pusta pamięć (zarówno przy pytaniu o pamięć
jak i operację z argumentem domyślnym) - EmptyMemory
"""
import sys
from operator import add, mul, sub, truediv


class CalculatorError(Exception):
    pass


class WrongOperation(CalculatorError):
    pass


class NotNumberArgument(CalculatorError):
    pass


class EmptyMemory(CalculatorError):
    pass


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

    @staticmethod
    def _cast_to_num(val):
        try:
            return float(val)
        except TypeError:
            return complex(val)

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
        try:
            arg2 = arg2 if arg2 is not None else self.memory
            res = self.operations[operator](
                self._cast_to_num(arg1),
                self._cast_to_num(arg2),
            )
            self._short_memory = self._cast_to_num(res)
        except KeyError:
            raise WrongOperation()
        except (ValueError, TypeError):
            raise NotNumberArgument()
        except ZeroDivisionError as _exc:
            raise CalculatorError() from _exc
        else:
            return self._short_memory

    @property
    def memory(self):
        if self._memory is not None:
            return self._memory
        else:
            raise EmptyMemory()

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
