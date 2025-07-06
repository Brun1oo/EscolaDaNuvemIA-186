#Definiu a função calcular gorjeta
def calcular_gorjeta(valor_conta, porcentagem_gorjata):
    #A conversão da porcentagem para decimal e multipilicação pelo valor da conta
    gorjeta = valor_conta * (porcentagem_gorjata / 100)
    #Arredonda a variável gorjeta e retorna para o programa 
    return round(gorjeta, 2)

#Captura dos dados através da interação com o usuário 
total_conta = float(input("Insira o valor total da conta: "))
porcentagem = float(input("Insira o valor percentual da gorjeta: "))

#Chama a função calcular_gorjeta
gorjeta = calcular_gorjeta(total_conta, porcentagem)

#Exibe esse conteúdo para o usuário
print(f"Para uma conta de R${total_conta: .2f}, a gorjeta de {porcentagem}% é de R${gorjeta}")