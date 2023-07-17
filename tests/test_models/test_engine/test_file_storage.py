#!/usr/bin/python3
"""

Unittests for FileStorage class

"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest


class TestFileStorage(unittest.TestCase):
    """
    This class defines unit tests for the FileStorage class
    """

    def setUp(self):
        """
        This method is called before every test case to create an instance of 
        FileStorage
        """

        self.storage = FileStorage("/AirBnB_clone/tests/test_models/file.json")
        self.bm = BaseModel()

    def test_create_storage_instance(self):
        """
        This method tests the creation of a FileStorage instance
        """

        self.assertTrue(type(self.storage), FileStorage)

    def test_new_and_all(self):
        """
        This method tests if new() adds the object to the objects dict
        and all() returns the dict list
        """

        self.storage.new(self.bm)
        self.assertIn("BaseModel." + self.bm.id, self.storage.all())

    def test_save_reload(self):
        """
        This method tests if save() adds object to file.json
        """

        self.storage.new(self.bm)
        self.storage.save()
        self.storage.__objects = ""
        self.storage.reload()
        self.assertIn("BaseModel." + self.bm.id, self.storage.all())

    def tearDown(self):
        """
        This method is called after every test case to
        delete the instance created
        """

        del self.storage
        del self.bm
