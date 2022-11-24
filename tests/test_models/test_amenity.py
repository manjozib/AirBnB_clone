#!/usr/bin/python3

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    def test_issubclass(self):
        """check if Amenity class is subclass of BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_instantiation(self):
        """check if the object is instance of the Amenity class"""
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, Amenity)
    
    def test_attribute(self):
        """check if the attributes exist"""
        new_aminty = Amenity()
        self.assertTrue(hasattr(Amenity, "name"))
