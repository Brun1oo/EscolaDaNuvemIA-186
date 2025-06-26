#Informações sobre o produto
nome_do_produto = "Camiseta"
preco_original = 50.00
porcentagem_de_desconto = 20

#Cálculo do desconto
valor_desconto = preco_original * (porcentagem_de_desconto / 100)

#Cálculo do produto com o desconto
preco_com_desconto = preco_original - valor_desconto

#Exibição para usuário
print(f"Nome do produto: {nome_do_produto}")
print(f"Preço Original: R$ {preco_original: .2f}")
print(f"Porcentagem do desconto: {porcentagem_de_desconto} %")
print(f"Valor do desconto: {valor_desconto: .2f}")
print(f"Valor do produto com desconto: R$ {preco_com_desconto: .2f}")