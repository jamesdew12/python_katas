import unittest
from string_end import end_matcher

class TestMultiplier(unittest.TestCase):
    def test_end_matcher(self):
        self.assertEqual(end_matcher('abcd', 'cd'), True)
        self.assertEqual(end_matcher('abcd', 'cde'), False)


if __name__ == '__main__':
    unittest.main()
