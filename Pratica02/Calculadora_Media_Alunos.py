nota1 = float(input("Insira a primeira nota:"))
nota2 = float(input("Insira a segunda nota:"))
nota3 = float(input("Insira a terceira nota:"))

nota_total = nota1 + nota2 + nota3 
nota_media = nota_total / 3

print(f"Notas do aluno, primeira nota {nota1}, segunda nota {nota2} e terceira nota {nota3}")
print(f"O seu aluno ficou com media de: {nota_media: .2f}")