import datetime

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


def sort_dates(date_str, date_format=' %a %d %B %Y %H:%M:%S %z'):
    """
    Parses and sorts given message to list of datetimes objects descending.
    :param date_str: log of events in time
    :type date_str: str
    :param date_format: event format
    :type date_format: str
    :return: sorted desc list of utc datetime objects
    :rtype: list
    """
    datestring_list = date_str.splitlines()
    datestring_list_filtered = list(filter(lambda x: x != " " and x != "" and x != "    ", datestring_list))
    date_datetime = list(map(lambda x: datetime.datetime.strptime(x, date_format), datestring_list_filtered))
    datetime_utc = list(map(lambda x: x.astimezone(datetime.timezone.utc), date_datetime))
    datetime_utc.sort(reverse=True)

    return (datetime_utc)


def group_dates(dates):
    """
    Groups list of given days day by day.
    :param dates: List of dates to group.
    :type dates: list
    :return:
    """
    days = list(set(map(lambda x: x.date(), dates)))  # wyciagamy daty z listy wejscowej

    days_listed = list(map(lambda x: [x], days))  # zmieniamy kazdy element listy w liste

    for i in days_listed:
        for j in dates:
            if j.date() == i[0]:  # szukamy dataczasow o dacie takiej samej jak z danej daty
                i.append(j)
        i.pop(0)  # wywalamy daty z list

    days.sort(reverse=True)
    days_listed.sort(reverse=True)
    to_return = [days, days_listed]
    return (to_return)


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
    date_str = day.strftime("%Y-%m-%d\n")
    events_str_list = list(map(lambda x: x.strftime("\t%H:%M:%S"), events))
    joined_events = "\n".join(events_str_list, )

    return (date_str + joined_events)

    pass


def parse_dates(date_str, date_format=' %a %d %B %Y %H:%M:%S %z'):
    """
    Parses and groups (in UTC) given list of events.
    :param date_str: log of events in time
    :type date_str: str
    :param date_format: event format
    :type date_format: str
    :return: parsed events
    :rtype: str
    """
    sorting = sort_dates(date_str, date_format)

    grouping = group_dates(sorting)

    tmp_str = []

    for i in range(len(grouping[0])):
        tmp_str.append(format_day(grouping[0][i], grouping[1][i]))
    return ("\n----\n".join(tmp_str))

    pass


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

assert parse_dates(dates) == """2015-05-10
\t20:54:36
\t13:54:36
----
2015-05-02
\t14:24:36
----
2015-05-01
\t13:54:36"""
