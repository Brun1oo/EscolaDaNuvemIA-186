while True:
    #A entrada da senha
    senha = input("Digite uma senha (ou digite 'sair' para encerrar): ")
    
    #Vereficação do camando "sair"
    if senha == "sair":
        print("O programa foi encerrado.")
        break

    #Verificação do comprimento da senha
    if senha < 8:
        print("Senha fraca. A senha precisa ter pelo menos 9 caracteres.")
        continue

    #Verificação se possuí um número
    if not any(caractere.isdigit() for caractere in senha):
        print("Senha fraca. A senha precisa ter pelo menos um número.")
        continue

    #Verificação se possuí pelo uma letra
    if not any(caractere.isalpha() for caractere in senha):
        print("Senha fraca. A senha precisa ter pelo menos uma letra.")
        continue

    #Verificação se possuí pelo menos uma letra maiúscula
    if not any(caractere.isupper() for caractere in senha):
        print("Senha fraca. A senha precisa ter pelo menos uma letra.")
        continue

    #Se chegar até aqui deu tudo certo
    print("A senha é forte.")
    break