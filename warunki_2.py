lista = []
lang = input("Wpisz znany Ci jezyk programowania")

match lang.lower():
    case "python":
        lista.append(lang)
    case "java":
        lista.append(lang)
    case "c#":
        lista.append(lang)
    case "c++":
        lista.append(lang)
    case _:
        print("nie ma takiego jezyka;)")

print(lista)
