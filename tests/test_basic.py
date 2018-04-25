import unittest


def test():
    return 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test(), 1)