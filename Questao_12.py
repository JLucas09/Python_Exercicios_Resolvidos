resul = 0
listaP = []

for i in range(10):
    print("Informe 'V' para Vitória, 'E' para Empate e 'D' para Derrota.")
    listaP.append(input(f"Qual foi o resultado da {i+1} partida:").upper())

for cc in range(10):
    if listaP[cc] == "V":
        resul += 10
    elif listaP[cc] == "E":
        resul += 5
    elif listaP[cc] == "D":
        resul -= 2

print("Sua pontuação foi:", resul)

if resul >= 60:
    print("##__Subiu de patente__##")
elif resul >= 21 and resul < 60:
    print("##__Permanece na mesma patente__##")
else:
    print("##__Caiu patente__##")
