quest = []

print("Responda apenas com 'S' para Sim ou 'N' para Nao")
print()
quest.append(input("Telefonou para a vítima?"))
quest.append(input("Esteve no local do crime?"))
quest.append(input("Mora perto da vítima?"))
quest.append(input("Tinha dívidas com a vítima?"))
quest.append(input("Já trabalhou com a vítima?"))
print("###########################")

if quest.count("S") == 2:
    print("Suspeita.")
elif quest.count("S") == 3 or quest.count("S") == 4:
    print("Cúmplice.")
elif quest.count("S") == 5:
    print("Assassino.")
else:
    print("Inocente.")
