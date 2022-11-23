#!/usr/bin/python3

import unittest
from models.city import City
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    def test_issubclass(self):
        """chekc if the User class is subclass of BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_instantiation(self):
        """check if the object created is instance of User Class"""
        new_city = City()
        self.assertIsInstance(new_city, City)

    def test_attributes(self):
        """check if the attributes exist"""
        new_city = City()
        self.assertTrue(hasattr(City, "name"))
        self.assertTrue(hasattr(City, "state_id"))
