#!/usr/bin/python3
"""
Module with class BaseModel
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    class BaseModel that defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        if kwarg:
            for k, v in kwargs.items():
                if k == "__class__":

