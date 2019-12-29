## 1. (1 pkt):
Uzupełnij definicję funkcji `get_city_woeid` wykonującą zapytanie do API
`https://www.metaweather.com/api/` i zwracającą słownik `{miasto:woeid}`
pasujących do wysłanego zapytania. Tzn:
- jeżeli API nie zwróciła żadnego miasta ma być zwracany pusty słownik,
- w przypadku niepustej odpowiedzi z API ma zwrócić słownik wszystkich par,
    
## 2. (1 pkt.):
Uzupełnij definicję funkcji `get_city_data` służącą do zapisu danych 
historycznych dla miasta o danym `woeid`. 
Funkcja poza identyfikatorem miasta ma przyjmować ścieżkę do miejsca zapisu 
oraz rok i miesiąc danych do pobrania. 

Jeżeli:
 - podana jest ścieżka bezwzględna - nie edytuj ścieżki zapisu,
 - podana jest ścieżka względna - miejscem zapisu jest podana ścieżka 
 w folderze uruchomienia pliku,
 - ścieżka nie jest podana - użyj folderu uruchomienia jako miejsca zapisu.

Funkcja tworzy w podanej ścieżce folder, o nazwie `woeid_yyyy_mm` 
(`woeid` to id miasta, `yyyy` to pobrany rok, `mm` miesiąc, 
jeżeli folder już istnieje ten krok jest pomijany), 
do którego zapisuje pliki CSV z danymi z każdego dnia .
Plik ma mieć nazwę `yyyy_mm_dd.csv`. 

Funkcja zwraca ścieżkę do utworzonego folderu oraz listę nazw pobranych plików.

**Do zadań 1 i 2**:
Funkcja w przypadku błędu:
- parsowania odpowiedzi z API ma podnieść `RuntimeError` (wbudowany błąd Pythona),
- związanego z komunikacją (zły status odpowiedzi) ma zwracać 
`requests.exceptions.HTTPError`,
- timeoutu `requests.exceptions.Timeout`.

Funkcja pozwala na zdefiniowanie timeoutu w sekundach (domyślnie 5s).

## 3. (2 pkt.):
Wykorzystując bibliotekę `pandas` napisz funkcję  `concat_data` parsującą 
dane pobrane za pomocą funkcji z zadania 2. Funkcja ma wybierać 
z każdego pliku tylko te dane, które powstały w dniu którego dotyczą 
(tzn. data z kolumn `created` i`applicable_date` mają być sobie równe)
oraz generować plik zbiorczy (z wybranymi danymi) dla całego miesiąca. 

Plik ma zawierać następujące kolumny (w tej kolejności):
['created',
'min_temp',
'temp' (w odpowiedzi API kolumna 'the_temp'),
'max_temp',
'air_pressure',
'humidity',
'visibility',
'wind_direction_compass',
'wind_direction',
'wind_speed']
i nazywać się `woeid_yyyy_mm.csv`. Dane w pliku mają być posortowane 
rosnąco po dacie utworzenia. Format daty pliku `yyyy-mm-ddTHH:MM`: 
`y`, `m`, `d`, `H`, `M` odpowiadają cyfrom roku, miesiąca, dnia, godziny, 
minuty , `T` jest separatorem. 

Dodatkowo napisz plik `.gitignore`, który będzie wykluczał wszystkie pliki 
z rozszerzeniem `.csv` pobrane w ramach uruchomienia plików 
z zadaniami 2 i 3 (czyli pliki `.csv` z folderów `weather_data` 
i `523920_2017_03`).