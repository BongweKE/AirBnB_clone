#!/usr/bin/env bash
"""A moduel to help not import all this in cases where we need them
or we're avoiding circular imports for our classes"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

expected = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


def get_class(obj_dict):
    """A function to return the class to use
    example:
    >>> ze_class = get_class({...., "__class__":"User",...})
    >>> new_user = ze_class()
    """
    return expected[obj_dict["__class__"]]
