#!/usr/bin/python3
""" tests for Review class """
import unittest
import pep8
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """ tests for Review class """
    
    def test_pep(self):
        """ tests for pep8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "Pep has issues")