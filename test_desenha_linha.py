import unittest

from desenha_linha import desenha_linha


class MyTestCase(unittest.TestCase):
    def test_desenha_linha(self):
        self.assertEqual(desenha_linha(7), "=======")  # add assertion here


if __name__ == '__main__':
    unittest.main()
