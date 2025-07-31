import pytest
from core.usuarios import Usuario

def test_cadastro_usuario_valido():
    usuario = Usuario("Joao Silva", "joao@gmail.com", "senha123")
    assert usuario.nome == "Joao Silva"
    assert usuario.email == "joao@gmail.com"
    assert usuario.senha == "senha123"

def test_usuario_cadastro_email_invalido():
    with pytest.raises(ValueError, match="E-mail inválido"):
        Usuario("Ana", "anagmail.com", "senha123")

def test_usuario_cadastro_senha_curta():
    with pytest.raises(ValueError, match="Senha deve ter pelo menos 6 caracteres"):
        Usuario("Ana", "ana@gmail.com", "123")

def test_usuario_cadastro_nome_vazio():
    with pytest.raises(ValueError, match="Nome é obrigatório"):
        Usuario("", "ana@gmail.com", "senha123")