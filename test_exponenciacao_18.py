import unittest

from exponenciacao_18 import exponenciacao


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.potencia = exponenciacao(2, 4)
        print("setUp sendo executado...")

    def test_potencia(self):
        self.assertEqual(self.potencia, 16)  # add assertion here

    def test_numero_como_string(self):
        self.potencia = exponenciacao("string", 4)
        self.assertFalse(self.potencia, False)

    def test_potencia_de_expoente_como_string(self):
        self.potencia = exponenciacao(4, "string")
        self.assertFalse(self.potencia, False)

    def tearDown(self) -> None:
        print("tearDown() sendo executado...")


if __name__ == '__main__':
    unittest.main()
