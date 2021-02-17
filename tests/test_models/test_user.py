#!/usr/bin/python3
""" tests class User """
import unittest
import pep8
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ tests for User class """
    
    def test_pep(self):
        """ tests for pep8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "Pep has issues")