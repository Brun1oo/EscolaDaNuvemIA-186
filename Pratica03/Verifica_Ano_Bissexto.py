ano = int(input("Digite um ano: "))

if ano % 4 == 0: #Se for divisivel por 4, pose ser que seja bissexto.
    if ano % 100 == 0: #Se for divisivel por 100, precisa ser analisado mais uma vez.
        if ano % 400 == 0: #Se for divisivel por 400 também, ele é um ano bissexto.
            print(f"{ano} é bissexto")
        else: #É divisivel por 4, por 100, mas não é divisivel por 400, portanto não é bissexto.
            print(f"{ano} não é bissexto")
    else: #É divisível por 4 e não é por 100, portanto é bissexto.
        print(f"{ano} não é bissexto")
else: #Se não for divisivel por 4, então não é bissexto.
    print(f"{ano} não é bissexto.")

