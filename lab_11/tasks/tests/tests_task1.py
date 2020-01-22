import pytest

from lab_11.tasks.tools.calculator import (
    Calculator,
    CalculatorError,
    EmptyMemory,
    NotNumberArgument,
    WrongOperation,
)
is_correct_math = [("+", 2, 2, 4),("-", 2, 2, 0),("*", 2, 2, 4),("/", 2, 2, 1)]
is_correct_error = [("o", 1, 2, WrongOperation),("/", 69, None, EmptyMemory),("-", "12", 2, NotNumberArgument),("/", 1, 0.0, CalculatorError)]


@pytest.fixture(scope="function")
def calculator():
    return Calculator()

@pytest.mark.parametrize("operator,arg1,arg2,outcome", is_correct_math)
def test_is_correct_math(operator, arg1, arg2, outcome, calculator):
    val = calculator.run(operator, arg1, arg2)
    assert val == outcome

@pytest.mark.parametrize("operator,arg1,arg2,error", is_correct_error)
def test_is_correct_error_raised(operator, arg1, arg2, error, calculator):
    with pytest.raises(error):
        calculator.run(operator, arg1, arg2)

def test_memory_functionality(calculator: "Calculator"):
    with pytest.raises(EmptyMemory):
        calculator.in_memory()
    with pytest.raises(EmptyMemory):
        calculator.memory
    calculator.run("*", 2, 2)
    calculator.memorize()
    assert calculator.memory == 4
    assert calculator._short_memory == calculator.memory
    calculator.clean_memory()
    with pytest.raises(EmptyMemory):
        calculator.in_memory()
    with pytest.raises(EmptyMemory):
        calculator.memory