#!/usr/bin/python3
"""

This module defines the user class

"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This class contains the attributes and methods for the user instance
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
