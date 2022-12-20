czy_znasz_Python = False

if czy_znasz_Python:
    print("Brawo")
else:
    print("Musisz sie dalej uczyc")

print("koniec")

podatek = 0.0
zarobki = int(input("Podaj swoj dochod"))
if zarobki < 10000:
    podatek = 0.0
elif zarobki < 30000:
    podatek = 0.2
elif zarobki < 100000:
    podatek = 0.35
else:
    podatek = 0.40

print(f"Zapłacisz {zarobki * podatek} zł")

suma_zam = 247
if suma_zam > 100:
    rabat = 25
else:
    rabat = 0
print('suma zam:', suma_zam, "rabat:", rabat)

rabat2 = 25 if suma_zam > 100 else 0
print(f"suma zam: {suma_zam} rabat: {rabat2}")

lista_bledow = []
alert_system = 'email'
error = 'inny'
error_message = "Stało sie cos strasznego"

if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    if error == 'critical':
        lista_bledow.append('critical')
    elif error == 'medium':
        lista_bledow.append('medium')
    else:
        lista_bledow.append("nieznany")

print(lista_bledow)
