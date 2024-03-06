#!/usr/bin/python3
"""Unittest module for the FileStorage class."""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import time

class TestFileStorage(unittest.TestCase):

    """Test Cases for the FileStorage class."""
    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_init(self):
        """Tests instantiation of storage class."""
        self.resetStorage()
        self.assertEqual(type(storage).__name__, "FileStorage")
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})
       
    
   

