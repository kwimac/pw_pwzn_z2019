import json

import pytest
import requests_mock
from requests import HTTPError
from requests.exceptions import ConnectTimeout

from lab_11.tasks.tools.metaweather import (
    get_cities_woeid
)


EMPTY_RESPONSE = []
EMPTY_RESULT = {}
PROPER_RESPONSE = [
    {
        'title': 'Warsaw', 'location_type': 'City',
        'woeid': 523920, 'latt_long': '52.235352,21.009390'
    }, {
        'title': 'Newark', 'location_type': 'City',
        'woeid': 2459269, 'latt_long': '40.731972,-74.174179'
    }
]
PROPER_RESULT = {
    'Warsaw': 523920,
    'Newark': 2459269,
}


@pytest.mark.parametrize(
    ('query', 'response', 'expected'),
    [
        pytest.param('Warszawa', EMPTY_RESPONSE, EMPTY_RESULT, id='Empty'),
        pytest.param(
            'War', PROPER_RESPONSE, PROPER_RESULT,
            id='Proper response',
        ),
    ]
)
def test__get_cities_woeid(query, response, expected):
    with requests_mock.mock() as m:
        m.get(requests_mock.ANY, status_code=200, text=json.dumps(response))

    result = get_cities_woeid(query)
    assert result == expected


def test__get_cities_woeid__wrong_status():
    with requests_mock.mock() as m:
        m.get(requests_mock.ANY, status_code=500, text='some error')

        with pytest.raises(HTTPError):
            get_cities_woeid('')


def test__get_cities_woeid__timeout():
    with requests_mock.mock() as m:
        m.get(requests_mock.ANY, exc=ConnectTimeout)

        with pytest.raises(ConnectTimeout):
            get_cities_woeid('', 0.1)
