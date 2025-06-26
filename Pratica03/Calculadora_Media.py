N1 = float(input("Digite a primeira nota (peso 2): "))
N2 = float(input("Digite a segunda nota (peso 3): "))
N3 = float(input("Digite a terceira nota (peso 4): "))
N4 = float(input("Digite a quarta nota (peso 1): "))

media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10

if media > 7.0:
    print("Aluno aprovado")
elif media < 5.0:
    print("Aluno reprovado")
else: 
    print("Aluno em exame")
    nota_exame = float(input("Digite a nota do exame: "))
    print(f"Nota do exame: {nota_exame: .1f}")

    segunda_media = (nota_exame + media) / 2

    if segunda_media > 5.0:
        print("Aluno aprovado")
    else:
        print("Aluno reprovado")

    print(f"Media final: {segunda_media}")

