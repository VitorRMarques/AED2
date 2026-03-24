# Elementos de uma lista: 
# Sempre leva o mesmo tempo

valores = [1, 10, 21, 30, 32, 40, 44, 50]

elementos = valores[2]

#print(elementos)

# Verificar se um numero eh par:

def eh_par(n):
    if n % 2 == 0:
        return True
    else: 
        return False
    
#print(eh_par(10))
#print(eh_par(11))

# Atribuicoes simples de valor:

x = 10

y = 10 + x

#print(y)

# Retornar elementos de uma tupla:

dados = ("nome", "sobrenome", "idade")

primeiro = dados[0]

#print(primeiro)

# Busca em Hash table:

dicionario = {"nome": "Ana", "idade": 22}

print("nome" in dicionario)
print("sexo" in dicionario)