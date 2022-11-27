#!/usr/bin/python3
""" The user module.
"""
import uuid
import datetime
from models.base_model import BaseModel


class User(BaseModel):
    """ Implementation of the User class.
    """

    email = ''
    password = ''
    first_name = ''
    last_name = ''
