import json

def carregar_dados():
    with open("dados.json", mode="r", encoding="utf-8") as arq:
        return json.load(arq)

def salvar_dados(lista):
    with open("dados.json", "w", encoding="utf-8") as arq:
        json.dump(lista, arq, ensure_ascii=False, indent=4)

def desativar_id(lista, id_buscado):
    for conta in lista:
        if conta["ID"] == id_buscado:
            conta["status"] = "d"
            return True
    return False

lista_dados = carregar_dados()

try:
    id_buscado = int(input("Digite o ID que deseja desativar a conta: "))
except ValueError:
    print("ID invalido, digite apenas numeros")
    exit()
encontrado = desativar_id(lista_dados, id_buscado)

if encontrado:
    salvar_dados(lista_dados)
    print(f"Conta com {id_buscado} desativada.")
else:
    print(f"ID {id_buscado} nao encontrado.")
