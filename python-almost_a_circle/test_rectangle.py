import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_rectangle_init(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_invalid_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_rectangle_invalid_type_width(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_display(self):
        r = Rectangle(2, 2)
        output = "##\n##\n"
        with self.assertLogs() as logs:
            r.display()
        self.assertIn(output, logs.output)

if __name__ == "__main__":
    unittest.main()

