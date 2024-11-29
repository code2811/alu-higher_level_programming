import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_square_init(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_square_invalid_size(self):
        with self.assertRaises(ValueError):
            Square(-5)

    def test_update(self):
        s = Square(5)
        s.update(89, 10)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 10)

    def test_to_dictionary(self):
        s = Square(3, 1, 1, 10)
        self.assertEqual(
            s.to_dictionary(),
            {'id': 10, 'size': 3, 'x': 1, 'y': 1}
        )

if __name__ == "__main__":
    unittest.main()

