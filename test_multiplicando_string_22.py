import unittest

from multiplicando_string_22 import multiplicando_string


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.multiplica = multiplicando_string(6)
        print("setUp() sendo executado...")

    def test_multiplicando_string(self):
        self.assertEqual(self.multiplica, None)  # add assertion here

    def tearDown(self) -> None:
        print("tearDown sendo executado...")


if __name__ == '__main__':
    unittest.main()
