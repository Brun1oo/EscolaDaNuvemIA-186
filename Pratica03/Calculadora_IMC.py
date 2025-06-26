#Pedimos que o usuário coloque algumas informações
peso_usuario = float(input("Digite o seu peso em quilogramas (KG): "))
altura_usuario = float(input("Digite sua altura em metros (m): "))

#Cálculo do IMC
altura_imc = altura_usuario * altura_usuario
imc_usuario = peso_usuario / altura_imc

#Condições do IMC
if imc_usuario <= 18.5:
    classificação = "Abaixo do peso"
elif imc_usuario < 25:
    classificação = "Peso normal"
elif imc_usuario < 30:
    classificação ="Sobrepeso"
else: 
    classificação = "Obeso"

#Exibição para o usuário
print(f"""
Seu IMC é: {imc_usuario}
Classificação: {classificação}
""")

