from urllib.parse import urljoin

import requests


API_URL = 'https://www.metaweather.com/api/'


def get_metaweather(url, query, timeout=5.):
    get_params = dict(
        timeout=timeout,
    )
    if query:
        get_params['params'] = query
    response = requests.get(
        url,
        **get_params
    )
    response.raise_for_status()
    try:
        return response.json()
    except TypeError as exc:
        raise RuntimeError from exc


def get_cities_woeid(query, timeout=5.):
    location_url = urljoin(API_URL, 'location/search')
    query = dict(query=query)
    content = get_metaweather(location_url, query, timeout)
    return {
        elem['title']: elem['woeid']
        for elem in content
    }


if __name__ == '__main__':
    assert get_cities_woeid('Warszawa') == {}
    assert get_cities_woeid('War') == {
        'Warsaw': 523920,
        'Newark': 2459269,
    }
    try:
        get_cities_woeid('Warszawa', 0.1)
    except Exception as exc:
        isinstance(exc, requests.exceptions.Timeout)
