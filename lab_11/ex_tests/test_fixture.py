import pytest

from util import multiply

@pytest.fixture
def param_2():
    value = 4
    print(value)
    return value

@pytest.fixture(scope='module')
def set_connection():
    print('\n >> Connection set <<')


@pytest.mark.usefixtures('set_connection')
def test_numbers_3_fixture(param_2):
    assert multiply(3, param_2) == 12


@pytest.mark.usefixtures('set_connection')
def test_numbers_3_4(param_2):
    assert multiply(3, 4) == 12
