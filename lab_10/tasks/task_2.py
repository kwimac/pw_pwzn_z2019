import pathlib
from typing import Optional, Union, List
import requests
from urllib.parse import urljoin
from csv import writer
from calendar import monthrange

API_URL = 'https://www.metaweather.com/api/'

def get_daily_data(woeid, year, month, day, timeout):
    location_url = urljoin(API_URL, f'location/{woeid}/{year}/{month}/{day}')

    data = None
    try:
        response = requests.get(location_url, timeout=timeout)
        data = response.json()
    except requests.exceptions.Timeout:
        print(f'Request for: {location_url} took to long!')
        raise requests.exceptions.Timeout
    return data


def save_to_csv(dict, filename):
    file = open(filename, 'w')
    # create the csv writer object
    csvwriter = writer(file)
    csvwriter.writerow(dict.keys())
    csvwriter.writerow(dict.values())

    file.close()


def get_city_data(
        woeid: int, year: int, month: int,
        path: Optional[Union[str, pathlib.Path]] = None,
        timeout: float = 5.
) -> (str, List[str]):
    days_in_query = monthrange(year,month)[1]
    my_month = str(month)
    if month < 10:
        my_month = "0" + my_month
    woeid_folder_name = str(woeid)+"_"+str(year)+"_"+my_month

    if path is None:
        folder = pathlib.Path.cwd() / woeid_folder_name
    elif path[1] == ":":
        folder = pathlib.Path(path)
    else:
        folder = pathlib.Path(path) / woeid_folder_name
    folder.mkdir(parents=True, exist_ok=True)
    file_names = []
    for i in range(days_in_query):
        data = get_daily_data(woeid,year,month,i+1, timeout)
        filename = str(year) + "_" + str(month) + "_" + str(i+1)
        file_full_path = folder / filename
        try:
            save_to_csv(data[0],file_full_path)
            file_names.append(filename)
        except:
            raise requests.exceptions.HTTPError
            #return str(folder), file_names

    return str(folder), file_names

    pass


if __name__ == '__main__':
    _path = pathlib.Path.cwd()
    expected_path = _path / '523920_2017_03'
    dir_path, file_paths = get_city_data(523920, 2017, 3)
    assert len(file_paths) == 31
    assert pathlib.Path(dir_path).is_dir()
    assert str(expected_path) == dir_path

    expected_path = 'weather_data\\523920_2017_03'
    dir_path, file_paths = get_city_data(523920, 2017, 3, path='weather_data')
    assert len(file_paths) == 31
    assert pathlib.Path(dir_path).is_dir()
    assert expected_path == dir_path

    expected_path = 'weather_data\\523920_2012_12'
    dir_path, file_paths = get_city_data(523920, 2012, 12, path='weather_data')
    assert len(file_paths) == 0
    assert pathlib.Path(dir_path).is_dir()
    assert expected_path == dir_path
