import pytest
import requests
import requests_mock

from tools.metaweather import (
    get_metaweather
)

API_URL_1 = 'https://www.metaweather.com/api/location/search?query=Warszawa'
API_URL_2 = 'https://www.metaweather.com/api/location/search?query=War'


def test_no_hits():

    with requests_mock.Mocker() as mock:
        mock.get(API_URL_1, json = [])
        assert get_cities_woeid('Warszawa') == {}


def test_good_response():

    with requests_mock.Mocker() as mock:
        mock.get(API_URL_2, json=[{'title': 'Warsaw', 'woeid': 523920}, {'title': 'Newark', 'woeid': 2459269}])
        assert get_cities_woeid('War') == {'Warsaw': 523920, 'Newark': 2459269}

def test_timeout():

    with pytest.raises(requests.exceptions.Timeout):
        get_cities_woeid('War', timeout=0.01)


def test_status():

    with requests_mock.Mocker() as mock:
        mock.get(API_URL_2, status_code=404)

        with pytest.raises(requests.exceptions.HTTPError):
            get_cities_woeid('War')
