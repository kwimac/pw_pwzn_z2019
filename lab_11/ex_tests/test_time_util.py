from unittest.mock import patch
from datetime import datetime

import pytest

from time_util import tell_me_yesterday


# Mockowanie w ten sposób nie da efektów, bo funkcja jest już zdefiniowana
# @patch('datetime.datetime')
@patch('time_util.datetime')
def test_numbers_3_parametrize(datetime_mock, capsys):
    datetime_mock.now.return_value = datetime(2019, 1, 1)
    tell_me_yesterday()
    # metoda przechwytuje to co zostało wypisane na standardowe wyjście
    assert capsys.readouterr().out == 'Yesterday was: 2019-01-01\n'
