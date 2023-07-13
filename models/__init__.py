#!/usr/bin/python3
"""

This module initializes the models package

"""
from models.engine.file_storage import FileStorage

storage = FileStorage("/AirBnB_clone/file.json")
storage.reload()
