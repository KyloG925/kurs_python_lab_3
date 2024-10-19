import csv
import random
import pathlib
from pathlib import Path
global SumA #suma Computation time dla modelu A - nalezy ja odczytac
SumA = 0

#przyklad_uzycia
#odczytCSV('/home/students/inf/k/ab123456/PycharmProjects/pythonProject2/')
#zapisCSV('/home/students/inf/k/ab123456/PycharmProjects/pythonProject2/')

def odczytCSV(sciezka):
    global SumA
    sciezkaPliku = sciezka + "Solution.csv"
    with open(sciezkaPliku, 'r') as plik:
        czytelnik = csv.reader(plik)
        it = 0
        for wiersz in czytelnik:
            if it == 1:
                print(wiersz)  # wiersz to lista zawierająca dane z pojedynczego wiersza pliku
                if wiersz[0] == "A":
                    SumA += int(wiersz[1])
            it += 1


def zapisCSV(sciezka):
    with open('Solution.csv', 'w', newline='') as plik:
        letter = chr(random.randrange(65, 65 + 3))
        number = random.randint(0, 1000)
        seconds = random.randint(0, 1000)
        seconds = str(seconds)
        seconds += 's'
        pisarz = csv.writer(plik)
        pisarz.writerow(['Model', 'Optput value', 'Time of computation'])
        pisarz.writerow([letter, number, seconds])

