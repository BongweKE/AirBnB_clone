#!/usr/bin/python3
""" The review module.
"""
import uuid
import datetime
from models.base_model import BaseModel


class Review(BaseModel):
    """ Implementation of the review class.
    """

    place_id = ''
    user_id = ''
    text = ''
