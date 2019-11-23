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
    female_correct = 0
    male_correct = 0
    header = True
    with open(file_path, 'r') as input_file:
        for row in input_file:
            if header is True:
                header = False
                continue

            male_pattern = bool(re.search('^([a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}_M_[0-9]\.[0-9]{3}e[+-][0-9]{2})', row))
            female_pattern = bool(re.search(
                '^([a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}_F_[0-9]\.[0-9]{3}e[+-][0-9]{2})',
                row))
            if male_pattern:
                male_correct = male_correct + 1

            if female_pattern:
                female_correct = female_correct + 1

    return female_correct, male_correct


if __name__ == '__main__':
    assert check_animal_list('s_animals_sce.txt') == (2, 2)
    assert check_animal_list('animals_sc_corrupted.txt') == (5, 0)
    pass