import unittest
from resta import sub

class TestSum(unittest.TestCase):

    def test_sub(self):
        self.assertEqual(sub(4,2), 2 )
        self.assertEqual(sub(2,-2), 4 )
        self.assertEqual(sub(-4,3), -1 )

if __name__ == "__main__":
    unittest.main()