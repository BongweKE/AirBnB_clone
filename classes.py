#!/usr/bin/python3
''' Implements a console for the project.
'''


def cls_of(cls_name):
    ''' Returns the class object whose name is cls_name. '''

    from models.base_model import BaseModel
    from models.user import User
    from models.state import State
    from models.place import Place
    from models.city import City
    from models.amenity import Amenity
    from models.review import Review

    if cls_name == "BaseModel":
        return BaseModel
    elif cls_name == "User":
        return User
    elif cls_name == "State":
        return State
    elif cls_name == "Place":
        return Place
    elif cls_name == "City":
        return City
    elif cls_name == "Amenity":
        return Amenity
    elif cls_name == "Review":
        return Review
    else:
        raise NameError
