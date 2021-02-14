#!/usr/bin/python3
""" User class """
from models.base_model import BaseModel


class User(BaseModel):
    """
    Public class attributes
    email - empty str
    password - empty str
    first_name - empty str
    last_name - empty str
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    