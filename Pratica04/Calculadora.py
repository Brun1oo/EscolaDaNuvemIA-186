while True:
    try:
        num1 = float(input("Digite um número: "))
        num2 = float(input("Digite um outro número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == "+":
            resultado = num1 + num2 
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            resultado = num1 / num2
        else:
            raise ValueError("Operação Inválida")
        
        print(resultado)
        break

    except ValueError as erro: 
        print(f"Erro {erro}. Por Favor, tente novamente.")
    except ZeroDivisionError:
        print("Erro: divisão por zero não é permitida. Por favor, tente novamente.")
