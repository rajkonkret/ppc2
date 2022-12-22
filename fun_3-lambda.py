odejmij = lambda a, b: a - b  # nazwa =  def, argumenty, return

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")

print(wiek(5))
print(wiek(15))
print(wiek(25))

lista = [1, 2, 7, 8, 10, 55]
print(f"Zastosowanie map: {list(map(lambda x: x * 2, lista))}")
print(f"Zastosowanie filter: {list(filter(lambda x: x < 3, lista))}")
print(f"Zastosowanie filter: {list(filter(lambda x: x > 8, lista))}")
print(f"Zastosowanie filter: {list(filter(lambda x: 3 < x < 20, lista))}")
# 3 < x < 20 - przedział 3 do 20
