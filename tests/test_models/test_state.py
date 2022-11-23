#!/usr/bin/python3

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    def test_issubclass(self):
        """check if State class is sub class of BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_instantiation(self):
        """check if the object is instnace of the State class"""
        new_state = State()
        self.assertIsInstance(new_state, State)
    
    def test_attribute(self):
        """check if the attribute exist"""
        new_state = State()
        self.assertTrue(hasattr(State, "name"))
