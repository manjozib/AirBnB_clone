#!/usr/bin/python3
"""a class City that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """
        Public class attribute

        Attributes:
            state_id (str): empty string: it will be the State.id
            name (str): empty string
        """
    state_id = ""
    name = ""
