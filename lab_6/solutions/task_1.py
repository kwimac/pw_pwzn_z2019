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
import csv
from collections import defaultdict
from itertools import chain
from operator import itemgetter
from pathlib import Path


mass_unit = {
    'Mg': float(1e3),
    'kg': float(1e0),
    'g': float(1e-3),
    'mg': float(1e-6),
}


def select_animals(input_path, output_path, compressed=False):
    animals = defaultdict(lambda: [{'_mass': float('inf')}] * 2)

    with open(input_path) as fptr:
        reader = csv.DictReader(fptr)
        for animal in reader:
            mass = animal['mass'].split(' ')
            animal['_mass'] = float(mass[0]) * mass_unit[mass[1]]
            genus = animal['genus']
            gender = animal['gender'] == 'male'
            animals[genus][gender] = min(
                animals[genus][gender],
                animal,
                key=lambda x: x['_mass']
            )
    # remove unpaired animals
    animals = filter(
        lambda item: all(elem['_mass'] != float('inf') for elem in item[1]),
        animals.items()

    )
    # sorting results
    animals = map(
        lambda item: (item[0], sorted(item[1], key=itemgetter('name'))),
        animals
    )
    animals = sorted(animals, key=lambda item: item[0])

    # preparing to write
    animals = chain.from_iterable(item[1] for item in animals)

    if compressed:
        animals = (
            dict(
                uuid=item['id'],
                gender=item['gender'][0].upper(),
                mass=f'{item["_mass"]:1.3e}',
            )
            for item in animals
        )
        kwargs = dict(
            delimiter='_',
            fieldnames=['uuid', 'gender', 'mass'],
        )
    else:
        kwargs = dict(fieldnames=reader.fieldnames)
    with open(output_path, 'w') as fptr:
        writer = csv.DictWriter(
            fptr,
            extrasaction='ignore',
            **kwargs
        )
        writer.writeheader()
        for animal in animals:
            writer.writerow(animal)


if __name__ == '__main__':
    input_path = Path('animals_n.txt')
    output_path = Path('animals_s.txt')
    select_animals(input_path, output_path)
    with open(output_path) as generated:
        with open('s_animals_se.txt') as expected:
            assert generated.read() == expected.read()

    output_path = Path('animals_sc.txt')
    select_animals(input_path, output_path, True)
    with open(output_path) as generated:
        with open('s_animals_sce.txt') as expected:
            assert generated.read() == expected.read()
