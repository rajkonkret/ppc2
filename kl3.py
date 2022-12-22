import sys


class Dom:
    """
    To jest klasa Dom
    """

    def __init__(self, metraz, kolor, ilosc_okien):
        self.__metraz = metraz
        self.kolor = kolor
        self.__ilosc_okien = ilosc_okien

    def zmien_metraz(self):
        wybor = int(input("Podaj nowy metraz"))
        self.__metraz = wybor
        print("Metraz wynosi", self.__metraz)

    def zmien_kolor(self):
        wybor = input("Podaj nowy kolor")
        self.kolor = wybor
        print("Kolor wynosi", self.kolor)
        self.__farba()

    def zmien_okna(self):
        wybor = int(input("Podaj ilosc_okien"))
        self.__ilosc_okien = wybor
        print("Metraz wynosi", self.__ilosc_okien)

    def sprawdz_kolor(self):
        return self.kolor

    def __farba(self):
        print("Skonczyła sie farba")


dom1 = Dom(23, "czerwony", 5)
print(dom1.kolor)
print(dom1)
dom1.zmien_metraz()
dom1.metraz = 99
dom1.zmien_okna()
dom1.zmien_kolor()
