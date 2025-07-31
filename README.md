# Cadastro de Usuários - Testes Funcionais com Pytest

Este projeto simula testes funcionais automatizados com `pytest` para um sistema simples de cadastro de usuários.

## Funcionalidades testadas:
- Cadastro com dados válidos
- Validação de e-mail inválido
- Validação de senha com menos de 6 caracteres
- Validação de nome obrigatório

## Como executar:
```bash
pip install -r requirements.txt
pytest --maxfail=1 --disable-warnings -v
```

## AUTOR:
César Henrique da Silva
Projeto criado para fins acadêmicos e como forma de praticar o que estou aprendendo.