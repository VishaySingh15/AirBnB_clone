#!/usr/bin/python3
"""

This module defines the review class

"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This class defines all attributes for a review instance
    """

    place_id = ""
    user_id = ""
    text = ""
