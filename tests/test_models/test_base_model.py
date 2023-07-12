#!/usr/bin/env python3
"""
Unittests for basemodel class
"""

import unittest
from models import base_model

class TestBaseModel(unittest.TestCase):
    """
    This class defines unit tests for the BaseModel class
    """

    def setUp(self):
        """
        This method is called before every test is run
        """

        self.bm = base_model.BaseModel()

    def test_create_instance(self):
        """
        Test the creation of an instance
        """

        self.assertTrue(self.bm.__class__.__name__, "BaseModel")

    def test_save(self):
        """
        This method tests the save functionality
        """

        self.bm.save()
        self.assertGreater(self.bm.updated_at, self.bm.created_at)

    def test_uuid_type(self):
        """
        This method tests the uuid type
        """

        self.assertEqual((type(self.bm.id)), str)

    def tearDown(self):
        """
        This method is called after every test case is run
        """

        del self.bm
