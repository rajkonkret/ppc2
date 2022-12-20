import random

lista = []
for i in range(10):
    if i % 2 == 0:  # % - modulo czyli reszta z dzielenia 5 % 2 = r 1
        print(i)
        lista.append(i)

print(lista)

lista2 = list(range(1, 50))
print(lista2)
for i in range(6):  # od 0 do 5
    wyn = random.choice(lista2)
    print(wyn)
    lista2.remove(wyn)

for i in range(5):
    print(i * "*")

for cyfra in lista:
    if cyfra == 2:
        cyfra += 1  # cyfra = cyfra +1  *=,
    print(cyfra)

lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)

imiona = ["Radek", "Zenek", "Marta"]
for p in imiona:
    print(p)

for p in range(len(imiona)):  # range(3)
    print(p, imiona[p])

for pozycja, wartosc in enumerate(imiona):
    print(pozycja, wartosc)

imie = "Radek"

for p, w in enumerate(imie):  # enumerate => p = index, w = imie[p]
    print(p, w)

ludzie = ["Radek", "Janek", "Asia", "Michał"]
wiek = [47, 67, 32, 34]
jezyk = ["java", "python"]

for pozycja, osoba in enumerate(ludzie):  # enumerate => p = index, w = imie[p]
    print(pozycja, osoba)

for pozycja, osoba in enumerate(ludzie):  # enumerate => p = index, w = imie[p]
    print(pozycja, osoba, wiek[pozycja])

for osoba, wiek, jezyk in zip(ludzie, wiek, jezyk):
    print(osoba, wiek, jezyk)

slownik = {"imie": "Radek", "nazwisko": "Kowalski"}
for k in slownik:
    print(k)

for v in slownik.values():
    print(v)

for k, v in slownik.items():
    print(k, "=>", v)

slownik = {"imie": "Grzes", "nazwisko": "Markiewic"}
for k in slownik:
    print(k)

for v in slownik.values():
    print(v)

for k, v in slownik.items():
    print(k, "=>", v)

print({value: key for key, value in slownik.items()})
# slownik[value] = key
