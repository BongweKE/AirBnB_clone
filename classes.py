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

    match cls_name:
        case "BaseModel":
            return BaseModel
        case "User":
            return User
        case "State":
            return State
        case "Place":
            return Place
        case "City":
            return City
        case "Amenity":
            return Amenity
        case "Review":
            return Review
        case _:
            raise NameError
