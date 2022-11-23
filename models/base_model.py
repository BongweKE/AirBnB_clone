#!/usr/bin/env python3
"""
"""
import uuid
import datetime

class BaseModel:
    """

    """
    def __init__(self):
        """Initialization of BaseModel instance
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.utcnow()
        self.updated_at = datetime.datetime.utcnow()

    def __str__(self):
        """Definition of how an instance is represented to the user
        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        s = "[{}] ({}) {}".format(self.__class__.__name__,
                                  self.id,
                                  self.__dict__)
        return s

    def save(self):
        """A method that updates the public instance attribute
        `updated_at` with the current datetime
        """
        self.updated_at = datetime.datetime.utcnow()

    def to_dict(self):
        '''Returns a dictionary containing all key/values of the instance'''

        dct = dict(self.__dict__)

        crt_at_str = dct['created_at'].isoformat()
        dct['created_at'] = crt_at_str

        upd_at_str = dct['updated_at'].isoformat()
        dct['updated_at'] = upd_at_str

        dct.update(__class__=self.__class__.__name__)
        return dct