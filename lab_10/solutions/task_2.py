import calendar
import csv
import pathlib
from datetime import datetime
from typing import Optional, Union, List
from urllib.parse import urljoin

from lab_10.solutions.task_1 import get_metaweather


API_URL = 'https://www.metaweather.com/api/'


def get_city_data(
        woeid: int, year: int, month: int,
        path: Optional[Union[str, pathlib.Path]] = None,
        timeout: float = 5.
) -> (str, List[str]):
    date = datetime(year=year, month=month, day=1)
    if path is None:
        path = pathlib.Path.cwd()
    else:
        path = pathlib.Path(path)
    path /= f'{woeid}_{date.strftime("%Y_%m")}'
    path.mkdir(parents=True, exist_ok=True)

    downloaded_paths = []
    for day in range(1, calendar.monthrange(year, month)[1] + 1):
        url = urljoin(API_URL, f'location/{woeid}/{year}/{month}/{day}')
        data = get_metaweather(url, timeout=timeout)
        if data:
            date = datetime(year=year, month=month, day=day)
            file_name = f'{date.strftime("%Y_%m_%d")}.csv'
            with open(str(path / file_name), 'w') as _file:
                writer = csv.DictWriter(
                    _file, delimiter=',',
                    quotechar='"',
                    fieldnames=data[0].keys()
                )
                writer.writeheader()
                writer.writerows(data)
            downloaded_paths.append(str(file_name))

    return str(path.absolute()), downloaded_paths


if __name__ == '__main__':
    _path = pathlib.Path.cwd()
    expected_path = _path / '523920_2017_03'
    dir_path, file_paths = get_city_data(523920, 2017, 3)
    assert len(file_paths) == 31
    assert pathlib.Path(dir_path).is_dir()
    assert str(expected_path) == dir_path

    expected_path = _path / 'weather_data/523920_2017_03'
    dir_path, file_paths = get_city_data(523920, 2017, 3, path='weather_data')
    assert len(file_paths) == 31
    assert pathlib.Path(dir_path).is_dir()
    assert str(expected_path) == dir_path

    expected_path = _path / 'weather_data/523920_2012_12'
    dir_path, file_paths = get_city_data(523920, 2012, 12, path='weather_data')
    assert len(file_paths) == 0
    assert pathlib.Path(dir_path).is_dir()
    assert str(expected_path) == dir_path
