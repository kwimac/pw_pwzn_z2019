import filecmp
import pathlib
from typing import Union
from os import listdir
from os.path import isfile, join
import pandas as pd


API_URL = 'https://www.metaweather.com/api/'


def concat_data(
        path: Union[str, pathlib.Path],
):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    final_df = pd.DataFrame()
    for file_ in files:
        day = int(file_.split('_')[2].split('.')[0])
        tmp = pd.read_csv(pathlib.Path(path) / file_)
        tmp = tmp[['created', 'min_temp', 'the_temp', 'max_temp', 'air_pressure',
                     'humidity', 'visibility','wind_direction_compass',
                     'wind_direction', 'wind_speed']]
        tmp.rename(columns={'the_temp': 'temp'}, inplace=True)
        tmp.created = pd.to_datetime(tmp.created)
        tmp = tmp[tmp.created.dt.day == day]
        final_df = final_df.append(tmp.copy())

    final_df = final_df.sort_values(['created'])
    final_df[['created']] = final_df.created.dt.strftime('%Y-%m-%dT%H:%M')
    final_df.to_csv(path+".csv", index = False)





if __name__ == '__main__':
    concat_data('weather_data/523920_2017_03')
    assert filecmp.cmp(
        'expected_523920_2017_03.csv',
        'weather_data/523920_2017_03.csv'
    )
