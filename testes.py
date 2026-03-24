import pytest
import json

# ============================================================
# Sistema simulado de cadastro
# Substitua pela importação real do seu módulo:
# from seu_modulo import verificar_acesso
# ============================================================

def carregar_dados():
   try:
      with open("dados.json", "r", encoding="utf-8") as arq:
         lista = json.load(arq)
         return lista if isinstance(lista, list) else []
   except (FileNotFoundError, json.JSONDecodeError):
      return []
   

def buscar_conta_id(id_buscado):
   lista = carregar_dados()
   for conta in lista:
      if str(conta["ID"]) == str(id_buscado):
         return conta
   return None

def verificar_acesso(conta_ativa, eh_premium, tem_credito, email_verificado):
    """
    Retorna o nível de acesso do usuário com base nas 4 condições booleanas.
    Valores possíveis: 'acesso_total', 'acesso_parcial', 'bloqueado'
    """

    id_input = input("Digite o ID da conta que deseja buscar: ")
    conta = buscar_conta_id(id_input)

    if conta is None:
        print(f"Nenhuma conta encontrada com ID {id_input}")
    
    conta_ativa = conta["Status de conta"]

    
    if not conta_ativa:
        return "bloqueado"

    if not tem_credito and not email_verificado:
        return "bloqueado"

    if tem_credito and email_verificado and eh_premium:
        return "acesso_total"

    return "acesso_parcial"


# ============================================================
# Fixtures reutilizáveis
# ============================================================

@pytest.fixture
def usuario_completo():
    """Usuário com todas as condições satisfeitas."""
    return dict(conta_ativa=True, eh_premium=True, tem_credito=True, email_verificado=True)

@pytest.fixture
def usuario_inativo():
    """Usuário com conta desativada."""
    return dict(conta_ativa=False, eh_premium=True, tem_credito=True, email_verificado=True)


# ============================================================
# BLOCO 1 — Conta ativa = True (8 casos)
# ============================================================

class TestContaAtiva:

    # Caso 1 — Caminho feliz: tudo True
    def test_caso_01_acesso_total(self):
        resultado = verificar_acesso(
            conta_ativa=True,
            eh_premium=True,
            tem_credito=True,
            email_verificado=True
        )
        assert resultado == "acesso_total", (
            "Caso 1: todas as condições True deve retornar acesso_total"
        )

    # Caso 2 — Premium com crédito, sem email verificado
    def test_caso_02_premium_sem_email(self):
        resultado = verificar_acesso(
            conta_ativa=True,
            eh_premium=True,
            tem_credito=True,
            email_verificado=False
        )
        assert resultado == "acesso_parcial", (
            "Caso 2: email não verificado deve reduzir para acesso_parcial"
        )

    # Caso 3 — Premium com email, sem crédito
    def test_caso_03_premium_sem_credito(self):
        resultado = verificar_acesso(
            conta_ativa=True,
            eh_premium=True,
            tem_credito=False,
            email_verificado=True
        )
        assert resultado == "acesso_parcial", (
            "Caso 3: sem crédito deve retornar acesso_parcial mesmo sendo premium"
        )

    # Caso 4 — Premium sem crédito e sem email (bloqueio total)
    def test_caso_04_premium_sem_credito_sem_email(self):
        resultado = verificar_acesso(
            conta_ativa=True,
            eh_premium=True,
            tem_credito=False,
            email_verificado=False
        )
        assert resultado == "bloqueado", (
            "Caso 4: sem crédito e sem email deve bloquear mesmo sendo premium"
        )

    # Caso 5 — Standard com tudo válido
    def test_caso_05_standard_completo(self):
        resultado = verificar_acesso(
            conta_ativa=True,
            eh_premium=False,
            tem_credito=True,
            email_verificado=True
        )
        assert resultado == "acesso_parcial", (
            "Caso 5: conta standard com tudo OK deve retornar acesso_parcial"
        )

    # Caso 6 — Standard com crédito, sem email
    def test_caso_06_standard_sem_email(self):
        resultado = verificar_acesso(
            conta_ativa=True,
            eh_premium=False,
            tem_credito=True,
            email_verificado=False
        )
        assert resultado == "acesso_parcial", (
            "Caso 6: standard sem email verificado deve retornar acesso_parcial"
        )

    # Caso 7 — Standard com email, sem crédito
    def test_caso_07_standard_sem_credito(self):
        resultado = verificar_acesso(
            conta_ativa=True,
            eh_premium=False,
            tem_credito=False,
            email_verificado=True
        )
        assert resultado == "acesso_parcial", (
            "Caso 7: standard sem crédito deve retornar acesso_parcial"
        )

    # Caso 8 — Standard sem crédito e sem email
    def test_caso_08_standard_sem_credito_sem_email(self):
        resultado = verificar_acesso(
            conta_ativa=True,
            eh_premium=False,
            tem_credito=False,
            email_verificado=False
        )
        assert resultado == "bloqueado", (
            "Caso 8: standard sem crédito e sem email deve bloquear"
        )


