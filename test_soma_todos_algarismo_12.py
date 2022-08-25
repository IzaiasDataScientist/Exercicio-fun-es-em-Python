import unittest

from soma_todos_algarismo_12 import soma_todos_algarismo


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(soma_todos_algarismo(251), 8)  # add assertion here


if __name__ == '__main__':
    unittest.main()
