import unittest
from calculator import div

class TestDiv(unittest.TestCase):

    def test_div(self):
        self.assertEqual(div(4,2), 2 )
        self.assertEqual(div(2,2), 1 )
        self.assertRaises(ZeroDivisionError, div, 4, 0)


if __name__ == "__main__":
    unittest.main()