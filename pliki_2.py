fh = open('dane.txt', 'a')
fh.write("Test nr 11\n")
fh.write("Test nr 12\n")
fh.write("Test nr 13\n")
fh.close()

with open('dane.txt') as fh:
    for lines in fh:
        print(lines.strip())

lista = [1, 2, 3, 4]
tmp = str(lista)
print(tmp)

with open('dane.txt', 'w') as fh:
    fh.write(str(lista))

with open('dane.txt', 'r') as fh:
    lines = fh.read()
    print(lines)

lista3 = []
with open('dane.txt', 'r') as fh:
    for line in fh:
        print(line)
        lista3.append(line)

print(lista3)
print(type(lista3))
print(lista3[0][3])
# csv wartosci oddzielone przecinkiem, srednikiem itd.
