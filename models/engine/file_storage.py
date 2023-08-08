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
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                             obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        dict1 = {}
        for k, v in FileStorage.__objects.items():
            dict1[k] = v.to_dict()
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as f:
            json.dump(dict1, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path) as file:
                data = json.load(file)
            for key, value in data.items():
                class_name = value["__class__"]
                if class_name == "BaseModel":
                    FileStorage.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            return
