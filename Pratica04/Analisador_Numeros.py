
def analisador_numeros ():
    pares = 0
    impares = 0

    while True:
        try:
            entrada = input("Digite um número inteiro (ou 'fim' para encerar): ")

            if entrada.lower() == "fim":
                break
            numero = int(entrada)
            if numero % 2 == 0:
                print(f"O número {numero} é par.")
                pares = pares + 1
            else:
                print(f"O número {numero} é impar.")
                impares = impares + 1
        except ValueError:
            print("Valor inválido. Por favor, insira apenas números inteiros.")

    print(f"""
    Resultado final:
    Quantidade de números pares: {pares}
    Quantidade de números impares: {impares}
    """)

analisador_numeros()