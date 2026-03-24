def inverter_palavra(palavra):
    palavra_invertida = ''
    for letra in range(len(palavra)-1, -1, -1):
        palavra_invertida += palavra[letra]
    return palavra_invertida

palavra = input("Digite uma palavra: ")
resultado = inverter_palavra(palavra)

for letra in resultado:
    print(letra)