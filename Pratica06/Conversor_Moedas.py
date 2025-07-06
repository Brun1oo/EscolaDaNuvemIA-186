import requests
from datetime import datetime

def obter_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        cotacao = dados[f"{moeda}BRL"]
        return f"""
    Moeda: {moeda} para BRL
    Valor: R$ {float(cotacao['bid']): .2f}
    Máximo: R$ {float(cotacao['high']): .2f}
    Mínimo: R$ {float(cotacao['low']): .2f}
    Data/Hora: {datetime.fromtimestamp(int(cotacao['timestamp']))}
    """

    except requests.RequestException as e:
        return f"Erro ao obter cotação: {e}"
    except KeyError:
        return f"Moeda não encontrada ou não suportada"

moeda = input("Digite o código da moeda desejada (USD, EUR, GBP): ")
print("\mObtendo cotação...")
resultado = obter_cotacao(moeda)
print(resultado)