#!/usr/bin/python3
""" tests for BaseModel """
import unittest
import pep8
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ tests for BaseModel class """
    
    def test_pep(self):
        """ tests for pep8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Pep has issues")

    def test_class(self):
        """ tests instance of class """
        base = BaseModel()
        self.assertTrue(isinstance(base, BaseModel))
    
    def test_to_dict(self):
        """ tests dictionary """
        base = BaseModel()
        return_dict = base.to_dict()
        self.assertTrue(isinstance(return_dict, dict))
    
    def test_str(self):
        """ tests str """
        base = BaseModel()
        BaseStr = base.__str__()
        self.assertTrue(isinstance(BaseStr, str))
    