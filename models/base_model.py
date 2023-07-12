#!/usr/bin/env python3
"""

This module defines the base model which all other models inherit.

"""
import datetime
import uuid

class BaseModel():
    """
    This class serves as a base model for all other classes
    """

    def __init__(self):
        """
        This method instantiates the object and initializes the public instance attributes
        id, created_at, updated_at
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Returns string representation of instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        This method updates the updated_at attribute to the current date
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        This method returns all kvp's of the instance
        """
        custom_dict = self.__dict__
        custom_dict['__class__'] = self.__class__.__name__
        custom_dict['created_at'] = custom_dict['created_at'].isoformat()
        custom_dict['updated_at'] = custom_dict['updated_at'].isoformat()
        return custom_dict