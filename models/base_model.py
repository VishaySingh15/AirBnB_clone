#!/usr/bin/python3
"""

This module defines the base model which all other models inherit.

"""
import datetime
import uuid
from models import storage

class BaseModel():
    """
    This class serves as a base model for all other classes
    """

    def __init__(self, *args, **kwargs):
        """
        This method instantiates the object, initializes the public instance attributes
        id, created_at, updated_at for new objects; and updates the storage object list with a new object, 
        otherwise re-creates an existing object from kwargs.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    exec("self." + key + '=value')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        Returns string representation of instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        This method updates the updated_at attribute to the current date
        and calls the method to save to storage
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """
        This method returns all kvp's of the instance
        """
        custom_dict = self.__dict__
        custom_dict['__class__'] = self.__class__.__name__
        if type(custom_dict['created_at']) == datetime.datetime:
            custom_dict['created_at'] = custom_dict['created_at'].isoformat()
        if type(custom_dict['updated_at']) == datetime.datetime:
            custom_dict['updated_at'] = custom_dict['updated_at'].isoformat()
        return custom_dict
