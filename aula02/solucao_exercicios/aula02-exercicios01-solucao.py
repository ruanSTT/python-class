# Exercício 1 - Solução

# test_descontos.py
import unittest
from descontos import calcular_desconto
from unittest.mock import patch

class TestDescontos(unittest.TestCase):

    def test_sem_desconto(self):
        self.assertEqual(calcular_desconto(100), 0)

    def test_desconto_5_porcento(self):
        self.assertEqual(calcular_desconto(200), 10)

    def test_desconto_10_porcento(self):
        self.assertEqual(calcular_desconto(1000), 100)

    @patch('descontos.calcular_desconto')
    def test_mock_desconto(self, mock_calc):
        mock_calc.return_value = 50
        resultado = mock_calc(500)
        self.assertEqual(resultado, 50)
        mock_calc.assert_called_once_with(500)

if __name__ == '__main__':
    unittest.main()

# descontos.py
def calcular_desconto(valor):
    if valor <= 100:
        return 0
    elif valor <= 500:
        return valor * 0.05
    else:
        return valor * 0.10
