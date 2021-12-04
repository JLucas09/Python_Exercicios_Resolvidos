quantAnos = int(input("Informe quantos anos a pessoa fuma:"))
quantCigarros = int(input("Informe quantos cigarros por dia:"))

minutosVida = (quantAnos * 365) * (quantCigarros * 10)
diasVida = minutosVida / 1440

print("Dias a menos de vida:",int(diasVida))
