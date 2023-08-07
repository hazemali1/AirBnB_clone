#!/usr/bin/python3
"""
FileStorage class
"""
import json


class FileStorage:
    """
    define some method and attributes
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        s = obj.__class__.__name__
        d = obj.id
        __objects["{}.{}".format(s, d)] = obj

    def save(self):
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)
