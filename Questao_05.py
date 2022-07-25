num1 = float(input("Informe o primeiro numero:"))
operacao = input("Escolha a operacao(+, -, *, /):")
num2 = float(input("Informe o segundo numero:"))

if operacao == '+':
    Resultado = num1 + num2

elif operacao == '-':
    Resultado = num1 - num2

elif operacao == '*':
    Resultado = num1 * num2

elif operacao == '/':
    if num2 == 0:
        print("Nao e possivel dividir por 0!")
        Resultado = "Invalido"
    else:
        Resultado = num1 / num2

else:
    print("Operacao invalida!")
    Resultado = "Invalida"

print("O resultado da operacao foi:", Resultado)
