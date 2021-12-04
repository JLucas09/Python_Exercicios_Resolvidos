weather = []
meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho",
    "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

for mes in range(12):
    weather.append(float(input(f"Informe a temperatura do mes {meses[mes]}:")))

media = sum(weather) / len(weather)

print()
print("Temperatura média anual:", media)
print()

print(".____ Meses acima da média ____.")
for i, mes in enumerate(weather):
    if mes > media:
        print(f"mes: {meses[i]} Temperatura: {mes}")
