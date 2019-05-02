import unittest
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "fizz")
    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "buzz")



if __name__ == '__main__':
    unittest.main()
