#!/usr/bin/python3
"""Testing BaseModel that defines all common attributes/methods for other classes"""

import unittest
from models.base_model import BaseModel
import time

class TestBaseModel(unittest.TestCase):

    """Test Cases for the BaseModel class."""

    def test_id(self):
        """Test Cases for the BaseModel id."""

        b1 = BaseModel()
        b2 = BaseModel()
        self.assertIsInstance(b1, BaseModel)
        self.assertTrue(hasattr(b1,"id"))
        self.assertIsInstance(b1.id, str)
        self.assertNotEqual(b1.id, b2.id)
    
    def test_created_at(self):
        """Test Cases for the BaseModel created_at."""

        b1 = BaseModel()
        time.sleep(0.5)
        b2 = BaseModel()
        self.assertLess(b1.created_at , b2.created_at)

    def test_updated_at(self):
        """Test Cases for the BaseModel updated_at."""

        b1 = BaseModel()
        time.sleep(0.5)
        b2 = BaseModel()
        time_diff = b1.created_at-b1.updated_at
        self.assertLess(b1.updated_at , b2.updated_at)
        self.assertTrue(abs(time_diff.total_seconds()) < 0.01)

