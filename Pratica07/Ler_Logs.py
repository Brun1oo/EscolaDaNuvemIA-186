with open("C:\\Users\\Bruno\\EscolaDaNuvemIA\\Pratica07\\log.txt") as f:
    tempos = []
    for linha in f:
        if "Execution Time:" in linha:
            tempo = float(linha.split("Execution Time:")[1].strip().replace("s", ""))
            tempos.append(tempo)

media = sum(tempos) / len(tempos)
desvio = (sum((x - media) ** 2 for x in tempos) / len(tempos)) ** 0.5

print("Média:", round(media, 2))
print("Desvio Padrão:", round(desvio, 2))
