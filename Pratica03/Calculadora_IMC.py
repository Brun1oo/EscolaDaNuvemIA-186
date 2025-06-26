peso_usuario = float(input("Digite o seu peso em quilogramas (KG): "))
altura_usuario = float(input("Digite sua altura em metros (m): "))

altura_imc = altura_usuario * altura_usuario
imc_usuario = peso_usuario / altura_imc

if imc_usuario <= 18.5:
    classificação = "Abaixo do peso"
elif imc_usuario < 25:
    classificação = "Peso normal"
elif imc_usuario < 30:
    classificação ="Sobrepeso"
else: 
    classificação = "Obeso"

print(f"""
Seu IMC é: {imc_usuario}
Classificação: {classificação}
""")

