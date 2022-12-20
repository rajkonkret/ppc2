# licznik = 0
#
# while True:
#     licznik += 1
#     print("Komunikat...")
#     if licznik == 10:
#         break
#
# print(licznik)
# licznik = 0
# while licznik < 10:
#     print("Komuniakt..")
#     licznik += 1
#
# lista = []
#
# while True:
#     wejscie = input("Podaj liczbe")
#     if wejscie.lower() == "s":
#         break
#     lista.append(wejscie)

# print(lista)
while True:
    print("""
    Kalkulator
    """)
    a = float(input("Podaj liczbe 1:"))
    b = float(input("Podaj liczbe 2:"))
    print("""
        1. Dodawanie,
        2. Odejmowanie,
        3. Mnożenie,
        4. Dzielenie,
        5+. Koniec
    """)
    odp = input("Podaj opcje (1-5)")

    if odp == "1":
        print(f"Wynik dodawania {a} + {b} = {a + b} ")
    elif odp == "2":
        print(f"Wynik odejmowania {a} - {b} = {a - b} ")
    # wynik dodawania a + b = wynik
    elif odp == "3":
        print(f"Wynik mnozenia {a} * {b} = {a * b} ")
    elif odp == "4":
        if b != 0:  # różne
            print(f"Wynik dzielenia {a} / {b} = {a / b} ")
        else:
            print("Nie dziel przez zero")
    else:
        print("Dziekujemy")
        break
