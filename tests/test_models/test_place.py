#!/usr/bin/python3
"""Module test_place.py
Tests for class Place.
"""


import unittest
from models.place import Place
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Tests for class Place."""

    def test_issubclass(self):
        """check if Place class is sub class of BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_instantiation(self):
        """check if the object is instnace of the Aminty class"""
        new_place = Place()
        self.assertIsInstance(new_place, Place)

    def test_attribute(self):
        """check if the attributes exist"""
        new_place = Place()
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertTrue(hasattr(Place, "user_id"))
        self.assertTrue(hasattr(Place, "name"))
        self.assertTrue(hasattr(Place, "description"))
        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertTrue(hasattr(Place, "number_bathrooms"))
        self.assertTrue(hasattr(Place, "max_guest"))
        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertTrue(hasattr(Place, "latitude"))
        self.assertTrue(hasattr(Place, "longitude"))
        self.assertTrue(hasattr(Place, "amenity_ids"))


if __name__ == '__main__':
    unittest.main()
