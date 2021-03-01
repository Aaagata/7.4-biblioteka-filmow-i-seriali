import random

class Movie:
    def __init__(self, tytul, rok, gatunek, liczba_odtworzen):
        self.tytul = tytul
        self.rok = rok
        self.gatunek = gatunek
        self.liczba_odtworzen = liczba_odtworzen
    def __str__(self):
        return f"{self.tytul}({self.rok})"
    def __repr__(self):
        return f"tytul = {self.tytul}, rok = {self.rok}"
    def play(self, step = 1):
        self.liczba_odtworzen += 1
m1 = Movie(tytul="Gran Torino", rok="2008", gatunek="Dramat", liczba_odtworzen="2123852")
m2 = Movie(tytul="Pętla", rok="2020", gatunek="Sensacyjny", liczba_odtworzen="100542")
m3 = Movie(tytul="Jak zostałem gangsterem", rok="2019", gatunek="Sensacyjny", liczba_odtworzen="1253174")
m4 = Movie(tytul="Aviator", rok="2004", gatunek="Biograficzny/Dramat", liczba_odtworzen="3123456")
m5 = Movie(tytul="Listy do M.", rok="2011", gatunek="Komedia romantyczna", liczba_odtworzen="301856")
m6 = Movie(tytul="Most Szpiegów", rok="2015", gatunek="Dramat", liczba_odtworzen="333555777")
Movie_list = [m1, m2, m3, m4, m5, m6]
class Serial(Movie):
    def __init__(self, numer_odcinka, numer_sezonu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu
    def __str__(self):
        return f"{self.tytul} {numer_sezonu}{numer_odcinka}"   
    def __repr__(self):
        return f"tytul = {self.tytul} numer_sezonu = {self.numer_sezonu}, numer_odcinka = {self.numer_odcinka}" 
    def play(self, step = 1):
        self.liczba_odtworzen += 1
s1 = Serial(tytul="24 godziny", rok="2001", gatunek="Thriller", numer_odcinka="E05", numer_sezonu="S01", liczba_odtworzen="8543795")
s2 = Serial(tytul="M jak Miłość", rok="2000", gatunek="Obyczajowy", numer_odcinka="E08", numer_sezonu="S01", liczba_odtworzen="12456789")
s3 = Serial(tytul="Homeland", rok="2020", gatunek="Sensacyjny", numer_odcinka="E03", numer_sezonu="S08", liczba_odtworzen="12045684")
s4 = Serial(tytul="Ojciec Mateusz", rok="2019", gatunek="Kryminał", numer_odcinka="E26", numer_sezonu="S21", liczba_odtworzen="1597863")
s5 = Serial(tytul="Lucyfer", rok="2017", gatunek="Fantastyczny", numer_odcinka="E02", numer_sezonu="S03", liczba_odtworzen="369258147")
Serial_list = [s1, s2, s3, s4, s5]

biblioteka = [Movie_list] + [Serial_list]
print("Biblioteka filmów")
print(biblioteka)
def get_movies():
    by_tytul = sorted(biblioteka, key=tytul)
    if type(object) == "Movie":
        print("to jest film")
def get_series():
    by_tytul = sorted(biblioteka, key=tytul)
    if type(object) == "Serial":
        print("to jest serial")
def search(tytul):
    tytul_search = input("Podaj tytuł filmu lub serialu: ")
    if tytul_search == self.title:
        print(self.tytul, self.rok)
    else:
        print("Brak tytułu w bazie")
        exit(1)
def generate_views():
    random_view = random.choice(biblioteka)
    random_number = random.randrange(1, 100)
    print(random_view, random_number)
def generate_views10():
    for _ in range(10):
        generate_views()
ilosc = int(input("Podaj interesującą Cię liczbę TopTitles: "))
def top_titles():
    by_liczba_odtworzen = sorted(biblioteka, key=lambda liczba_odtworzen: liczba_odtworzen)
    licznik = 0
    for element in by_liczba_odtworzen:
        print(element)
        licznik += 1
        if licznik > ilosc:
            break
generate_views10()
top_titles()