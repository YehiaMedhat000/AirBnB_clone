#!/usr/bin/env python3
""" Test module for the `BaseModel` """
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        del self.base_model

    def test_id_is_string(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_contains_class_name(self):
        obj_dict = self.base_model.to_dict()
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

    def test_init_with_kwargs(self):
        data = {
            'id': 'test_id',
            'created_at': '2023-05-15T12:30:45.678',
            'updated_at': '2023-05-15T13:45:50.123',
            'custom_attr': 'custom_value'
        }
        obj = BaseModel(**data)
        self.assertEqual(obj.id, 'test_id')
        self.assertEqual(obj.created_at,
                         datetime(2023, 5, 15, 12, 30, 45, 678000))
        self.assertEqual(obj.updated_at,
                         datetime(2023, 5, 15, 13, 45, 50, 123000))

    def test_init_with_empty_kwargs(self):
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_to_dict_datetime_format(self):
        data = {
            'id': 'test_id',
            'created_at': '2023-05-15T12:30:45.678',
            'updated_at': '2023-05-15T13:45:50.123',
            'custom_attr': 'custom_value'
        }
        obj = BaseModel(**data)
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict['created_at'], '2023-05-15T12:30:45.678000')
        self.assertEqual(obj_dict['updated_at'], '2023-05-15T13:45:50.123000')


if __name__ == '__main__':
    unittest.main()
