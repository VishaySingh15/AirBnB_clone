#!/usr/bin/python3
"""

This module defines unittests for the Review class

"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    This class contains all unittests for the Review class
    """

    def test_create_obj(self):
        """
        This method tests if an instance can be created
        """

        self.obj = Review()
        self.assertTrue(self.obj.__class__.__name__, "Review")

    def test_save(self):
        """
        This method tests the save functionality
        """

        self.obj = Review()
        self.obj.save()
        self.assertGreater(self.obj.updated_at, self.obj.created_at)

    def test_create_from_dict(self):
        """
        This method tests instance creation from dict
        """

        my_obj = {"id": "d0ef8146-4664-4de5-8e89-096d667b728e",
                "created_at": "2017-09-28T21:11:42.848280",
                "updated_at": "2017-09-28T21:11:42.848294",
                "__class__": "Review"}
        self.obj = Review(**my_obj)
        self.obj2 = Review()
        self.assertEqual(self.obj.id, "d0ef8146-4664-4de5-8e89-096d667b728e")
        self.assertNotEqual(self.obj, self.obj2)

    def tearDown(self):
        """
        This method is called after every testcase to delete the instance
        """

        del self.obj
