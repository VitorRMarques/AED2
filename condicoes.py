import json

dados = []

def carregar_dados():
    with open("dados.json", "r", "utf-8") as arq:
        return json.load(arq)
    

def verificar_conta(id):
   dados[id] = "ID"
   if dados["Nivel de conta"] == "Premium" and dados["status"] == "a" :
      return "Conta com acesso ilimitado"
   if dados["Nivel de conta"] == "Standard" and dados["status"] == "a":
      return "Conta com acesso limitado"
   if dados["Nivel de conta"] == "Standard" and dados["status"] == "d":
      return "conta com acesso nao autorizado ou desativada"
   if dados["Nivel de conta"] == "Premium" and dados["status"] == "d":
      return "Conta com nivel premium, porem desativada, entre em contato com algum agente disponivel" 

try:
   id_input = input("Digite o 'ID' que voce quer verificar: ")
   verificar_conta(id_input)
except KeyError as e:
   print("erro desconhecido")
