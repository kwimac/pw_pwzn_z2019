## 1. (2 pkt):
Napisz generator zwracający liczby z ciągu Fibbonaciego.
Generator może przyjąć jednen parametr - liczbę n (integer) pierwszych liczb
ciągu, które ma zwrócić generator. 
Generator może zwrócić maksymalnie 100 minimalnie 1 liczbę ciągu.
Przy podaniu złej wartości parametru funckja ma podnosić `RuntimeError`

Podpowiedź: Funkcja może zawierać więcej niż jedno `yield`.
## 2. (2 pkt.):
Napisz dekorator logujący (z datą logu w formacie `YYYY-mm-ddTHH:MM:SS`):
* nazwę udekorowanej funkcji
* liczbę parametrów pozycyjnych
* nazwy parametrów opcjonalnych (lub `-` jeżeli nie było żadnych)
* wartość zwracaną
* czas wykonania (tylko funkcji nie dekoratora)

Przykładowe logi (do wywołań z zadania):
>2020-01-23T21:09:55| function sum called with:
>
>1 postional parameters
>
> optional parameters: -
>
>returned: 6 (1.43e-06s)
>
>2020-01-23T21:09:55| function fun called with:
>
>3 postional parameters
>
>optional parameters: bb
>
>returned: None (1.43e-06s)

Podpowiedź:
* nazwa funkcji znajduje się w dunderze `__name__`
