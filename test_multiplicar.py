import unittest
from calculator import mul

class TestMul(unittest.TestCase):

    def test_mul(self):
        self.assertEqual(mul(2, 2), 4 )
        self.assertEqual(mul(2, 0), 0 )
        self.assertEqual(mul(2, 1), 2 )

if __name__ == "__main__":
    unittest.main()