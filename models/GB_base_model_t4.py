#!/usr/bin/env python3
"""
"""
import uuid
import datetime

class BaseModel:
    """

    """
    def __init__(self, *args, **kwargs):
        """Initialization of BaseModel instance
        """

        if len(kwargs) > 0:
            # Reload a saved instance
            del kwargs['__class__']
            kwargs['created_at'] = datetime.datetime.fromisoformat(kwargs['created_at'])
            kwargs['updated_at'] = datetime.datetime.fromisoformat(kwargs['updated_at'])
            self.__dict__.update(kwargs)
        else:
            # Create a new instance
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
