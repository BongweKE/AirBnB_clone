#!/usr/bin/python3
""" The city module.
"""
import uuid
import datetime
from models.base_model import BaseModel


class City(BaseModel):
    """ Implementation of the City class.
    """

    state_id = ''
    name = ''
