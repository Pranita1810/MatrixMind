import unittest 
from base import summ, sorting

# Test Case - 1
class TestBase(unittest.TestCase):
    def test_summ(self):
        self.assertEqual(summ(1,2), 3)


class SortingCheck(unittest.TestCase):
    def test_sortingfunction(self):
        array = [6,5,4,3,2,5,6,7]
        self.assertEqual(sorting(array), sorted(array))

if __name__ == "__main__":
    unittest.main()

"""
assertEqual(a, b)	    Checks a == b
assertNotEqual(a, b)	Checks a != b
assertTrue(x)	        Checks whether x is true
assertFalse(x)	        Checks whether x is false
assertIsNone(x)	        Checks whether x is None
assertIn(a, b)	        Checks whether a exists in b
"""