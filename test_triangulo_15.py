import unittest

from triangulo_15 import formam_um_triangulo, tipos_triangulo


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.triangulo = tipos_triangulo(23, 23, 23)
        self.forma_triangulo = formam_um_triangulo(3, 23, 5)
        print('setUp() sendo executado...')

    def test_forma_triangulo(self):
        #self.forma_triangulo = formam_um_triangulo(3, 23, 5)
        self.assertEqual(self.forma_triangulo, True)

    def test_triangulo_equilatero(self):
        self.assertEqual(self.triangulo, 'Triangulo equilatero')

    def test_triangulo_isosceles1(self):
        self.triangulo = tipos_triangulo(23, 23, 3)
        self.assertEqual(self.triangulo, 'Triangulo isosceles')

    def test_triangulo_isosceles2(self):
        self.triangulo = tipos_triangulo(3, 23, 23)
        self.assertEqual(self.triangulo, 'Triangulo isosceles')

    def test_triangulo_isosceles3(self):
        self.triangulo = tipos_triangulo(23, 3, 23)
        self.assertEqual(self.triangulo, 'Triangulo isosceles')

    def test_triangulo_escaleno(self):
        self.triangulo = tipos_triangulo(3, 23, 22)
        self.assertEqual(self.triangulo, 'Triangulo escaleno')

    def tearDown(self) -> None:
        print('tearDown() sendo executado')


if __name__ == '__main__':
    unittest.main()
