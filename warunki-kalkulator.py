print("""
    Kalkulator
    """)
a = int(input("Podaj liczbe 1:"))
b = int(input("Podaj liczbe 2:"))

odp = input("1. Dodawanie, 2. Odejmowanie, 3. Mnożenie, 4. Dzielenie")

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
