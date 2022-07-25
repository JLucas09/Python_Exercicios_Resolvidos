lista = []
num = int(input("Informe o limite para verificação dos números primos:"))

for cc in range(1, num + 1):
    cont = 0

    for x in range(1, num + 1):
        if cc % x == 0:
            cont += 1

    if cont == 2:
        lista.append(cc)

print(lista)
