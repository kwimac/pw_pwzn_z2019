import pytest

from tools.calculator import (
    Calculator,
    CalculatorError,
    EmptyMemory,
    NotNumberArgument,
    WrongOperation,
)

@pytest.fixture(scope='module')
def calculator():
    return Calculator()

@pytest.mark.parametrize ('operator, arg1, arg2, expected',
                          [
                              pytest.param('+', 3, 6, 9),
                              pytest.param('+', -2, -5, -7),
                              pytest.param('-', 8, -3, 11),
                              pytest.param('-', 5, 9, -4),
                              pytest.param('*', 3, 0, 0),
                              pytest.param('*', 8, -3, -24),
                              pytest.param('/', 6, 3, 2),
                              pytest.param('/', 5, 10, 0.5)
                          ])

def test_dzialania(calculator, operator, arg1, arg2, expected):
    assert calculator.run(operator, arg1, arg2) == expected

@pytest.mark.parametrize ('operator, arg1, arg2, expected',
                          [
                              pytest.param('/', 3, 0, CalculatorError),
                              pytest.param('^', 2, 4, WrongOperation),
                              pytest.param('plus', 8, -3, WrongOperation),
                              pytest.param(5, '*', 2, WrongOperation),
                              pytest.param(5, 6, 3, WrongOperation),
                              pytest.param('-', 3, None, EmptyMemory),
                              pytest.param('*', 8, 's', NotNumberArgument),
                              pytest.param('/', 'two', 3, NotNumberArgument)
                          ])

def test_bledy(calculator, operator, arg1, arg2, expected):
    with pytest.raises(expected):
        calculator.run(operator, arg1, arg2)

def test_pamieci(calculator):
    calculator.run('*', 3, 6)
    assert calculator._short_memory == 18
    calculator.memorize()
    assert calculator._memory == 18
    assert calculator.in_memory() == print(f'Zapamiętana wartość: 18')
    assert calculator.run('-', 20) == 2
    calculator.clean_memory()
    assert calculator._memory == None
    with pytest.raises(EmptyMemory):
        calculator.in_memory()
        calculator.run('/', 4)