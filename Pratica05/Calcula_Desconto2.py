def caclcula_desconto (preco, percentual_desconto):
    desconto = preco * (percentual_desconto / 100)
    preco_final = preco - desconto
    return round(preco_final)

while True:
   try:
        #Solicitando os dados para o usuário 
        preco_original = float(input("Digite o preço do produto: "))
        desconto = float(input("Digite o percentual do desconto: "))

        #Verificação dos valores sempre positivos
        if preco_original < 0 or desconto < 0:
            print("Erro. O preço e o desconto devem ter valores positivos.")
            continue
        break
   except ValueError:
       print("Por favor, insira um valor númerico.")
       continue

preco_com_desconto = caclcula_desconto(preco_original, desconto)
print(f"O preço final com desconto {desconto}% é de R${preco_com_desconto}")