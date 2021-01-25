import filecmp
import pathlib
from typing import Union

import pandas as pd


API_URL = 'https://www.metaweather.com/api/'


def concat_data(
        path: Union[str, pathlib.Path],
):
    if not isinstance(path, pathlib.Path):
        path = pathlib.Path(path)

    all_data = pd.DataFrame()

    for file in path.iterdir():
        data = pd.read_csv(file)
        data = data[pd.to_datetime(data.applicable_date).dt.date == pd.to_datetime(data.created).dt.date]
        all_data = pd.concat([all_data, data])

    final_data = pd.DataFrame(all_data,
                              columns=['created', 'min_temp', 'the_temp', 'max_temp', 'air_pressure', 'humidity', 'visibility', 'wind_direction_compass', 'wind_direction', 'wind_speed'])
    final_data = final_data.rename(columns={'the_temp': 'temp'})
    final_data['created'] = pd.to_datetime(final_data['created']).dt.strftime("%Y-%m-%dT%H:%M")
    final_data.sort_values(['created'], inplace=True)
    final_data.to_csv(f'{path}.csv', index=False)


if __name__ == '__main__':
    concat_data('weather_data/523920_2017_03')
    assert filecmp.cmp(
        'expected_523920_2017_03.csv',
        'weather_data/523920_2017_03.csv'
    )
