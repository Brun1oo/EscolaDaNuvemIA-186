import csv

with open("pessoas.csv") as f:
    leitor = csv.reader(f)
    for linha in leitor:
        print(linha)
