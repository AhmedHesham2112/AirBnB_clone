#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for other classes"""

import datetime
import uuid
import models


class BaseModel:
    """Class BaseModel"""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            id (str): The identity of the new BaseModel.
            created_at: The time the instance was created at
            updated_at: The time the instance was updated at
        """
        if len(kwargs) != 0:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.datetime.strptime
                    (kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.datetime.strptime
                    (kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        return "[" + type(self).__name__ + "]" + " (" + self.id + ") " + str(self.__dict__)

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
