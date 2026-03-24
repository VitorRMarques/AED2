fila = []
while True:
    nome = input("Digite um nome (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        print("fila final:", fila)
        break
    fila.append(nome)
    print("Fila atual: ", fila)

