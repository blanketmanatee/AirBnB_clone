#!/usr/bin/python3
""" Tests class state """
import unittest
import pep8
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """ tests for State class """
    
    def test_pep(self):
        """ tests for pep8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "Pep has issues")