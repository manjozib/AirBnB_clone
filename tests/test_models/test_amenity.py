#!/usr/bin/python3
"""Module amenity.py
Test for class Amenity.
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Tests for class Amenity."""

    def test_class(self):
        """check if the class is named correctly"""
        amenity = Amenity()
        self.assertEqual(amenity.__class__.__name__, "Amenity")

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


if __name__ == '__main__':
    unittest.main()
