A = 80000
taxaA = 0.03
B = 200000
taxaB = 0.015
anos = 0

while A <= B:
    A += (A * taxaA)
    B += (B * taxaB)
    anos += 1

print("Populacao atual A:", A)
print("Populacao atual B:", B)
print("Necessario", anos, "anos para a populacao A passar a B")