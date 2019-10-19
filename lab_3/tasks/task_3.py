"""
Zadanie za 2 pkt.

Uzupełnij funckję parse_dates tak by zwracała przygotowaną wiadomość
z posortowanymi zdarzeniami.
Funkcja przyjmuje ciag zdarzeń (zapisanych w formie timestampu w dowolnej strefie czasowej),
przetwarza je na zdarzenia w strefie czasowej UTC i sortuje.
Posortowane zdarzenia są grupowane na dni i wypisywane od najnowszych do najstarszych.

Na 1pkt. Uzupełnij funkcję sort_dates, która przyjmuje dwa parametry:
- log (wielolinijkowy ciąg znaków z datami) zdarzeń
- format daty (podany w assercie format ma być domyślnym)
Zwraca listę posortowanych obiektów typu datetime w strefie czasowej UTC.

Funkcje group_dates oraz format_day mają pomoc w grupowaniu kodu.
UWAGA: Proszę ograniczyć użycie pętli do minimum.
"""
import datetime
from task_1 import parse_input

def sort_dates(date_str, date_format=''):
    """
    Parses and sorts given message to list of datetimes objects descending.

    :param date_str: log of events in time
    :type date_str: str
    :param date_format: event format
    :type date_format: str
    :return: sorted desc list of utc datetime objects
    :rtype: list
    """

    import datetime


    mod_input = dates.strip()
    listed_dates = mod_input.split('\n')
    list_without_whitespaces = list(map(lambda x: x.strip(), listed_dates))
    # print(list_without_whitespaces)

    timestamp_list = []
    for date in list_without_whitespaces:
        timestamp = datetime.datetime.strptime(date, '%a %d %b %Y %X %z').timestamp()
        timestamp_list.append(timestamp)

    result = list(
        map(lambda x: datetime.datetime.fromtimestamp(x, tz=datetime.timezone.utc).strftime("%a %d %b %Y %H:%M:%S %z"),
            timestamp_list))
    # print(result)

    formated_list = list(map(lambda date: datetime.datetime.strptime(date,"%a %d %b %Y %H:%M:%S %z"), result))
    formated_list.sort(reverse=True)

    # print(formated_list)

    return formated_list


def group_dates(dates):
    """
    Groups list of given days day by day.

    :param dates: List of dates to group.
    :type dates: list
    :return:
    """
    days = []
    times = []

    for elem in dates:
        if elem.date() not in days:
            days.append(elem.date())
            times.append([elem.time()])
        else:
            times[-1].extend([elem.time()])

    events = [(day, time) for day, time in zip(days, times)]

    return(events)


def format_day(day, events):
    """
    Formats message for one day.

    :param day: Day object.
    :type day: datettime.datetime
    :param events: List of events of given day
    :type events: list
    :return: parsed message for day
    :rtype: str
    """
    pass


def parse_dates(date_str, date_format="%Y-%m-%d %H:%M:%S"):
    """
    Parses and groups (in UTC) given list of events.

    :param date_str: log of events in time
    :type date_str: str
    :param date_format: event format
    :type date_format: str
    :return: parsed events
    :rtype: str
    """
    from collections import defaultdict, OrderedDict

    date_dict = defaultdict(list)

    split_dates = date_str.split('\n')
    for date in split_dates:
        if date.strip():
            timestamp = datetime.datetime.strptime(date.strip(), '%a %d %b %Y %X %z').timestamp()
            date_time = datetime.datetime.utcfromtimestamp(timestamp)

            date_dict[date_time.date().isoformat()].append(date_time.timetz().isoformat())

    response_string = ''

    for key, times in date_dict.items():
        response_string += '\n----\n'
        response_string += key + '\n' + '\t'
        response_string += '\t'.join([time for time in times])

    response = response_string.split('----', 1)
    # print(response[1])
    return response[1]



if __name__ == '__main__':
    dates = """
    Sun 10 May 2015 13:54:36 -0700
    Sun 10 May 2015 13:54:36 -0000
    Sat 02 May 2015 19:54:36 +0530
    Fri 01 May 2015 13:54:36 -0000
    """

    assert sort_dates(dates) == [
        datetime.datetime(2015, 5, 10, 20, 54, 36, tzinfo=datetime.timezone.utc),
        datetime.datetime(2015, 5, 10, 13, 54, 36, tzinfo=datetime.timezone.utc),
        datetime.datetime(2015, 5, 2, 14, 24, 36, tzinfo=datetime.timezone.utc),
        datetime.datetime(2015, 5, 1, 13, 54, 36, tzinfo=datetime.timezone.utc),
    ]
    #
    # assert parse_dates(dates) == """2015-05-10
    # \t20:54:36
    # \t13:54:36
    # ----
    # 2015-05-02
    # \t14:24:36
    # ----
    # 2015-05-01
    # \t13:54:36"""