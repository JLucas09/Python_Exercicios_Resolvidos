contA = 0
contB = 0
contC = 0
cont0 = 0

for i in range(20):
    voto = input('''
    Candidatos diponiveis:
     Candidato A 88
     Candidato B 51
     Candidato C 39
    Informe seu voto:''')

    if voto.upper() == "A" or voto == "88":
        contA += 1
    elif voto.upper() == "B" or voto == "51":
        contB += 1
    elif voto.upper() == "C" or voto == "39":
        contC += 1
    else:
        print("Voto nulo")
        cont0 += 1

print()
print("-------- Resultados --------")
print("Votos para o candidato A:", contA)
print("Votos para o candidato B:", contB)
print("Votos para o candidato C:", contC)
print("Votos nulos:", cont0)
