from task_1 import parse_input
from collections import Counter


def check_frequency(input):
    """
    Perform counting based on input queries and return queries result.

    Na wejściu otrzymujemy parę liczb całkowitych - operacja, wartość.
    Możliwe operacje:
    1, x: zlicz x
    2, x: usuń jedno zliczenie x jeżeli występuje w zbiorze danych
    3, x: wypisz liczbę zliczeń x (0 jeżeli nei występuje) na przyklad: 3 2 : wypisac liczbe zliczen dwojki
    Do parsowania wejścia wykorzystaj funkcję parse_input.
    Po wejsciu iterujemy tylko raz (tylko jedna petla)
    Zbiór danych zrealizuj za pomocą struktury z collections.
    Parsujemy za pomoca funkcji z poprzedniego zadania.

    :param input: pairs of int: command, value
    :type input: string
    :return: list of integers with results of operation 3
    :rtype: list

    wskazówka: skorzystaj z modulu collections
    """
    tmp = parse_input(input)
    myCounter = Counter()
    tobereturned = []


    for elem in tmp:
        if elem[0] == 1:
            myCounter.update([elem[1]])
        elif elem[0] == 2:
            myCounter.subtract([elem[1]])
        elif elem[0] == 3:
            tobereturned.append(myCounter[elem[1]])
    return (tobereturned)



_input = """
1 5
1 6
3 2
1 10
1 10
1 6
2 5
1 2
3 2


"""

if __name__ == '__main__':
    assert check_frequency(_input) == [0, 1]