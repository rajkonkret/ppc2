def mnozenie(a, b):
    try:
        print(int(a) * int(b))
    except ValueError:
        print("Błąd wartosci")
    except TypeError:
        print("Błąd typu")
    except Exception as e:
        print("Inny bład")
    else:
        print("Inny bład")
    finally:
        print("zawsze")


# by wychwyciłą dzielenie przez zero
def dzielenie(a, b):
    try:
        print(int(a) / int(b))
    except ValueError:
        print("Błąd wartosci")
    except TypeError:
        print("Błąd typu")
    except ZeroDivisionError:
        print("nie dziel przez zero")
    else:
        print("poszło")


mnozenie(2, 3)
mnozenie(2, "3")
mnozenie("a", "3")
mnozenie("2", "3")
mnozenie((2,), "3")
print("Program działa dalej")
dzielenie(2, 0)  # ZeroDivisionError
