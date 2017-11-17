import unittest
import foo


class SimpleTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(foo.divide(2, 2), 1, "2 / 2 = 1 failed")

    def test2(self):
        self.assertEqual(foo.divide(0, 1), 0, "0 / 1 = 0 failed")

    def test3(self):
        self.assertEqual(foo.divide(3, 3), 1, "3 / 3 = 1 failed")


if __name__ == '__main__':
    unittest.main()
