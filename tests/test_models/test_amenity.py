#!/usr/bin/python3

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    def test_issubclass(self):
        """check if User class is sub class of BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_instantiation(self):
        """check if the object is instnace of the State class"""
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, Amenity)
    
    def test_attribute(self):
        new_aminty = Amenity()
        self.assertTrue(hasattr(Amenity, "name"))
