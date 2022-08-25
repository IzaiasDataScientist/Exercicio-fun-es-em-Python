import unittest
import math

from volume_esfera_5 import volume


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(volume(5), (4/3)*math.pi*(5**3))  # add assertion here


if __name__ == '__main__':
    unittest.main()
