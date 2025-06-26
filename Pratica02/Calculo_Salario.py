numero_funcionario = int(input("Insira o numero do funcionario: "))
horas_trabalhadas = int(input("Insira a quantidade de horas trabalhadas: "))
valor_por_hora = float(input("Insira o valor das horas trabalhadas: "))

salario = horas_trabalhadas * valor_por_hora

print(
f"""Número do funcionário: {numero_funcionario}
Salário = R$ {salario: .2f}
"""
)