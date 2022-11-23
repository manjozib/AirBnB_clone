#!/usr/bin/python3

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    def test_issubclass(self):
        """chekc if the User class is subclass of BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_instantiation(self):
        """check if the object created is instance of User Class"""
        new_user = User()
        self.assertIsInstance(new_user, User)

    def test_attributes(self):
        """check if the attributes exist"""
        new_user = User()
        self.assertTrue(hasattr(User, "first_name"))
        self.assertTrue(hasattr(User, "email"))
        self.assertTrue(hasattr(User, "password"))
        self.assertTrue(hasattr(User, "last_name"))
