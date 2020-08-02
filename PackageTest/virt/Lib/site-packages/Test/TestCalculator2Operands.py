import unittest

from PackageTest.Calculator2Operands import *

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.a=2
        self.b=3

    def test_sum(self):
        self.assertEqual(sum(self.a,self.b), 5)

    def test_sub(self):
        self.assertEqual(sub(self.a,self.b), -1)

    def test_mult(self):
        self.assertEqual(multiply(self.a,self.b), 6)

    def test_div(self):
        self.assertEqual(round(division(self.a,self.b),2), 0.67)

    def test_wrapper(self):
        f = logger(sum)
        print(f.__name__)
        self.assertEqual(f(2,3), 5)

if __name__ == "__main__":
    unittest.main()