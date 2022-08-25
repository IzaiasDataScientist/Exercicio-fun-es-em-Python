import unittest

from calculadora_simples_13 import calculadora_simples


class MyTestCase(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(calculadora_simples(2, 2, "+"), 4)  # add assertion here

    def test_subtracao(self):
        self.assertEqual(calculadora_simples(2, 2, "-"), 0)

    def test_multiplicação(self):
        self.assertEqual(calculadora_simples(2, 2, "*"), 4)

    def test_divisao(self):
        self.assertEqual(calculadora_simples(2, 2, "/"), 1)

if __name__ == '__main__':
    unittest.main()
