class Human:
    """
    To jest klasa Human opisująca człowieka w Pythonie
    """

    plec = ""
    imie = ""
    wiek = None

    def powitanie(self):
        """
        Metoda w klasie Human
        :return: wypisuje imie obiektu
        """
        print("Nazywam sie", self.imie)

    def ruszaj(self):
        if self.plec == 'k':
            print("Ruszyłam w droge")
        elif self.plec == 'm':
            print("Ruszyłem w droge")
        else:
            print("Ruszyłom w droge")


osoba1 = Human()
print(Human.powitanie.__doc__)  # dokumentacja klay
print(osoba1.wiek)
osoba1.wiek = 47
osoba1.imie = "Radek"
print(osoba1.wiek)
print(osoba1.imie)
osoba1.powitanie()
# Tworzymy obiekt klasy Human np.: osoba2

osoba2 = Human()
Human.powitanie.__doc__  # dokumentacja klay
print(osoba2.wiek)
osoba2.wiek = 32
osoba2.imie = "Ela"
osoba2.plec = "k"
print(osoba2.wiek)
print(osoba2.imie)
osoba2.powitanie()
osoba2.ruszaj()
