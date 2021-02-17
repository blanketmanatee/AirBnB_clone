#!/usr/bin/python3
""" Tests for place class """
import unittest
import pep8
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """ tests for Place class """
    
    def test_pep(self):
        """ tests for pep8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "Pep has issues")