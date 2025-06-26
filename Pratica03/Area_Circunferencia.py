#Valor de pi
pi = 3.14159265

#Pedimos para que o usuário coloque o valor do raio
raio = float(input("Insira o valor do raio em cm: "))

#Cálculo da area
area = pi * (raio ** 2)

#Exibição para o usuário
print(f"A área da circungerência é: {area: .4f} cm²")