import pytest

from util import multiply

@pytest.fixture
def param_2():
    return 4

# Poniższy dekorator dodaje dwie wersje testu
@pytest.mark.parametrize(
    'param_1, expected',  # lista parametrów, może być podana jako tupla stringów
    [
        # podanie przez obiekt `param` pozwala na nazwanie zbioru parametrów
        pytest.param(3, 12, id='Numbers'),  
        ['a', 'aaaa'], # ale można podać go też jako iterablę
    ],
)
def test_numbers_3_parametrize(param_1, param_2, expected):
    assert multiply(param_1, param_2) == expected
