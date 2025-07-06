import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + "!@#$%&*"
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho_senha))
    return senha

tamanho_senha = int(input("Digite o tamanho da senha que deseja: "))
nova_senha = gerar_senha(tamanho_senha)
print(f"Sua senha é: {nova_senha}")
