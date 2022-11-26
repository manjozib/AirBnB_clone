#!/usr/bin/python3
"""Module test_user.py
unittest for FileStorage.
"""


import unittest
from models.base_model import BaseModel
import models
from models.engine.file_storage import FileStorage
import os.path


class TestFileStorgar(unittest.TestCase):
    """Test FileStorage"""

    def test_all_notempty(self):
        """test if the function all works and new works"""
        new_model = BaseModel()
        models.storage.new(new_model)
        message = "the dictinary is not empty"
        self.assertIsNotNone(models.storage.all(), message)
        self.assertEqual(dict, type(models.storage.all()))

    def test_save(self):
        """test for the save file """
        if os.path.exists("file.json"):
            pass
        else:
            new_model = BaseModel()
            models.storage.save()
            file_exist = os.path.exists("file.json")
            self.assertTrue(file_exist)

    def test_relode(self):
        """ test the relode method"""
        new_model = BaseModel()
        models.storage.reload()
        new_next_model = models.storage.all()
        message = "instance recreated"
        self.assertIsNotNone(new_next_model, message)


if __name__ == '__main__':
    unittest.main()
