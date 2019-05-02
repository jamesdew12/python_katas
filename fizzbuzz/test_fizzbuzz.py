import unittest
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "fizz")
    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "buzz")
    def test_fizbuzz(self):
        self.assertEqual(fizzbuzz(15), "fizzbuzz")
    def test_number(self):
        self.assertEqual(fizzbuzz(4), '4')



if __name__ == '__main__':
    unittest.main()
