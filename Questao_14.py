notas = []
rng = 0

while rng >= 0:
    rng = float(input("Informe a nota do estudante:"))

    if rng < 0:
        break
    else:
        notas.append(rng)

print()

print(f"Quantidade de notas lidas: {len(notas)}")  # Quantidade de notas
print(notas)  # Lista na ordem
notas.reverse()  # Invertendo a ordem
print(notas)  # Lista inversa
print(f"A soma de todas as notas e: {sum(notas)}")  # Soma de todas as notas
media = sum(notas) / len(notas)  # Calculo da media
print(f"A media das notas e: {media}")  # Media de todas as notas
print()
for rng in notas:  # Exibicao das notas maiores que a media
    if rng > media:
        print("Nota maior que a media:", rng)
