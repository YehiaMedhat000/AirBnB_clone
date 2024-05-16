#!/usr/bin/env python3
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path
        self.obj1 = BaseModel()
        self.obj2 = BaseModel()
        self.obj3 = BaseModel()
        self.storage.new(self.obj1)
        self.storage.new(self.obj2)
        self.storage.new(self.obj3)
        self.storage.save()

    def tearDown(self):
        self.storage._FileStorage__objects = {}
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_reload(self):
        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()
        self.assertIn("BaseModel." + self.obj1.id, new_storage.all())
        self.assertIn("BaseModel." + self.obj2.id, new_storage.all())
        self.assertIn("BaseModel." + self.obj3.id, new_storage.all())

    def test_all(self):
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertIn("BaseModel." + self.obj1.id, all_objs)
        self.assertIn("BaseModel." + self.obj2.id, all_objs)
        self.assertIn("BaseModel." + self.obj3.id, all_objs)

    def test_new(self):
        obj4 = BaseModel()
        self.storage.new(obj4)
        self.assertIn("BaseModel." + obj4.id, self.storage.all())

    def test_save(self):
        file_exists = os.path.isfile(self.file_path)
        self.assertTrue(file_exists)

    def test_save_contents(self):
        with open(self.file_path, 'r') as file:
            data = file.read()
            self.assertIn("BaseModel." + self.obj1.id, data)
            self.assertIn("BaseModel." + self.obj2.id, data)
            self.assertIn("BaseModel." + self.obj3.id, data)

    def test_save_format(self):
        with open(self.file_path, 'r') as file:
            data = file.read()
            self.assertIn('"__class__": "BaseModel"', data)
            self.assertIn('"created_at": "{}"'.
                          format(self.obj1.created_at.isoformat()), data)
            self.assertIn('"updated_at": "{}"'.
                          format(self.obj1.updated_at.isoformat()), data)

    def test_save_update(self):
        obj_id = self.obj1.id
        old_updated_at = self.obj1.updated_at
        self.obj1.save()
        self.storage.save()
        new_updated_at = self.storage.all()["BaseModel." + obj_id].updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)


if __name__ == '__main__':
    unittest.main()
