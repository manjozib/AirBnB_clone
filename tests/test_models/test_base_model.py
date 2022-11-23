#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_instance(self):
        """test if an object is instance of a given class"""
        new_model = BaseModel()
        message = "new_model is not instance of BaseModel"
        self.assertIsInstance(new_model, BaseModel, message)

    def test_id(self):
        """test if an id is generated and has a type string"""
        new_model = BaseModel()
        self.assertNotEqual(new_model.id, None)
        self.assertEqual(type(new_model.id), str)

    def test_unique_id(self):
        """test if each id is unique"""
        model_one = BaseModel()
        model_two = BaseModel()
        self.assertNotEqual(model_one.id, model_two.id)

    def test_created_at(self):
        """test"""
        new_model = BaseModel()
        self.assertEqual(type(datetime.today()), type(new_model.created_at))

    def test_updated_at(self):
        """test"""
        new_model = BaseModel()
        self.assertEqual(type(datetime.today()), type(new_model.updated_at))

    def test_created_at_differ(self):
        """test if two instances are not created at the same time"""
        model_one = BaseModel()
        model_two = BaseModel()
        self.assertNotEqual(model_one.created_at, model_two.created_at)

    def test_created_and_updated(self):
        """check if update_at and created_at differ"""
        new_model = BaseModel()
        new_model.save()
        self.assertNotEqual(new_model.created_at, new_model.updated_at)

    def test_str(self):
        """test for the __str__ method"""
        new_model = BaseModel()
        new_model_str = new_model.__str__()
        self.assertIn("[BaseModel]", new_model_str)
        self.assertIn(f"({new_model.id})", new_model_str)

    def test_dir(self):
        """test for the to_dict() method"""
        new_model = BaseModel()
        new_model.name = "alx"
        self.assertIn('id', new_model.to_dict())
        self.assertIn('created_at', new_model.to_dict())
        self.assertIn('updated_at', new_model.to_dict())
        self.assertIn('name', new_model.to_dict())
