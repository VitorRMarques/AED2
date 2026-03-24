import random
import json
import pytest


# CONSTANTES
NIVEL_CONTA = "Nivel de conta"
CONTA_PREMIUM = "* Conta Premium *"
CONTA_STANDARD = "Conta Standard"
STATUS_ATIVO = "a"
STATUS_DESATIVO = "d"
ARQUIVO_DADOS = "dados.json"

# FUNCOES AUXILIARES

def carregar_dados():
   try:
      with open("dados.json", "r", encoding="utf-8") as arq:
         lista = json.load(arq)
         return lista if isinstance(lista, list) else []
   except (FileNotFoundError, json.JSONDecodeError):
      return [] 
   
def salvar_dados(lista):
   with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arq:
      json.dump(lista, arq, ensure_ascii=False, indent=4)

def buscar_conta_id(id_buscado):
   lista = carregar_dados()
   for conta in lista:
      if str(conta["ID"]) == str(id_buscado):
         return conta
   return None

# VERIFICACAO DE ACESSO

def verificar_conta(conta):
   nivel = conta[NIVEL_CONTA]
   status = conta["status"]
   if nivel == CONTA_PREMIUM and status == STATUS_ATIVO :
      print("Conta com acesso ilimitado")
      print("--------------------------")
      return True
   elif nivel == CONTA_STANDARD and status == STATUS_ATIVO:
      print("Conta com acesso limitado")
      print("--------------------------")
      return True
   elif nivel == CONTA_STANDARD and status == STATUS_DESATIVO:
      print("conta com acesso nao autorizado ou desativada")
      print("---------------------------")
      return False
   else:
      print("Conta com nivel premium, porem desativada, entre em contato com algum agente disponivel") 
      print("----------------------------")
      return False
   
def verificar_idade(conta_idade):
   idade = conta_idade["idade"]
   if idade < "18":
      return "Usuario menor de idade, conta deve ter supervisao."
   elif idade >= "18":
      return "Usuario maior de idade, acesso total."
def add(key, value):
    dados[key] = value


inicio = input("Voce quer adicionar alguma conta (1), verificar ela? (2) ou testar a validade de dados (3): ")

if inicio == "1":
   try: 
      dados = {}

      id = random.randrange(0, 100)
      add("ID", id)
      print("-----------------------")

      nome = input("Digite o nome: ")
      add("nome", nome)

      print("-----------------------")

      idade = input("Digite sua idade: ")
      add("idade", idade)

      print("-----------------------")

      email = input("Digite o Email: ")
      add("email", email)

      print("-----------------------")
      senha = input("Digite a senha: ")
      add("senha", senha)


      print("-----------------------")

      premium = input("Deseja ativar o modo premium a essa conta?")
      if premium == "sim".lower():
         p = CONTA_PREMIUM
      else:
         p = CONTA_STANDARD
      add(NIVEL_CONTA, p)

      print("-----------------------")

      resp = input("Adicionar Creditos?")
      if resp == "sim":
         quant = input("Digite a quantidade:")
         add("creditos", quant)
      else:
         quant = "0"
         add("creditos", quant)

      print("-----------------------")
         
      print("...")
      ativada = STATUS_ATIVO
      print("Conta cadastrada!")
      add("status", ativada)
      print(dados)

      try:
         with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            lista_dados = json.load(arquivo)
            if not isinstance(lista_dados, list):
               lista_dados = []
      except (FileNotFoundError, json.JSONDecodeError):
         
         lista_dados = []

      lista_dados.append(dados.copy())

      try:
         with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
          json.dump(lista_dados, arquivo, ensure_ascii=False, indent=4)
         print(f"Dicionario salvo em {ARQUIVO_DADOS}")

      except IOError as e:
         print(f"erro ao salvar o dicionario: {e}")

   except ValueError as e:
    print(e)

   print("\nLista final de dicionarios:")
   for item in lista_dados:
      print(item)


