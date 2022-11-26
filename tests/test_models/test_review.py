#!/usr/bin/python3
"""Module test_review.py
Tests for class Review.
"""


import unittest
from models.review import Review
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Tests for class Reiew."""

    def test_issubclass(self):
        """chekc if the Review class is subclass of BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_instantiation(self):
        """check if the object created is instance of Review Class"""
        new_review = Review()
        self.assertIsInstance(new_review, Review)

    def test_attributes(self):
        """check if the attributes exist"""
        new_review = Review()
        self.assertTrue(hasattr(Review, "place_id"))
        self.assertTrue(hasattr(Review, "user_id"))
        self.assertTrue(hasattr(Review, "text"))


if __name__ == '__main__':
    unittest.main()
