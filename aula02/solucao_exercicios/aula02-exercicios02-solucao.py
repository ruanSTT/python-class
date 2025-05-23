# test_validacao.py
import unittest
from validacao import validar_nome_variavel
from unittest.mock import patch

class TestValidacaoNomes(unittest.TestCase):

    def test_valido(self):
        self.assertTrue(validar_nome_variavel("nome_valido"))

    def test_invalido_inicia_com_numero(self):
        self.assertFalse(validar_nome_variavel("1nome"))

    def test_invalido_camel_case(self):
        self.assertFalse(validar_nome_variavel("nomeCompleto"))

    def test_invalido_caracter_especial(self):
        self.assertFalse(validar_nome_variavel("valor-total"))

    @patch('validacao.validar_nome_variavel')
    def test_mock_validacao(self, mock_validador):
        mock_validador.return_value = True
        self.assertTrue(mock_validador("qualquer_nome"))
        mock_validador.assert_called_once_with("qualquer_nome")

if __name__ == '__main__':
    unittest.main()


# validacao.py
import re

def validar_nome_variavel(nome):
    pattern = r'^[a-z_][a-z0-9_]*$'
    return bool(re.match(pattern, nome))