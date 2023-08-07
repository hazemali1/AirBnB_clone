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
        if kwarg:
            format_data = "%y-/%m-/%dT%H:%M:%S.%f"
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                if k == "created_at":
                    self.created_at = datetime.strptime\
                            (kwargs["created_at"], format_data)
                if k == "updated_at":
                    self.updated_at = datetime.strptime\
                            (kwargs["updated_at"], format_data)
                else:
                    setattr(self, k. v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
