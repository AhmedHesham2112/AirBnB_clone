#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for other classes"""

import datetime
import uuid

class BaseModel:
    """Class BaseModel"""
    def __init__(self):
        """Initialize a new BaseModel.

        Args:
            id (str): The identity of the new BaseModel.
            created_at: The time the instance was created at
            updated_at: The time the instance was updated at
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        return "[" + type(self).__name__ + "]" + " (" + self.id + ") " + str(self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        my_dict = self.__dict__
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
