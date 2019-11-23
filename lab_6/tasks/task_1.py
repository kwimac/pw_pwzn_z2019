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
import operator
from decimal import Decimal

def str_to_mass(str):
    units = str[-2:]
    mass = float(str[:-3])
    if units == "kg":
        return mass
    elif units == " g":
        return mass/1000
    elif units == "mg":
        return mass/1000/1000
    elif units == "Mg":
        return mass*1000




def select_animals(input_path, output_path, compressed=False):
    male_wolf = None
    female_wolf = None
    male_wpecker = None
    female_wpecker = None

    with open(input_path,'r') as input_file:
        csv_reader = csv.DictReader(input_file, delimiter=',')
        for row in csv_reader:
            mass = str_to_mass(row['mass'])
            if row['genus'] == "Wolf":
                if row['gender'] == "male":
                    if male_wolf is None or str_to_mass(male_wolf['mass']) > mass:
                        male_wolf = row
                else:
                    if female_wolf is None or str_to_mass(female_wolf['mass']) > mass:
                        female_wolf = row
            elif row['genus'] == "Woodpecker":
                if row['gender'] == "male":
                    if male_wpecker is None or str_to_mass(male_wpecker['mass']) > mass:
                        male_wpecker = row
                else:
                    if female_wpecker is None or str_to_mass(female_wpecker['mass']) > mass:
                        female_wpecker = row

        output = [male_wolf,female_wolf,male_wpecker,female_wpecker]
        output.sort(key=operator.itemgetter('name'))

        if compressed is False:
            outfile = open(output_path, 'w')
            wrtr = csv.DictWriter(outfile, fieldnames=["id", "mass", "genus", "name", "gender"], delimiter=',',
                                  lineterminator="\n")
            wrtr.writeheader()
            for line in output:
                wrtr.writerow(line)

            outfile.close()
        else:
            outfile = open(output_path, 'w')
            compressed_output = ["uuid_gender_mass"]
            for line in output:
                if line['gender'] == "male":
                    line['gender'] = "M"
                else:
                    line['gender'] = "F"
                e_notation = '%.3e' % Decimal(str_to_mass(line['mass']))
                compressed_line = line['id']+"_"+line['gender']+"_"+e_notation
                compressed_output.append(compressed_line)
            for i in compressed_output:
                outfile.write(i+"\n")




            outfile.close()









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
