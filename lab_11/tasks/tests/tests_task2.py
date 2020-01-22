import pytest
import unittest.mock
from lab_11.tasks.tools.metaweather import (
    get_metaweather,
    get_cities_woeid
)
import requests



def test_get_cities_woeid():
    mock_response = unittest.mock.MagicMock()
    mock_response.json.return_value = [{"title": "Warsaw", "woeid": 523920},{"title": "Newark", "woeid": 2459269}]
    mock_response.status = 200

    with unittest.mock.patch("requests.get", return_value=mock_response) as mock:
        assert get_cities_woeid("War") == {
            "Warsaw": 523920,
            "Newark": 2459269
        }


def test_timeout_exception():

    with unittest.mock.patch("requests.get", side_effect=requests.exceptions.Timeout()) as mock:
        with pytest.raises(requests.exceptions.Timeout):
            get_cities_woeid("Warszawa", 0.1)