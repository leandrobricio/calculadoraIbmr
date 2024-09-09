
def calculadora(operacao, num1, num2):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero!"
    else:
        return "Operação inválida!"



def programa_calculadora():
    print("Bem-vindo à calculadora!")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /): ")

    resultado = calculadora(operacao, num1, num2)
    print(f"O resultado da operação é: {resultado}")



programa_calculadora()
