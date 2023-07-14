#!/usr/bin/python3
"""

This module defines the city class

"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    This class defines all attributes for a city instance
    """

    state_id = ""
    name = ""
