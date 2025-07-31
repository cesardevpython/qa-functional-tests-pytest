import re

class Usuario:
    def __init__(self, nome, email, senha):
        if not nome:
            raise ValueError("Nome é obrigatório")
        if not self._validar_email(email):
            raise ValueError("E-mail inválido")
        if len(senha) < 6:
            raise ValueError("Senha deve ter pelo menos 6 caracteres")

        self.nome = nome
        self.email = email
        self.senha = senha

    def _validar_email(self, email):
        padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(padrao, email) is not None