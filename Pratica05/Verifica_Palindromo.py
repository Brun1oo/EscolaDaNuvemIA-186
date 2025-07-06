def verifica_palindromo(texto):
    #Remover espaços e coverter para minúsculo
    texto_limpo = "".join(char.lower() for char in texto if char.isalnum())
    #Compara o texto com a sua versão invertida
    return texto_limpo == texto_limpo[::-1]


frase = input("Digite uma palavra ou uma frase para verificar se é palindromo: ")
resultado = verifica_palindromo(frase)

if resultado == True:
    resposta = "Sim"
else:
    resposta = "Não"

print(f"O texto {frase} é um palindromo? {resposta}")