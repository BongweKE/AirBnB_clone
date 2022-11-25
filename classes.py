#!/usr/bin/python3
''' Implements a console for the project.
'''
from models.base_model import BaseModel
from models.user import User


def cls_of(cls_name):
    ''' Returns the class object whose name is cls_name. '''

    match cls_name:
        case "BaseModel":
            return BaseModel
        case "User":
            return User
        case _:
            raise NameError
