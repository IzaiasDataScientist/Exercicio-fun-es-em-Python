import unittest

from distancia_por_litro_14 import distancia_por_litro


class MyTestCase(unittest.TestCase):
    def test_venda_o_carro(self):
        self.assertEqual(distancia_por_litro(350, 50), 'Venda o carro!')  # add assertion here

    def test_economico(self):
        self.assertEqual(distancia_por_litro(500, 50), 'Economico!')

    def test_super_economico(self):
        self.assertEqual(distancia_por_litro(700, 50), 'Super economico!')


if __name__ == '__main__':
    unittest.main()
