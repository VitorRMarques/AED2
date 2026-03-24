vetor = []
while True:
    listadenumeros = input("Digite um numero para adicionar no vetor ou 'sair': ")
    if listadenumeros.lower() == 'sair':
        break
    try:
        vetor.append(int(listadenumeros))
    except ValueError:
        print("Por favor, digite um número válido")
        continue
    print(vetor)

def remover_negativos():
    global vetor
    vetor = [i for i in vetor if i >= 0]

print("vetor antes de remover os negativos:", vetor)
remover_negativos()
print("vetor depois de remover os negativos:", vetor)


