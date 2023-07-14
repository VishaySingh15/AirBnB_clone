#!/usr/bin/python3
"""

This module defines unittests for the User class

"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    This class contains all unittests for the user class
    """

    def test_create_user(self):
        """
        This method tests if a user can be created
        """

        self.usr = User()
        self.assertTrue(self.usr.__class__.__name__, "User")

    def test_save(self):
        """
        This method tests the save functionality
        """

        self.usr = User()
        self.usr.save()
        self.assertGreater(self.usr.updated_at, self.usr.created_at)

    def test_create_from_dict(self):
        """
        This method tests instance creation from dict
        """

        my_user = {"id": "d0ef8146-4664-4de5-8e89-096d667b728e",
                "created_at": "2017-09-28T21:11:42.848280",
                "updated_at": "2017-09-28T21:11:42.848294",
                "email": "airbnb_2@mail.com",
                "first_name": "John",
                "__class__": "User",
                "password": "root"}
        self.usr = User(**my_user)
        self.usr2 = User()
        self.assertEqual(self.usr.id, "d0ef8146-4664-4de5-8e89-096d667b728e")
        self.assertNotEqual(self.usr, self.usr2)

    def tearDown(self):
        """
        This method is called after every testcase to delete the instance
        """

        del self.usr
