import unittest

class ut(unittest.TestCase):
    def test_eq(self):
        self.assertEqual({2: 1, 3: 2, 1: 3}.keys(), {3: 2, 2: 1, 1: 3}.keys())

    def __str__(self):
        return "testString"
