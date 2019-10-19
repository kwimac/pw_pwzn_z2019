def check_frequency(input):
    """
    Perform counting based on input queries and return queries result.

    Na wejściu otrzymujemy parę liczb całkowitych - operacja, wartość.
    Możliwe operacje:
    1, x: zlicz x
    2, x: usuń jedno zliczenie x jeżeli występuje w zbiorze danych
    3, x: wypisz liczbę zliczeń x (0 jeżeli nei występuje)
    Do parsowania wejścia wykorzystaj funkcję parse_input.
    Po wejściu (już jakoliście) iterujemy tylko raz (jedna pętla).
    Zbiór danych zrealizuj za pomocą struktury z collections.

    :param input: pairs of int: command, value
    :type input: string
    :return: list of integers with results of operation 3
    :rtype: list
    """
    from task_1 import parse_input
    import collections

    parsed_input = parse_input(_input)

    numbers = []
    output = []
    for i in parsed_input:
        if i[0] == 1:
            numbers.append(i[1])
        elif i[0] == 2:
            if i[1] in numbers:
                numbers.remove(i[1])
        elif i[0] == 3:
            c = collections.Counter(numbers)
            if i[1] in c.values():
                n = collections.Counter(c.values())
                output.append(n[i[1]])
            else:
                output.append(0)

    return(output)


_input = """
1 5
1 6
2 1
3 2
1 10
1 10
1 6
2 5
3 2


"""
# Nie wiem czy dobrze, zrozumiałam polecenie, ale pamiętam, że na zajęciach mówił Pan,
# że funkcja ma pokazywać ile jest x-ów o liczbie zliczeń podanej dla operacji nr 3.
# W tym przypadku dla drugiej z operacji nr 3 funkcja wyrzuca ile x-ów występuje 2 razy.
# Mamy 2 razy liczbę 6 i 2 razy liczbę 10, dlatego poprawną odpowiedzią powinno być chyba [0, 2].
if __name__ == '__main__':
    assert check_frequency(_input) == [0, 2]