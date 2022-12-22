class Human:
    """
    Klasa Human opisujaca człowieka
    """

    def __init__(self, imie, wiek=0, plec='k'):
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

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

    # def __str__(self):
    #     return "imie= " + self.imie + " plec=" + self.plec


osoba1 = Human("Radek")
print(osoba1.wiek)
print(osoba1.plec)
print(osoba1)
osoba1.ruszaj()
osoba1.plec = "m"
osoba1.ruszaj()

osoba2 = Human("Radek", 50, "m")
print(osoba2.imie)
print(osoba2.plec)
