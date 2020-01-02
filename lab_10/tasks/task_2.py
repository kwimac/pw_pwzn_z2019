import pathlib
from typing import Optional, Union, List
from urllib.parse import urljoin
import csv
import requests

API_URL = 'https://www.metaweather.com/api/'

def get_city_data(
        woeid: int, year: int, month: int,
        path: Optional[Union[str, pathlib.Path]] = None,
        timeout: float = 5.
) -> (str, List[str]):

    if path is None:
        path = pathlib.Path.cwd()
    else:
        path = pathlib.Path(path)
    path = path / f'{woeid}_{year}_{month:02d}'
    path.mkdir(parents=True, exist_ok=True)

    final_data = []
    for day in range(1, 32):

        location_url = urljoin(API_URL, f'location/{woeid}/{year}/{month}/{day}')

        try:
            response = requests.get(location_url, timeout=timeout)
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
                data = response.json()
                if data:
                    with open(path / f'{year}_{month:02d}_{day:02d}.csv', 'w') as _file:
                        writer = csv.DictWriter(_file, delimiter=',', quotechar='"', fieldnames=data[0].keys())
                        writer.writeheader()
                        writer.writerows(data)

                    final_data.append(path / f'{year}_{month:02d}_{day:02d}.csv')
            except RuntimeError:
                raise RuntimeError

    return str(path), final_data

if __name__ == '__main__':
    _path = pathlib.Path.cwd()
    expected_path = _path / '523920_2017_03'
    dir_path, file_paths = get_city_data(523920, 2017, 3)
    assert len(file_paths) == 31
    assert pathlib.Path(dir_path).is_dir()
    assert str(expected_path) == dir_path

    expected_path = r'weather_data\523920_2017_03'
    dir_path, file_paths = get_city_data(523920, 2017, 3, path='weather_data')
    assert len(file_paths) == 31
    assert pathlib.Path(dir_path).is_dir()
    assert expected_path == dir_path

    expected_path = r'weather_data\523920_2012_12'
    dir_path, file_paths = get_city_data(523920, 2012, 12, path='weather_data')
    assert len(file_paths) == 0
    assert pathlib.Path(dir_path).is_dir()
    assert expected_path == dir_path
