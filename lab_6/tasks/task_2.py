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

    with open(file_path) as file_:

        f_pattern = r'^[\da-f]{8}\-[\da-f]{4}\-[\da-f]{4}\-[\da-f]{4}\-[\da-f]{12}_F_[\d]\.[\d]{3}[e][\-\+][\d]{2}$'
        m_pattern = r'^[\da-f]{8}\-[\da-f]{4}\-[\da-f]{4}\-[\da-f]{4}\-[\da-f]{12}_M_[\d]\.[\d]{3}[e][\-\+][\d]{2}$'

        f_count = 0
        m_count = 0

        for line in file_.readlines():

            if bool(re.fullmatch(f_pattern, line.strip())):
                f_count += 1
            if bool(re.fullmatch(m_pattern, line.strip())):
                m_count += 1

        # print(f_count, m_count)
        return f_count, m_count

if __name__ == '__main__':
    assert check_animal_list('s_animals_sce.txt') == (2, 2)
    assert check_animal_list('animals_sc_corrupted.txt') == (5, 0)
<<<<<<< HEAD

# Na podstawie Pana komentarza w konwersacji rozumiem, że program powinien uznawac wielkie litery w UUID jako blad.
# Taka tez informacje znalazalam w internecie: "6.5.4 Software generating the hexadecimal representation of a UUID shall not use upper case letters."
# Jednak w wielu zrodlach dopuszczalne jest uzycie rowniez wielkich liter. Wtedy f_pattern i m_pattern wygladalyby nastepujaco:
#    f_pattern = r'^[\da-fA-F]{8}\-[\da-fA-F]{4}\-[\da-fA-F]{4}\-[\da-fA-F]{4}\-[\da-fA-F]{12}_F_[\d]\.[\d]{3}[e][\-\+][\d]{2}$'
#    m_pattern = r'^[\da-fA-F]{8}\-[\da-fA-F]{4}\-[\da-fA-F]{4}\-[\da-fA-F]{4}\-[\da-fA-F]{12}_M_[\d]\.[\d]{3}[e][\-\+][\d]{2}$'
