def count_letters(msg):
    """
    Zwraca pare (znak, liczba zliczeń) dla najczęściej występującego znaku w wiadomości.
    W przypadku równości zliczeń wartości sortowane są alfabetycznie.

    :param msg: Message to count chars in.
    :type msg: str
    :return: Most frequent pair char - count in message.
    :rtype: list
    """
    counts = dict()
    for elem in msg:
        if elem not in counts:
            counts[elem] = 1
        else:
            counts[elem] += 1
    _max, max_key = 0, 'aa'
    for key, val in counts.items():
        if val > _max or (val == _max and key < max_key):
            _max = val
            max_key = key
    return max_key, _max


if __name__ == '__main__':
    msg = 'Abrakadabra'
    assert count_letters(msg) == ('a', 4)
    assert count_letters('za') == ('a', 1)