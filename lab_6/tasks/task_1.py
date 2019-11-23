"""
Jesteś informatykiem w firmie Noe's Animals Redistribution Center.
Firma ta zajmuje się międzykontynentalnym przewozem zwierząt.
---------
Celem zadania jest przygotowanie funkcji pozwalającej na przetworzenie
pliku wejściowego zawierającego listę zwierząt do trasnportu.
Funkcja ma na celu wybranie par (samiec i samica) z każdego gatunku,
tak by łączny ładunek był jak najlżeszy (najmniejsza masa osobnika
rozpatrywana jest względem gatunku i płci).
---------
Na 1 pkt.
Funkcja ma tworzyć plik wyjściowy zwierający listę wybranych zwierząt
w formacie wejścia (takim samym jak w pliku wejściowym).
Wyjście ma być posortowane alfabetycznie względem gatunku,
a następnie względem nazwy zwierzęcia.
---------
Na +1 pkt.
Funkcja ma opcję zmiany formatu wejścia na:
"<id>_<gender>_<mass>"
(paramter "compressed") gdzie:
- "id" jest kodem zwierzęcia (uuid),
- "gender" to jedna litera (F/M)
- "mass" zapisana jest w kilogramach w notacji wykładniczej
z dokładnością do trzech miejsc po przecinku np. osobnik ważący 456 gramów
ma mieć masę zapisaną w postaci "4.560e-01"
---------
Na +1 pkt.
* Ilość pamięci zajmowanej przez program musi być stałą względem
liczby zwierząt.
* Ilość pamięci może rosnąć liniowo z ilością gatunków.
---------
UWAGA: Możliwe jest wykonanie tylko jednej opcji +1 pkt.
Otrzymuje się wtedy 2 pkt.
UWAGA 2: Wszystkie jednoski masy występują w przykładzie.
"""
from pathlib import Path
import csv
from decimal import Decimal

def select_animals(input_path, output_path, compressed=False):

    with open(input_path) as file_:
        reader = csv.DictReader(file_)

        mass_units = {
            'Mg': 1000,
            'kg': 1,
            'g': 0.001,
            'mg': 0.000001,
        }

        f_mass = {}
        m_mass = {}
        output = []

        for row in reader:
            mass = row['mass'].split(' ')
            kg_mass = float(mass[0]) * mass_units[mass[1]]

            if row['gender'] == 'female':
                if row['genus'] not in f_mass.keys():
                    f_mass[row['genus']] = kg_mass/mass_units[mass[1]]
                else:
                    if kg_mass < f_mass[row['genus']]:
                        f_mass[row['genus']] = kg_mass/mass_units[mass[1]]

            elif row['gender'] == 'male':
                if row['genus'] not in m_mass.keys():
                    m_mass[row['genus']] = kg_mass/mass_units[mass[1]]
                else:
                    if kg_mass < f_mass[row['genus']]:
                        m_mass[row['genus']] = kg_mass/mass_units[mass[1]]

            if float(mass[0]) in f_mass.values():
                output.append(row)
            if float(mass[0]) in m_mass.values():
                output.append(row)

            output = sorted(output, key=lambda row: (row['genus'], row['name']))

        with open(output_path, 'w', newline='') as file_:
            if compressed:
                writer = csv.writer(file_, delimiter=',', quotechar="*")
                writer.writerow(['uuid_gender_mass'])
                gender = {'male': 'M', 'female': 'F'}
                for row in output:
                    mass = row['mass'].split(' ')
                    writer.writerow(['{}_{}_{}'.format(row['id'], gender[row['gender']], '%.3e' % Decimal(
                        float(mass[0]) * mass_units[mass[1]]))])
            else:
                fields = ['id', 'mass', 'genus', 'name', 'gender']
                writer = csv.DictWriter(file_, delimiter=',', fieldnames=fields)
                writer.writeheader()
                writer.writerows(output)

if __name__ == '__main__':
    input_path = Path('s_animals.txt')
    output_path = Path('s_animals_s.txt')
    select_animals(input_path, output_path)
    with open(output_path) as generated:
        with open('s_animals_se.txt') as expected:
            assert generated.read() == expected.read()

    output_path = Path('s_animals_sc.txt')
    select_animals(input_path, output_path, True)
    with open(output_path) as generated:
        with open('s_animals_sce.txt') as expected:
            assert generated.read() == expected.read()
