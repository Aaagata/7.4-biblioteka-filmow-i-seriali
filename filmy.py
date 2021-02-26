from random import Random
random = Random

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
m1 = Movie("Gran Torino", "2008", "Dramat", "2123852")
m2 = Movie("Pętla", "2020", "Sensacyjny", "100542")
m3 = Movie("Jak zostałem gangsterem", "2019", "Sensacyjny", "1253174")
m4 = Movie("Aviator", "2004", "Biograficzny/Dramat", "3123456")
m5 = Movie("Listy do M.", "2011", "Komedia romantyczna", "301856")
m6 = Movie("Most Szpiegów", "2015", "Dramat", "333555777")
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
s1 = Serial("24 godziny", "2001", "Thriller", "E05", "S01", "8543795")
s2 = Serial("M jak Miłość", "2000", "Obyczajowy", "E08", "S01", "12456789")
s3 = Serial("Homeland", "2020", "Sensacyjny", "E03", "S08", "12045684")
s4 = Serial("Ojciec Mateusz", "2019", "Kryminał", "E26", "S21", "1597863")
s5 = Serial("Lucyfer", "2017", "Fantastyczny", "E02", "S03", "369258147")
Serial_list = [s1, s2, s3, s4, s5]

biblioteka = [Movie_list] + [Serial_list]

def get_movies():
    by_tytul = sorted(biblioteka, key=self.tytul)
    if type(object) == "Movie":
        print("to jest film")
def get_series():
    by_tytul = sorted(biblioteka, key=self.tytul)
    if type(object) == "Serial":
        print("to jest serial")
def search(tytul):
    tytul_search = input("Podaj tytuł filmu lub serialu: ")
    if tytul_search == self.title:
        print(self.tytul, self.rok)
    else:
        print("Brak tytułu w bazie")
        exit(1)
# def generate_views():
#     random_view = random.choice(biblioteka)
#     random_number = randrange(1, 100)
#     print(random_view, random_number)
# def generate_views10():
#     for _ in range(10):
#         generate_views()
ilosc = int(input("Podaj interesującą Cię liczbę TopTitles: "))
def top_titles():
    by_liczba_odtworzen = sorted(biblioteka, key=liczba_odtworzen)
    licznik = 0
    for element in biblioteka:
        print(element)
        licznik += 1
        if licznik < ilosc:
            break
print("Biblioteka filmów")
# generate_views10()
top_titles()