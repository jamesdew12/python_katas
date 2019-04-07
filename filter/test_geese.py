import unittest
from geese import geese_filter

class TestHighPassFilter(unittest.TestCase):
    def test_python(self):
     self.assertEqual(geese_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]),["Mallard", "Hook Bill", "Crested", "Blue Swedish"])




if __name__ == '__main__':
    unittest.main()