if inicio == "2":
   
      id_input = input("Digite o 'ID' que voce quer verificar: ").strip()
      conta = buscar_conta_id(id_input)
      
      if conta is None:
         print(f"Nenhuma conta encontrada com ID {id_input}")
      else:
         print("-------Informacoes de conta---------")
         print(f"ID: {conta['ID']}")
         print(f"Nome: {conta['nome']}")
         print(f"Idade do usuario: {conta['idade']}")
         print(f"Nivel de conta: {conta[NIVEL_CONTA]}")
         print(f"Status de conta: {"ativada" if conta['status'] == STATUS_ATIVO else 'DESATIVADA'}")
         print(f"Credito: {conta.get('creditos', 0)}")
         print("--Resultado da verificacao--")
         print(verificar_conta(conta))
         print(verificar_idade(conta))
if inicio == "3":

    contas = carregar_dados()

    if not contas:
        print("Nenhuma conta encontrada em dados.json")
    else:
        aprovados = 0
        reprovados = 0

        print("\n========= TESTANDO TODAS AS CONTAS =========")

        for conta in contas:
            nome = conta.get("nome", "?")
            id_conta = conta.get("ID", "?")
            nivel = conta.get("Nivel de conta", "?")
            status = conta.get("status", "?")
            idade = conta.get("idade", "?")

            print(f"\n--- Conta: {nome} (ID: {id_conta}) ---")

            # Tuplas de dominio valido
            niveis_validos   = ("* Conta Premium *", "Conta Standard")
            status_validos   = ("a", "d")

            # TESTE 1 - Nivel de conta valido
            try:
                assert nivel in niveis_validos, f"Nivel invalido: '{nivel}'"
                print(f"  [PASSOU] Nivel de conta valido: '{nivel}'")
                aprovados += 1
            except AssertionError as e:
                print(f"  [FALHOU] {e}")
                reprovados += 1

            # TESTE 2 - Status valido (a = ativo, d = desativado)
            try:
                assert status in status_validos, f"Status inesperado: '{status}' (esperado 'a' ou 'd')"
                print(f"  [PASSOU] Status valido: '{status}'")
                aprovados += 1
            except AssertionError as e:
                print(f"  [FALHOU] {e}")
                reprovados += 1

            # TESTE 3 - Idade numerica e positiva
            try:
                assert int(idade) > 0, f"Idade invalida: {idade}"
                print(f"  [PASSOU] Idade valida: {idade}")
                aprovados += 1
            except (AssertionError, ValueError) as e:
                print(f"  [FALHOU] Idade com problema: {e}")
                reprovados += 1

            # TESTE 4 - verificar_conta() retorna bool esperado
            try:
                combinacoes_esperadas = (
                    ("* Conta Premium *", "a", True),
                    ("Conta Standard",    "a", True),
                    ("Conta Standard",    "d", False),
                    ("* Conta Premium *", "d", False),
                )
                esperado = None
                for n, s, resultado in combinacoes_esperadas:
                    if nivel == n and status == s:
                        esperado = resultado
                        break

                if esperado is not None:
                    obtido = verificar_conta(conta)
                    assert obtido == esperado, f"Esperado {esperado}, obtido {obtido}"
                    print(f"  [PASSOU] verificar_conta() => {obtido}")
                    aprovados += 1
                else:
                    print(f"  [AVISO]  Combinacao nivel+status fora do padrao: ('{nivel}', '{status}')")
                    reprovados += 1

            except AssertionError as e:
                print(f"  [FALHOU] verificar_conta(): {e}")
                reprovados += 1

            # TESTE 5 - verificar_idade() retorna string correta
            try:
                faixas_validas = (
                    "Usuario maior de idade, acesso total.",
                    "Usuario menor de idade, conta deve ter supervisao.",
                )
                msg = verificar_idade(conta)
                assert msg in faixas_validas, f"Retorno inesperado: '{msg}'"
                print(f"  [PASSOU] verificar_idade() => '{msg}'")
                aprovados += 1
            except AssertionError as e:
                print(f"  [FALHOU] verificar_idade(): {e}")
                reprovados += 1

        print("\n=========================================")
        print(f"  Total de testes : {aprovados + reprovados}")
        print(f"  Aprovados        : {aprovados}")
        print(f"  Reprovados       : {reprovados}")
        print("=========================================\n")




















    