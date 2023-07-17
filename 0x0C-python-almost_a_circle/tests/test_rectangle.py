#!/usr/bin/python3
"""Unittest for rectangle"""
import io
from io import StringIO
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class RectangleTestCase(unittest.TestCase):
    """Unit tests for rectangle class"""
    def setUp(self):
        self.rect = Rectangle(4, 6, 2, 3, 1)

    def test_attributes(self):
        self.assertEqual(self.rect.width, 4)
        self.assertEqual(self.rect.height, 6)
        self.assertEqual(self.rect.x, 2)
        self.assertEqual(self.rect.y, 3)
        self.assertEqual(self.rect.id, 1)

    def test_invalid_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-4, 6, 2, 3)

    def test_invalid_height(self):
        with self.assertRaises(ValueError):
            Rectangle(4, -6, 2, 3)

    def test_invalid_x(self):
        with self.assertRaises(ValueError):
            Rectangle(4, 6, -2, 3)

    def test_invalid_y(self):
        with self.assertRaises(ValueError):
            Rectangle(4, 6, 2, -3)

    def test_area(self):
        self.assertEqual(self.rect.area(), 24)

    def test_to_dictionary(self):
        expected_dict = {'x': 2, 'y': 3, 'id': 1, 'width': 4, 'height': 6}
        self.assertEqual(self.rect.to_dictionary(), expected_dict)

    def test_str_representation(self):
        expected_str = "[Rectangle] (1) 2/3 - 4/6"
        self.assertEqual(str(self.rect), expected_str)

    def test_update_with_args(self):
        self.rect.update(10, 8, 12, 5, 7)
        self.assertEqual(self.rect.id, 10)
        self.assertEqual(self.rect.width, 8)
        self.assertEqual(self.rect.height, 12)
        self.assertEqual(self.rect.x, 5)
        self.assertEqual(self.rect.y, 7)

    def test_update_with_kwargs(self):
        self.rect.update(id=10, width=8, height=12, x=5, y=7)
        self.assertEqual(self.rect.id, 10)
        self.assertEqual(self.rect.width, 8)
        self.assertEqual(self.rect.height, 12)
        self.assertEqual(self.rect.x, 5)
        self.assertEqual(self.rect.y, 7)


if __name__ == '__main__':
    unittest.main()
