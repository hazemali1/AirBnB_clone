#!/usr/bin/python3
"""
Module with class BaseModel
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    class BaseModel that defines all common attributes/methods
    for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Instantiation
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                if k == "updated_at" or k == "created_at":
                    self.__dict__[k] = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, (self.id),
            self.__dict__)


    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        return self.__dict__

