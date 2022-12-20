a = 5
b = 6


def dodaj():
    print("Wynik=", a + b)


def dodaj2(a, b):
    return a + b


def odejmij(a, b, c=0):
    return a - b - c


def mnozenie(a, b):
    return a * b


def oblicz_vat(cena, vat):
    return cena * (100 + vat) / 100


oblicz_vat2 = lambda cena, vat: cena * (100 + vat) / 100
print(oblicz_vat(100, 23))
print(oblicz_vat2(100, 23))

odejmij2 = lambda a, b: a - b
print(odejmij2(1, 2))
print(odejmij2(b=2, a=6))

x = 7
y = 10
print(odejmij2(b=2, a=6))

x = 5
dodaj()
print(dodaj2(5, 4))
print(odejmij(9, 7))
print(odejmij(x, 2, 7))
print(mnozenie(odejmij(2, 3), dodaj2(3, 4)))
