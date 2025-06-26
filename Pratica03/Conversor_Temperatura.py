#Solicitar a temperatura ao usuário
temperatura_usuario = float(input("Informe a temperatura: "))

#fornecer as escalas
unidade_origem = input("Informe a unidade de origem (C, F, K): ").upper()
unidade_destino = (input("Informe a unidade de origem (C, F, K): ")).upper()

#Conversão da temperatura 
#Escala de origem é a mesma do destino
if unidade_origem == unidade_destino:
    resultado = temperatura_usuario

#Conversão quando a origem for Celsius (C)
elif unidade_origem == "C":
    if unidade_destino == "F":
        resultado = (temperatura_usuario * 1.8) + 32
    else: #De celsius para Kelvin
        resultado = temperatura_usuario + 273.15

#Conversão quando a origem for Fahrenheit (F)
elif unidade_origem == "F":
    if unidade_destino == "C":
        resultado = (temperatura_usuario - 32) / 1.8
    else: 
        resultado = ((temperatura_usuario - 32) * 1.8) + 273.15

#Conversão quando a origem for Kelvin (K)
else:
    if unidade_destino == "C":
        resultado = temperatura_usuario - 273,15
    else:
        resultado = ((temperatura_usuario - 273.15) * 1.8) + 32

print(f"{temperatura_usuario} {unidade_origem} é igual a {resultado: .2f}{unidade_destino}")