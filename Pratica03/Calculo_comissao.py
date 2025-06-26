#Inserir o nome do vendedor
nome = input("Favor inserir o nome do vendedor: ")

#Informações sobre vendas e salario
salario_fixo = float(input("Insira o salário fixo: R$ "))
total_vendas = float(input("Insira o total de vendas: R$ "))

#Calculo da comissão
comissao_percentual = 0.15
comissao = total_vendas * comissao_percentual

#Calculo do total a receber
total_receber = salario_fixo + comissao

#Exibição para o usuário
print(f"O vendedor {nome} irá receber R$ {total_receber: .2f}")
