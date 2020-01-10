## 1. (5 pkt):
Napisz testy do klasy `Calculator` z pliku `tools/calculator`:
* test metody `run` dla wszystkich działań 
z wykorzystaniem parametryzacji (1 pkt.)
* testy metody do wychwycenia wszystkich możliwych błędów (3 pkt.).
Zwróć uwagę na:
    * kolejność podnoszenia testów,
    * typ wejścia (np. parametr przekazany jako string a jako inny typ)
Napisz fixturę `calculator` do testów, zwracającą instancję kalkulatora.
Okreś jej zakres w taki sposób, żeby testy pozostały atomowe.
Testy umieść w katalogu `tests`.
## 2. (3 pkt.):
Napisz testy do metody `get_cities_woeid` wykorzystujące mockowanie analogiczne
do bloku main w pliku.
Podpowiedź: mockując metodę `requests.get` pamiętaj o tym co powinna zwracać
i jakie atrybuty/metody ma mieć zwracany mock.