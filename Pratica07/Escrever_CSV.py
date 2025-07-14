import csv

with open("pessoas.csv", "w", newline="") as f:
    escritor = csv.writer(f)
    escritor.writerow(["Nome", "Idade", "Cidade"])
    escritor.writerow(["Ana", 22, "SP"])
    escritor.writerow(["João", 30, "RJ"])
