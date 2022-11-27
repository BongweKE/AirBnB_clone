#!/usr/bin/python3
""" The BaseModel module.
"""
import uuid
import datetime
from models import storage


class BaseModel:
    """ Implementation of the BaseModel class.
    """
    def __init__(self, *args, **kwargs):
        """Initialization of BaseModel instance
        """

        if len(kwargs) > 0:
            # Reload a saved instance
            del kwargs['__class__']
            kwargs['created_at'] =\
                datetime.datetime.fromisoformat(kwargs['created_at'])
            kwargs['updated_at'] =\
                datetime.datetime.fromisoformat(kwargs['updated_at'])
            self.__dict__.update(kwargs)
        else:
            # Create a new instance
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.utcnow()
            self.updated_at = datetime.datetime.utcnow()
            storage.new(self)

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
        storage.save()

    def to_dict(self):
        '''Returns a dictionary containing all key/values of the instance'''

        dct = dict(self.__dict__)

        crt_at_str = dct['created_at'].isoformat()
        dct['created_at'] = crt_at_str

        upd_at_str = dct['updated_at'].isoformat()
        dct['updated_at'] = upd_at_str

        dct.update(__class__=self.__class__.__name__)
        return dct
