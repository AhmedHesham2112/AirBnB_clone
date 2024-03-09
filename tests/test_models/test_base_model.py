#!/usr/bin/python3
"""Testing BaseModel that defines all common
attributes/methods for other classes"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import time


class TestBaseModel(unittest.TestCase):

    """Test Cases for the BaseModel class."""

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_id(self):
        """Test Cases for the BaseModel id."""

        b1 = BaseModel()
        b2 = BaseModel()
        self.assertIsInstance(b1, BaseModel)
        self.assertTrue(hasattr(b1, "id"))
        self.assertIsInstance(b1.id, str)
        self.assertNotEqual(b1.id, b2.id)

    def test_created_at(self):
        """Test Cases for the BaseModel created_at."""

        b1 = BaseModel()
        time.sleep(0.5)
        b2 = BaseModel()
        self.assertLess(b1.created_at, b2.created_at)

    def test_updated_at(self):
        """Test Cases for the BaseModel updated_at."""

        b1 = BaseModel()
        time.sleep(0.5)
        b2 = BaseModel()
        time_diff = b1.created_at-b1.updated_at
        self.assertLess(b1.updated_at, b2.updated_at)
        self.assertTrue(abs(time_diff.total_seconds()) < 0.01)

    def test_to_dict_type(self):
        """Tests the public instance method to_dict()."""

        b = BaseModel()
        d = b.to_dict()
        self.assertEqual(d["id"], b.id)
        self.assertEqual(d["__class__"], type(b).__name__)
        self.assertEqual(d["created_at"], b.created_at.isoformat())
        self.assertEqual(d["updated_at"], b.updated_at.isoformat())

    def test_to_dict_no_args(self):
        """Tests the public instance method to_dict() with no agruments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict()
        msg = "to_dict() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_to_dict_too_many_args(self):
        """Tests the public instance method to_dict()
        with too many agruments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict(self, 15165)
        msg = "to_dict() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)
