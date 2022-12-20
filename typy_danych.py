wiek = 47
rok = 2022
temp = 36.6  # float
wiek2 = 37.5

# wypisac typ zmiennej temp
print(type(temp))
print(type(wiek2))

print(wiek * rok)  # ctrl+D  - kopiowanie lini
print(wiek - rok)
print(wiek + rok)
print(wiek / rok)  # wynikiem dielenia jest float
print(wiek // rok)  # wynik dzielenia - czesc całkowita
print(wiek ** rok)  # potegowanie
print(type(wiek ** rok))
print(54 - (5 * 43) + (4 / 2 + 4) / 2)

print("\tSprawdzam zmienna temp {} {}\n".format(wiek, temp))  # \t - tabulator, \n - nowy wiersz
print(f"\tSprawdzam zmienna wiek {wiek}  {temp}")

print(f"""
    zmienna {temp}
    zmienna {wiek}
    Wynik działania:
    {54 - (5 * 43) + (4 / 2 + 4) / 2}
""")

imie = "Radek Radek"
print(imie)
imie.lower()
print(imie)
imie_2 = imie.lower()
print(imie_2)

print(imie.upper())
print(imie.capitalize())

print(wiek)
imie = imie.lower()
print(imie)
print(imie.count("radek"))

print(4 / 2)
print(type(4 / 2))
print(4 // 2)
print(type(4 // 2))
print(2.0)

print("False/True")
czy_znasz_Python = True
print(czy_znasz_Python)
print(int(czy_znasz_Python))  # 1 - True, 0 - False
print(type(czy_znasz_Python))
