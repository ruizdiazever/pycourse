lista = []
suma = 0

for i in range(0, 101, 1):
    if i % 2 == 0:
        lista.append(i)
print(lista)

for i in lista:
    suma += i
    print(suma)