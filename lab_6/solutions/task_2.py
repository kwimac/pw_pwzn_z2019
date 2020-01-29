"""
Na (1 pkt.):
Napisz program do sprawdzenia poprawności skompresowanego wyjścia poprzedniej
funkcji.
Funkcja MUSI w swej implementacji korzystać z wyrażeń regularnych.

Funkcja na wejściu przyjmuje nazwę pliku do sprawdzenia, na wyjściu zwraca
dwuelementową tuplę zawierającą liczbę poprawnych wierszy:
- na indeksie 0 płeć F
- na indeksie 1 płeć M
"""
import re


def check_animal_list(file_path):
    h = lambda x: f'[0-9a-f]{{{x}}}'
    regex = (
        rf'{h(8)}-{h(4)}-{h(4)}-{h(4)}-{h(12)}'
        r'_(?P<gender>[MF])_(?P<mass>\d\.\d{3}e[+-]\d{2})'
    )

    with open(file_path) as fptr:
        line = fptr.readline()
        counts = dict(F=0, M=0)
        while line:
            match = re.match(regex, line)
            if match:
                values = match.groupdict()
                counts[values['gender']] += 1
            line = fptr.readline()
        return counts['F'], counts['M']


if __name__ == '__main__':
    assert check_animal_list('s_animals_sce.txt') == (2, 2)
    assert check_animal_list('animals_sc_corrupted.txt') == (5, 0)
