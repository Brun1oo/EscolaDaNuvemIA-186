#Pedimos que o usuário coloque a sua idade
idade_usuario = int(input("Digite a sua idade: "))

#Aqui classificamos o usuário apartir da idade que ele colocou
if idade_usuario < 0:
    print("Idade válida")
elif idade_usuario <= 12:
    print("Você é um criança")
elif idade_usuario <= 17: 
    print("Você é uma adolescente")
elif idade_usuario >= 59:
    print("Você é um adulto")
else:
    print("Você é um idoso")
