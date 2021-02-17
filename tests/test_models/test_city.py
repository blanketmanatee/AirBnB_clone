#!/usr/bin/python3
""" Tests for City """
import unittest
import pep8
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """ tests for City class """
    
    def test_pep(self):
        """ tests for pep8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "Pep has issues")