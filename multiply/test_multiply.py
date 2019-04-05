import unittest
from multiply import multiplier

class TestMultiplier(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiplier(3, 4), 12)

if __name__ == '__main__':
    unittest.main()
