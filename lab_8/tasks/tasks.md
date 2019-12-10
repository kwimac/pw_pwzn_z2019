Celem zadania jest skonfigurowanie środowiska korzystającego 
z Jupyter Notebooka. 

Wszystkie pliki tworzone w ramach zadań mają być tworzone 
w folderze `lab_8/tasks`. Proszę nie dodawać folderu środowiska wirtualnego 
do repozytorium. **Wyniki proszę nadsyłać do przyszłego czwartku do 23:59.**


## 1. (1 pkt):
Stwórz czyste środowisko wirtualne oparte o Pythona przynajmniej 3.6.
Dodaj do niego paczki: `jupyter`, `jupytext`, `matplotlib`.
Stwórz requirementsy dla środowiska i dodaj je do repozytorium.
Listę komend potrzebnych do uruchomienia środowiska umieść w pliku `Readme.md`.
## 2. (1 pkt):
Sprawdź czy na twojej maszynie istnieje konfiguracja jupytera:
```
jupyter --config-dir
```
Jeżeli nie istnieje, utwórz ją zgodnie z [dokumentacją](
https://jupyter-notebook.readthedocs.io/en/stable/config.html).
W odpowiednim miejscu konfiguracji dodaj następujące linijki:
```
c.NotebookApp.contents_manager_class="jupytext.TextFileContentsManager"
c.ContentsManager.default_jupytext_formats = ".ipynb,.Rmd"
```
Skopiuj zawartość katalogu, w którym stworzyłeś repozytorium 
do folderu `config/` i dodaj go do repozytorium.
## 3 (2 pkt):
* Stwórz nowy plik: `analiza.Rmd` i dodaj go do repozytorium. 
W repozytorium nie może być plik z rozszerzeniem `.ipynb`!
* Utwórz folder z zależnościami `tools`. 
Do folderu dodaj plik z funkcją `least_sq` z poprzednich laboratoriów. 
Zmień nazwę pliku na `fit_funcs.py`

W notebooku `analiza.Rmd`:
* dodaj kod pozwalający na wczytanie pliku ze ścieżki `data/input01.txt` 
z wykorzystaniem `numpy`. Plik zawiera ustrukturyzowane dane 
z niepewnością pomiarową. 
* Dopasuj do punktów prostą z wykorzystaniem funkcji `least_sq` dodanej
 w module `lib`.
* Sprawdź, niepewność względna których punktów przekracza 5%. 
Wykonaj dopaswanie tylko dla punktów, 
których niepewność pomiarowa nie przekraczaja 5%.
* Wykreśl wczytane dane, wraz z niepewnością pomiarow
ą (rozmiar znacznika punktu 2). 
Punkty, których niepewność pomiarowa nie przekracza 5% 
mają być wykreślone czarnymi kwadratami. 
Punkty przekraczające - czerwonymi trójkątami.
* Wykreśl dopasowane proste przerywaną linią. Dodaj legendę. 
Prosta dopasowana do wszystkich punktów ma się nazywać `all` (kolor niebieski), 
prosta z ograniczeniem `Δ<5%` (kolor zielony).
* W pliku powinna znajdować się linijka wyświetlająca tylko skończony wykres 
oraz druga pozwalająca na zapisanie go do pliku `fitted_input01` 
w fromacie `png`, z rozdzielczością 100 dpi.
* Uzyskany wykres ma wyglądać jak `exaple.png`
