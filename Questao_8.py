contPar = 0
contImpar = 0

for i in range(10):
    num = int(input("Informe um numero:"))

    if num % 2 == 0:
        contPar += 1
    else:
        contImpar += 1

print()
print("Quantidade de números pares:", contPar)
print("Quantidade de números impares:", contImpar)
