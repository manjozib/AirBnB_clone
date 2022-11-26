#!/usr/bin/python3
"""a class User that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Public class attributes

    Attributes:
        email (str): user email
        password (str): user password
        first_name (str): first name
        last_name (str): last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
