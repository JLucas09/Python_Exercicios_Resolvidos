quantCigarros = int(input("Informe quantos cigarros por dia:"))
quantAnos = int(input("Informe quantos anos ja fuma:"))

minutosVida = (quantAnos * 365) * (quantCigarros * 10)
diasVida = minutosVida / 1440

print("Dias a menos de vida:", int(diasVida))
