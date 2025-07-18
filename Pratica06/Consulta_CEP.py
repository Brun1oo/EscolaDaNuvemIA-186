import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()

        if "erro" in dados:
            return "CEP não encontrado"
        
        return f""""
        Logradouro: {dados['logradouro']}
        Bairro: {dados['bairro']}
        Cidade: {dados['localidade']}
        Estado: {dados['uf']}
        """
    except requests.RequestException as e:
        return f"Erro de consulta {e}"

cep = input("Digite o CEP para consulta (apenas números): ")
print("Consultando CEP...")
resultado = consultar_cep(cep)
print(resultado)
