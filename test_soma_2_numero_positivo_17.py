import unittest

from soma_2_numero_positivo_17 import soma


class MyTestCase(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)  # add assertion here

    def test_numeros_negativos(self):
        self.assertEqual(soma(-2, -4), -1)

    def test_numero_nao_string(self):
        self.assertEqual(soma("w", "e"), -1)


if __name__ == '__main__':
    unittest.main()
