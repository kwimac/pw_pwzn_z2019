import filecmp
import pathlib
from typing import Union

import pandas as pd


API_URL = 'https://www.metaweather.com/api/'


def concat_data(
        path: Union[str, pathlib.Path],
):
    columns = [
        'created',
        'min_temp',
        'temp',
        'max_temp',
        'air_pressure',
        'humidity',
        'visibility',
        'wind_direction_compass',
        'wind_direction',
        'wind_speed'
    ]
    renamed_columns = {
        'the_temp': 'temp',
    }
    all_data = None
    path = pathlib.Path(path)
    for file_path in path.iterdir():
        df = pd.read_csv(file_path, parse_dates=['created', 'applicable_date'])
        df = df[df.created.dt.date == df.applicable_date.dt.date]
        df.rename(columns=renamed_columns, inplace=True)
        df = df[columns]
        all_data = pd.concat([all_data, df])
    all_data.sort_values(['created']).to_csv(
        path.parent / f'{path.stem}.csv',
        index=False,
        date_format='%Y-%m-%dT%H:%M'
    )


if __name__ == '__main__':
    concat_data('weather_data/523920_2017_03')
    assert filecmp.cmp(
        'expected_523920_2017_03.csv',
        'weather_data/523920_2017_03.csv'
    )
