#!/usr/bin/python3
""" The amenity module.
"""
import uuid
import datetime
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Implementation of the Amenity class.
    """

    name = ''
