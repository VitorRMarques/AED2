import string

def contar_palavras(frase: str) -> dict:
    if not isinstance(frase, str):
        raise TypeError("A palavra deve ser uma string")

    frase = frase.lower()

    tradutor = str.maketrans("", "", string.punctuation)
    frase = frase.translate(tradutor)

    palavras = frase.split()

    contagem = {} 
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
    
    return contagem

if __name__ == "__main__":
    entrada = input("Digite uma frase:").strip()
    try:
        resultado = contar_palavras(entrada)
        print("\nContagem de palavras:")
        for palavra, qtd in resultado.items():
            print(f"{palavra}: {qtd}")

    except Exception as e:
        print("Erro: ", {e})

