class porownywanie_odp:

    def __init__(self, kod): #zapisanie do późniejszego użycia wygenerowanej przez kod poprawnej sekwencji kolorów
        self.kod = kod

    def porownanie(self, odpowiedz): #odpowiedź to lista zawierająca sekwencje kolorów, wprowadzana przez gracza trzeba zaimplementować wprowadzanie odpowiedzi
        if len(odpowiedz) != len(self.kod):
            raise ValueError("Błędna długość zgadywanej sekwencji") #wyrzuca błąd kiedy dłguość listy opdpowiedz różni się od dł listy kod

        #zmienne zliczające ilość poprawnych kolorów + miejsc oraz poprawnych kolorów ale złych miejsc:
        dobra_odpowiedz = 0
        dobry_kolor = 0

        #kopie orginalnych list do modyfikaacji:
        kod_kopia = self.kod.copy()
        odpowiedz_kopia = odpowiedz.copy()

        for x in range(len(odpowiedz)):
            if odpowiedz[x] == self.kod[x]:
                dobra_odpowiedz += 1 #zliczenie poprawnych trafien
                # zaznaczenie na kopi listy poprawnych odpowiedzi:
                odpowiedz_kopia[x] = None
                kod_kopia[x] = None

        for x in range(len(odpowiedz)):
            if odpowiedz_kopia[x] and odpowiedz_kopia[x] in kod_kopia:
                dobry_kolor += 1
                indeks = kod_kopia.index(odpowiedz_kopia[x])
                odpowiedz_kopia[indeks] = None #usunięcie koloru żeby się nie powtarzał

        #return wartości, w wypadku len(kod) == dobra_odpowiedz użytkownik zgadł wszytko dobrze, w przeciwnym wypaadku należy wywołać funkcję ponownie z nową odpowiedzią
        return dobra_odpowiedz, dobry_kolor


