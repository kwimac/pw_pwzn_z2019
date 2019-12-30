import requests
from urllib.parse import urljoin

def get_cities_woeid(query: str, timeout: float = 5.):
    API_URL = 'https://www.metaweather.com/api/'
    location_url = urljoin(API_URL, 'location/search')
    response = requests.get(location_url, params=dict(query=query)).json()
    new_dict = {}
    for i in response:
        new_dict[i['title']] = i['woeid']
    return new_dict

# dodac obsluge bledow
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
