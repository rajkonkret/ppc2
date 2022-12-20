slownik = {}

slownik['imie'] = 'radek'
print(slownik)
slownik['wiek'] = 39
print(slownik)
print(len(slownik))

print(slownik.items())
print(slownik.keys())
print(slownik.values())
print(slownik['imie'])

lista = [44, 55, 66, 77, 88, 33, 22, 11, 55, 33, 11]
slownik['liczby'] = lista
print(slownik['liczby'])
print(slownik['liczby'][0])
# wypisz element o indexie 7
print(slownik['liczby'][7])

lista2 = [44, 55, 66, 11]
nowa_lista = lista + lista2
print(nowa_lista)

slownik2 = {'imie': ['Radek', 'Krzysztof']}
print(slownik2)
print(slownik2['imie'][1])

slownik3 = {"cat": "kot", "name": "imie", "learn": "uczyc sie (Pythona)"}

# print("Mam takie słowa w słowniku", slownik3.keys())  # ctrl + / - komentarz
# key = input("Podaj wyraz do przetłumaczenia")  # input zwraca str
# print(slownik3[key])
# dodac klikla innych slówek do słownika, wyswietlic inne tłumaczenia

li1 = int(input("Podaj liczbe 1"))
li2 = int(input("Podaj liczbe 2"))
print(li2 + li1)
