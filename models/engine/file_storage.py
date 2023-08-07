#!/usr/bin/python3
"""
FileStorage class
"""
import json
from models.base_model import BaseModel

class FileStorage:
    """
    define some method and attributes
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        s = obj.__class__.__name__
        d = obj.id
        FileStorage.__objects["{}.{}".format(s, d)] = obj

    def save(self):
        b = {}
        for k, v in FileStorage.__objects.items():
            b[k] = v.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(z, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path) as k:
                a = json.load(k)
            m = a.values()
            for v in a.values():
                del v["__class__"]
                self.new(m)
        except FileNotFoundError:
            return
