#!/usr/bin/python3
""" The state module.
"""
import uuid
import datetime
from models.base_model import BaseModel


class State(BaseModel):
    """ Implementation of the State class.
    """

    name = ''
