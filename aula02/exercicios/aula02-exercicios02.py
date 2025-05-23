"""
Exercício 2: Validação de Nomes de Variáveis usando PEP8 + Testes
🎯 Objetivo:
Entender a importância de padronização com PEP8.

Criar uma função que valida nomes de variáveis usando regras da PEP8.

Testar com unittest e mock.
"""

"""
📝 Contexto:
Você está criando um linter simplificado: uma função que verifica se um nome de variável respeita o padrão snake_case, e não pode conter números no início, nem caracteres especiais.

Exemplos de nomes válidos:

nome_completo

contador_1

Exemplos inválidos:

1variavel

nomeCompleto

valor-total

✅ Requisitos:
Criar a função validar_nome_variavel(nome: str) -> bool

Escreva os testes com unittest.

Crie um mock dessa função para simular comportamentos válidos/invalidos.

Adicione testes que verificam a chamada da função.

Aplique PEP8.
"""