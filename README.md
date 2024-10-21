# Rozwiązanie grupowego zadania domowego z labu 3 (Kurs Pythona)

Krzysztof Głowiński kg439929 - utworzenie git repo oraz parsowanie argumentów

Konrad Kedzierski kk459164 - Obsluga (zapis i odczyt) plikow .csv.

Tymoteusz Fedorowski tf458956 - Obsluga (zapis i odczyt) plikow .json

Piotr Ochal po459457 - Generowanie ścieżek do plików na podstawie argumentów

(...) [możecie się wpisać]

# Przykład użycia funkcji parsowania argumentów:

```
from parse_arguments import parse_arguments

months, days, times, operation, file_type = parse_arguments()
[reszta skryptu]
```
Skrypty używające tego parsowania należy odpalać: 
```
python3 [nazwa skryptu].py -m [miesiące] -d [przedziały dni] -t [r/w] -o [t/u] -c/-j
```
np.
```
python3 parse_arguments.py -m styczen luty listopad -d pn-pt pt czw -t r r w -o u -c
```
W pliku parse_arguments.py w komentarzu dostępny jest opis funkcji wraz z informacją, co ona zwraca.

Gdybyście mieli jakieś pytania/problemy piszcie.
