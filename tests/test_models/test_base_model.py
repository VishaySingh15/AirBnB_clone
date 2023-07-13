#!/usr/bin/python3
"""
Unittests for basemodel class
"""

import unittest
import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    This class defines unit tests for the BaseModel class
    """

    def test_create_instance(self):
        """
        Test the creation of an instance
        """

        self.bm = BaseModel()
        self.assertTrue(self.bm.__class__.__name__, "BaseModel")

    def test_save(self):
        """
        This method tests the save functionality
        """

        self.bm = BaseModel()
        self.bm.save()
        self.assertGreater(self.bm.updated_at, self.bm.created_at)

    def test_uuid_type(self):
        """
        This method tests the uuid type
        """

        self.bm = BaseModel()
        self.assertEqual((type(self.bm.id)), str)

    def test_create_from_dict(self):
        """
        This method tests instance creation from dict
        """

        my_model_json = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 
                'created_at': '2017-09-28T21:03:54.052298', 
                '__class__': 'BaseModel', 
                'my_number': 89, 
                'updated_at': '2017-09-28T21:03:54.052302', 
                'name': 'My_First_Model'}
        self.bm = BaseModel(**my_model_json)
        self.bm2 = BaseModel()
        self.assertEqual(type(self.bm.created_at), datetime.datetime)
        self.assertNotEqual(self.bm, self.bm2)

    def tearDown(self):
        """
        This method is called after every test case is run
        """

        del self.bm
