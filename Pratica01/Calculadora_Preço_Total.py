#Esse codigo tem objetivo de calcular o preco total de um produto 

#Variaveis com detalhes do produto 
nome_produto = "Cadeira Infantil"
preço_unitário = 12.40
quantidade = 3

#Variavel com o calculo do valor total
preco_total =quantidade * preço_unitário

#Exibição das informações do produto e do valor total 
print(f"Produto: {nome_produto}")
print(f"Preço unitario: R$ {preço_unitário: .2f}")
print(f"Quantidade: {quantidade}")
print(f"Preço Total: R$ {preco_total: .2f}")

#: .2f => Seja exibido duas casas decimais, como utilizamos em representação monetaria.
