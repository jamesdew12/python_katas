import unittest
from src.airport import Airport

class Airport(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(self.Land(), True)




if __name__ == '__main__':
    unittest.main()
