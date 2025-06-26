#Informações sobre o dinheiro
valor_em_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

#A conversão do dinheiro (Real para euro e dolar)
valor_em_dolar = valor_em_reais / taxa_dolar
valor_em_euro = valor_em_reais / taxa_euro

#Exibição para o usuário
print(f"Valor em Reais: R$ {valor_em_reais: .2f}")
print(f"Valor em Dolares: $ {valor_em_dolar: .2f}")
print(f"Valor em Euros: € {valor_em_euro: .2f}")
