def count_letters(msg):
    list = []
    wynik = []
    for letter in msg:
        a = msg.count(letter)
        list.append(a)
    _max = max(list)
    for letter in msg:
        a = msg.count(letter)
        if a == _max:
            if letter not in wynik:
                wynik.append(letter)
                wynik.sort()

    print(wynik, _max)
    return(wynik, _max)

#msg = 'Abrakadabra'
#assert count_letters(msg) == ('a', 4)
#assert count_letters('za') == ('a', 1)