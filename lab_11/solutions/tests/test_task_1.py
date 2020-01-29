import pytest

from lab_11.tasks.tools.calculator import (
    Calculator,
    CalculatorError,
    EmptyMemory,
    NotNumberArgument,
    WrongOperation,
)


@pytest.fixture
def calculator():
    return Calculator()


def test__exception_inheritance():
    assert issubclass(EmptyMemory, CalculatorError)
    assert issubclass(NotNumberArgument, CalculatorError)
    assert issubclass(WrongOperation, CalculatorError)


@pytest.mark.parametrize(
    ('operator', 'expected'),
    [
        pytest.param('+', 5, id='Add'),
        pytest.param('-', 1, id='Sub'),
        pytest.param('*', 6, id='Mul'),
        pytest.param('/', 1.5, id='Div'),
    ]
)
def test__operations(calculator, operator, expected):
    assert calculator.run(operator, 3, 2) == expected


def test__wrong_operator_exception(calculator):
    with pytest.raises(WrongOperation):
        calculator.run('^', 2, 3)


def test__zero_division(calculator):
    with pytest.raises(CalculatorError) as exc:
        calculator.run('/', 2, 0)
    assert isinstance(exc.value.__cause__, ZeroDivisionError)


def test__string_argument(calculator):
    assert calculator.run('*', '-1.2', 3) == pytest.approx(-3.6, abs=0.1)


def test__complex_argument(calculator):
    assert calculator.run('*', 3, 5+1j) == pytest.approx((15+3j), abs=0.1)


@pytest.mark.parametrize(
    ('value',),
    [
        pytest.param('a', id='Letter'),
        pytest.param({}, id='Collection'),
    ]
)
def test__wrong_not_a_number(calculator, value):
    with pytest.raises(NotNumberArgument):
        calculator.run('*', 3, value)


def test__empty_memory(calculator):
    with pytest.raises(EmptyMemory):
        calculator.in_memory()


def test__empty_memory_in_operation(calculator):
    with pytest.raises(EmptyMemory):
        calculator.run('/', 3)
