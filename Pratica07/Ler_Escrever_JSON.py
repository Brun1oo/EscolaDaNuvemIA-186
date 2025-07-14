import json

# Escrever
dados = {"nome": "Maria", "idade": 25, "cidade": "BH"}
with open("pessoa.json", "w") as f:
    json.dump(dados, f)

# Ler
with open("pessoa.json") as f:
    pessoa = json.load(f)
    print(pessoa)
