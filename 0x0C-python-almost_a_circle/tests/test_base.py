#!/usr/bin/python3
"""Unittest for base"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square



class BaseTestCase(unittest.TestCase):

    def test_init_with_id(self):
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

    def test_init_without_id(self):
        b2 = Base()
        self.assertEqual(b2.id, 1)

    def test_to_json_string_non_empty_list(self):
        dictionary_list = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
        json_string = Base.to_json_string(dictionary_list)
        expected_json = json.dumps(dictionary_list)
        self.assertEqual(json_string, expected_json)

    def test_to_json_string_empty_list(self):
        empty_list = []
        json_string = Base.to_json_string(empty_list)
        self.assertEqual(json_string, "[]")

    def test_save_to_file_none(self):
        Base.save_to_file(None)
        with open('Base.json', 'r') as json_file:
            self.assertEqual(json_file.read(), "")

    def test_from_json_string_empty(self):
        empty_json = "[]"
        obj_list = Base.from_json_string(empty_json)
        self.assertEqual(obj_list, [])

    def test_save_to_file_empty_list(self):
        Base.save_to_file([])
        with open('Base.json', 'r') as json_file:
            self.assertEqual(json_file.read(), "[]")

    def test_from_json_string_non_empty(self):
        json_string = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        obj_list = Base.from_json_string(json_string)
        expected_list = json.loads(json_string)
        self.assertEqual(obj_list, expected_list)

    
if __name__ == '__main__':
    unittest.main()