# ============================================================
# BLOCO 2 — Conta ativa = False (8 casos)
# conta_ativa=False é condição dominante: sempre bloqueado
# ============================================================

class TestContaInativa:

    @pytest.mark.parametrize("eh_premium,tem_credito,email_verificado,caso", [
        (True,  True,  True,  9),
        (True,  True,  False, 10),
        (True,  False, True,  11),
        (True,  False, False, 12),
        (False, True,  True,  13),
        (False, True,  False, 14),
        (False, False, True,  15),
        (False, False, False, 16),
    ])
    def test_conta_inativa_sempre_bloqueada(
        self, eh_premium, tem_credito, email_verificado, caso
    ):
        resultado = verificar_acesso(
            conta_ativa=False,
            eh_premium=eh_premium,
            tem_credito=tem_credito,
            email_verificado=email_verificado
        )
        assert resultado == "bloqueado", (
            f"Caso {caso}: conta inativa deve sempre retornar bloqueado "
            f"(premium={eh_premium}, credito={tem_credito}, email={email_verificado})"
        )


# ============================================================
# BLOCO 3 — Testes com fixture
# ============================================================

class TestComFixtures:

    def test_usuario_completo_tem_acesso_total(self, usuario_completo):
        resultado = verificar_acesso(**usuario_completo)
        assert resultado == "acesso_total"

    def test_usuario_inativo_bloqueado(self, usuario_inativo):
        resultado = verificar_acesso(**usuario_inativo)
        assert resultado == "bloqueado"


# ============================================================
# BLOCO 4 — Testes de fronteira críticos
# ============================================================

class TestFronteira:

    def test_unica_condicao_faltando_email(self):
        """Só o email faltando não deve bloquear completamente."""
        resultado = verificar_acesso(
            conta_ativa=True,
            eh_premium=True,
            tem_credito=True,
            email_verificado=False
        )
        assert resultado != "bloqueado"

    def test_unica_condicao_faltando_credito(self):
        """Só o crédito faltando não deve bloquear completamente."""
        resultado = verificar_acesso(
            conta_ativa=True,
            eh_premium=True,
            tem_credito=False,
            email_verificado=True
        )
        assert resultado != "bloqueado"

    def test_premium_nao_garante_acesso_sem_conta_ativa(self):
        """Ser premium não deve sobrescrever conta inativa."""
        resultado = verificar_acesso(
            conta_ativa=False,
            eh_premium=True,
            tem_credito=True,
            email_verificado=True
        )
        assert resultado == "bloqueado"

    def test_retorno_invalido_nao_aceito(self):
        """O sistema não deve retornar valores fora do conjunto esperado."""
        resultado = verificar_acesso(True, True, True, True)
        assert resultado in {"acesso_total", "acesso_parcial", "bloqueado"}