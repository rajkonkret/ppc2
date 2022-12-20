lista = []
lista.append("Radek")
lista.append("Magda")
lista.append("Renata")
lista.append("Renata")

print(lista)
lista.insert(1, "Renata")
print(lista)
lista[1] = "Krzysiek"
print(lista)
lista.remove("Renata")
print(lista)
lista.reverse()
print(lista)
lista2 = lista.copy()
lista.clear()
print(lista)
print("Koniec" in lista2)

liczby = [54, 999, 34, 12, 22.56, 0xa, 876, 78]
liczby.sort()
print(liczby)
liczby.reverse()
print(liczby)
liczby2 = liczby.copy()
print(liczby2)
liczby2[0] = 6666
print(liczby2)
print(liczby2[0:3])
print(liczby2[:3])
print(liczby2[2:])
print(liczby2[:-1])
# usunac z liczby2 liczbe 54
# wypisac liste
# wypisac liste ale tylko indexy od 2 do 5 włącznie
print(len(liczby2))
liczby2.remove(54)
print(liczby2)
print(liczby2[2:6])  # 6 bo chcemy wyswietlic index 5 a indexy sa od 0
print(len(liczby2))

krotka = tuple(liczby2)
print(krotka)

13:45