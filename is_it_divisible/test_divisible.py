import unittest
from divisible import divider_check

class TestMultiplier(unittest.TestCase):
    def test_divider(self):
        self.assertEqual(divider_check(3, 4), 12)

if __name__ == '__main__':
    unittest.main()
