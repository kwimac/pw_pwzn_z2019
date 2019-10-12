def count_letters(msg):

    list_of_chars=list(set(msg))
    list_of_chars.sort()
    list_of_counts = []
    for i in list_of_chars:
        list_of_counts.append(msg.count(i))
    maximum = max(list_of_counts)
    index_max = list_of_counts.index(maximum)

    krotka = (list_of_chars[index_max],list_of_counts[index_max])

    return (krotka)






    """
    Zwraca pare (znak, liczba zliczeń) dla najczęściej występującego znaku w wiadomości.
    W przypadku równości zliczeń wartości sortowane są alfabetycznie.

    :param msg: Message to count chars in.
    :type msg: str
    :return: Most frequent pair char - count in message.
    :rtype: list
    jezeli sa dwie literki z taka sama liczba, to ma byc brane alfabetycznie
    """
    pass


if __name__ == '__main__':
    msg = 'Abrakadabra'
    assert count_letters(msg) == ('a', 4)
    assert count_letters('za') == ('a', 1)