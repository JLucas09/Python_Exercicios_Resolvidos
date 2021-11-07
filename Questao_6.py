valorImovel = float(input("Informe o valor do imovel:"))
salario = float(input("Informe o salario:"))
quantMeses = int(input("Informe a quantidade de parcelas:"))

valorParcela = valorImovel / quantMeses
salPres = salario * 0.3

if valorParcela <= salPres :
    print("financiamento imobiliario aprovado!")
else:
    print("financiamento imobiliario reprovado!")