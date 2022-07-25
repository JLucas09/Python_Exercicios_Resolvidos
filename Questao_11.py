cont = 0
N = int(input("\nDigite o número de pessoas:"))

for i in range(N):
    idade = int(input(f"Digite a idade da {i+1} pessoa:"))
    cont += idade
media = cont / N
print("Media de idade:", media)

if media <= 25:
    print("Media Jovem")
elif media > 25 and media <= 60:
    print("Media Adulta")
else:
    print("Media Idosa")
