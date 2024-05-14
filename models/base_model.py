#!/usr/bin/env python3
""" Script for Defining the `BaseModel` """
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """A base class defining common attributes and methods for other classes.

    Public instance attributes:
        id: a unique identifier generated using uuid.uuid4().
        created_at: the datetime when an instance is created.
        updated_at: the datetime when an instance is last updated.

    Public instance methods:
        save(self): Updates 'updated_at' with the current datetime.
        to_dict(self): Returns a dictionary containing all instance attributes
                       in a serialized format.
    """

    def __init__(self, *args, **kwargs):
        """ Initialize a new instance of the BaseModel class

        Args:
            args -- list of arguments
            kwargs -- dict of arguments
        """

        # If kwargs isn't empty
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ Return a string representation of the instance """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Update the 'updated_at' attribute with the current datetime """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Serialize the instance attributes into a dictionary """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
