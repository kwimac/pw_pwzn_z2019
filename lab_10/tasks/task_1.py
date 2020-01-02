import requests
from urllib.parse import urljoin

def get_cities_woeid(query: str, timeout: float = 5.):

    API_URL = 'https://www.metaweather.com/api/'
    final_dict = {}

    location_url = urljoin(API_URL, 'location/search')

    try:
        response = requests.get(location_url, params=dict(query = query), timeout = timeout)
    except requests.exceptions.Timeout:
        print(f'Request took to long!')
        raise requests.exceptions.Timeout
    else:
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            print(f'Communication Error!')
            raise requests.exceptions.HTTPError
        try:
            for n in range(0, len(response.json())):
                final_dict[response.json()[n]['title']] = response.json()[n]['woeid']
        except RuntimeError:
            raise RuntimeError
    finally:
        # print(final_dict)
        return final_dict


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
