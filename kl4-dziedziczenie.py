from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisujaca Ptaka
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "lece  szybkocia", self.szybkosc)

    @abstractmethod
    def wydaj_odglos(self):
        pass


class Orzel(Ptak):
    """
    to ja orzel
    """

    def poluj(self):
        print("Tu", self.gatunek, "Rozpoczynam polowanie")

    def wydaj_odglos(self):
        print("piiiii")


class Kura(Ptak):

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)
        self.gatunek = gatunek

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def dziobanie(self):
        print("Tu", self.gatunek, "Ide sobie podziobac")

    def wydaj_odglos(self):
        print("Kokokokoko")


# orzel = Ptak("Orzel", 5)
# print(orzel.szybkosc)
# orzel.latam()

kura = Kura("Kura")
kura.latam()
kura.dziobanie()
kura.wydaj_odglos()
orzel2 = Orzel("orzel", 10)
orzel2.latam()
orzel2.poluj()
orzel2.wydaj_odglos()
