#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_normal_list(self):
        list_test = [1, 2, 3, 4]
        self.assertEqual(max_integer(list_test), 4)

    def test_normal_list_unordered(self):
        list_test = [3, 1, 4, 2]
        self.assertEqual(max_integer(list_test), 4)

    def test_empty_list(self):
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_negative_num(self):
        list_test = [-1, -2, -3, -4]
        self.assertEqual(max_integer(list_test), -1)

    def test_single_element(self):
        list_test = [3]
        self.assertEqual(max_integer(list_test), 3)

    def test_duplicates(self):
        list_test = [1, 1, 1, 1]
        list_test2 = [-2, -2, -2, -2]
        self.assertEqual(max_integer(list_test), 1)
        self.assertEqual(max_integer(list_test2), -2)

    def test_floats(self):
        list_test = [2.5, 20.2, 15.76, 4.0, -3.878]
        self.assertEqual(max_integer(list_test), 20.2)

    def test_string(self):
        list_test = ['a', 'b', 'c']
        self.assertEqual(max_integer(list_test), 'c')

if __name__ == '__main__':
    unittest.main()
