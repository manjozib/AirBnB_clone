#!/usr/bin/python3
"""Module test_city.py
Tests for class City.
"""


import unittest
from models.city import City
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Tests for class City."""

    def test_issubclass(self):
        """chekc if the City class is subclass of BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_instantiation(self):
        """check if the object created is instance of City Class"""
        new_city = City()
        self.assertIsInstance(new_city, City)

    def test_attributes(self):
        """check if the attributes exist"""
        new_city = City()
        self.assertTrue(hasattr(City, "name"))
        self.assertTrue(hasattr(City, "state_id"))


if __name__ == '__main__':
    unittest.main()
