import random

class KodGenerator:
    def generuj_kod(self, dlugosc=4, unikalne=False, tryb='kolory', trudnosc=None):
        kolory_podstawowe = ['czerwony', 'zielony', 'niebieski', 'żółty', 'biały', 'czarny']
        kolory_rozszerzone = kolory_podstawowe + ['fioletowy', 'pomarańczowy']
        liczby_podstawowe = ['1', '2', '3', '4', '5', '6']
        liczby_rozszerzone = liczby_podstawowe + ['7', '8']
	
	#wybór trudności gry
        if trudnosc:
            if trudnosc == 'latwy':
                tryb = 'kolory'
                symbole = kolory_podstawowe
                dlugosc = 4
                unikalne = False
            elif trudnosc == 'sredni':
                tryb = 'kolory'
                symbole = kolory_podstawowe
                dlugosc = 6
                unikalne = False
            elif trudnosc == 'trudny':
                tryb = 'kolory_roz'
                symbole = kolory_rozszerzone
                dlugosc = 8
                unikalne = False
            else:
                print("Dostępne poziomy trudności to: 'latwy', 'sredni', 'trudny'")
                return []
	
        if tryb == 'kolory':
            symbole = kolory_podstawowe
        elif tryb == 'kolory_roz':
            symbole = kolory_rozszerzone
        elif tryb == 'liczby':
            symbole = liczby_podstawowe
        elif tryb == 'liczby_roz':
            symbole = liczby_rozszerzone
        else:
            print("Dostępne tryby to: 'kolory', 'liczby', 'kolory_roz', 'liczby_roz'")
            return []

        if unikalne and dlugosc > len(symbole):
            print(f"Nie można wygenerować unikalnego kodu - dostępnych symboli: {len(symbole)}, żądana długość: {dlugosc}")
            return []

        if unikalne:
            kod = random.sample(symbole, dlugosc)
        else:
            kod = [random.choice(symbole) for _ in range(dlugosc)]

        return kod
