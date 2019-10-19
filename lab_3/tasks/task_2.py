from collections import Counter
from task_1 import parse_input


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
    list_numbers = parse_input(_input)
    counter_list = [0] * 10
    final_list = []
    c = Counter()
    for [i, j] in list_numbers:
        if i == 1:
            counter_list[j - 1] += 1
        if i == 2:
            if counter_list[j - 1] > 0:
                counter_list[j - 1] -= 1
        if i == 3:
            c = Counter(counter_list)
            final_list.append(c[j])

    # print(final_list)
    return final_list


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
if __name__ == '__main__':
    # popełnił Pan chyba przypadkiem błąd i powinno być [0,2] a nie [0,1] bo występują 2 elementy które wystąpiły 2 razy (6 i 10)
    assert check_frequency(_input) == [0, 2]
