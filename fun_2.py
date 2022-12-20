a = 10


def dodaj():
    global a
    a = 4
    b = 10
    print("Wynik=", a + b)


print("Wartosc a z gory", a)
dodaj()
print("Wartosc a z gory", a)
