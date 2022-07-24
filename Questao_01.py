preco = float(input("Informe o preço do produto:"))
desconto = float(input("Informe o percentual de desconto:"))

valorDesconto = preco * (desconto / 100)
precoFinal = preco - valorDesconto

print(f"O valor do desconto e: {valorDesconto}%")
print("O valor atual com o desconto aplicado:", precoFinal)
