#!/usr/bin/python3
"""

This Module defines the class FileStorage
which serializes instances to JSON and vice versa

"""
import json
import os.path


class FileStorage():
    """
    This class serializes and deserializes instances and JSON
    """

    def __init__(self, file_path=None):
        """
        This method initializes an instance
        """

        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        """
        This method returns all objects
        """

        return self.__objects

    def new(self, obj):
        """
        This method adds a new instance to the objects dict list
        """

        obj_dict = obj.to_dict()
        key = obj_dict["__class__"] + "." + obj_dict["id"]
        self.__objects[key] = obj

    def save(self):
        """
        This method serializes the objects dict list to the file
        """

        objects_dict = {}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            for key, value in self.__objects.items():
                objects_dict[key] = value.to_dict()
            json.dump(objects_dict, f)

    def reload(self):
        """
        This method deserializes the JSON file to the dict list
        """

        file_path = os.path.isfile(self.__file_path)
        if file_path and os.path.getsize(self.__file_path) != 0:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                objects = json.load(f)
            from models.base_model import BaseModel
            from models.user import User
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.place import Place
            from models.review import Review
            for obj_id in objects:
                cls = obj_id.split('.')[0]
                args = str(objects[obj_id])
                exec("objects[obj_id] = " + cls + "(**" + args + ")")
            self.__objects = objects
