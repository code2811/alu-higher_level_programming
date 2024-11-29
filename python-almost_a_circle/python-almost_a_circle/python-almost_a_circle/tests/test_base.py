#!/usr/bin/python3
"""Unit tests for Base class"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def setUp(self):
        """Reset __nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_no_id(self):
        """Test id assignment when no id is provided"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_with_id(self):
        """Test id assignment when id is provided"""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_mixed_id_assignment(self):
        """Test mixed id assignments"""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)

if __name__ == '__main__':
    unittest.main()
