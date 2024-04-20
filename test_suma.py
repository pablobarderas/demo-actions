import unittest
from calculator import sum

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(2,2), 4 )
        self.assertEqual(sum(2,-2), 0 )
        self.assertEqual(sum(2,-3), -1 )

if __name__ == "__main__":
    unittest.main()