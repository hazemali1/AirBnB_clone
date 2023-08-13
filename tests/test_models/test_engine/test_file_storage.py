#!/usr/bin/python3
"""
test for filestorage
"""
from models.engine.file_storage import FileStorage
import unittest
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class Test_for_file_stoarge(unittest.TestCase):
    """
    class testing filestorage
    """
    def test_for_file_path_type(self):
        """
        file_path type
        """
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_for_object_type(self):
        """
        object type
        """
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_for_all_type(self):
        """
        all() type
        """
        self.assertEqual(dict, type(models.storage.all()))

    def test_for_new_BaseModel(self):
        """
        new basemodel
        """
        s = BaseModel()
        models.storage.new(s)
        self.assertIn("BaseModel." + s.id, models.storage.all().keys())
        self.assertIn(s, models.storage.all().values())

    def test_for_new_User(self):
        """
        new User
        """
        s = User()
        models.storage.new(s)
        self.assertIn("User." + s.id, models.storage.all().keys())
        self.assertIn(s, models.storage.all().values())

    def test_for_new_State(self):
        """
        new State
        """
        s = State()
        models.storage.new(s)
        self.assertIn("State." + s.id, models.storage.all().keys())
        self.assertIn(s, models.storage.all().values())

    def test_for_new_Place(self):
        """
        new Place
        """
        s = Place()
        models.storage.new(s)
        self.assertIn("Place." + s.id, models.storage.all().keys())
        self.assertIn(s, models.storage.all().values())

    def test_for_new_City(self):
        """
        new City
        """
        s = City()
        models.storage.new(s)
        self.assertIn("City." + s.id, models.storage.all().keys())
        self.assertIn(s, models.storage.all().values())

    def test_for_new_Amenity(self):
        """
        new Amenity
        """
        s = Amenity()
        models.storage.new(s)
        self.assertIn("Amenity." + s.id, models.storage.all().keys())
        self.assertIn(s, models.storage.all().values())

    def test_for_new_Review(self):
        """
        new Review
        """
        s = Review()
        models.storage.new(s)
        self.assertIn("Review." + s.id, models.storage.all().keys())
        self.assertIn(s, models.storage.all().values())

    def test_for_save_BaseModel(self):
        """
        save basemodel
        """
        s = BaseModel()
        models.storage.new(s)
        models.storage.save()
        with open("file.json", "r") as d:
            obj = d.read()
            self.assertIn("BaseModel." + s.id, obj)

    def test_for_save_User(self):
        """
        save User
        """
        s = User()
        models.storage.new(s)
        models.storage.save()
        with open("file.json", "r") as d:
            obj = d.read()
            self.assertIn("User." + s.id, obj)

    def test_for_save_State(self):
        """
        save State
        """
        s = State()
        models.storage.new(s)
        models.storage.save()
        with open("file.json", "r") as d:
            obj = d.read()
            self.assertIn("State." + s.id, obj)

    def test_for_save_Place(self):
        """
        save Place
        """
        s = Place()
        models.storage.new(s)
        models.storage.save()
        with open("file.json", "r") as d:
            obj = d.read()
            self.assertIn("Place." + s.id, obj)

    def test_for_save_City(self):
        """
        save City
        """
        s = City()
        models.storage.new(s)
        models.storage.save()
        with open("file.json", "r") as d:
            obj = d.read()
            self.assertIn("City." + s.id, obj)

    def test_for_save_Amenity(self):
        """
        save Amenity
        """
        s = Amenity()
        models.storage.new(s)
        models.storage.save()
        with open("file.json", "r") as d:
            obj = d.read()
            self.assertIn("Amenity." + s.id, obj)

    def test_for_save_Review(self):
        """
        save Review
        """
        s = Review()
        models.storage.new(s)
        models.storage.save()
        with open("file.json", "r") as d:
            obj = d.read()
            self.assertIn("Review." + s.id, obj)

    def test_for_reload_BaseModel(self):
        """
        reload basemodel
        """
        s = BaseModel()
        models.storage.new(s)
        models.storage.save()
        models.storage.reload()
        obj = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + s.id, obj)

    def test_for_reload_User(self):
        """
        reload User
        """
        s = User()
        models.storage.new(s)
        models.storage.save()
        models.storage.reload()
        obj = FileStorage._FileStorage__objects
        self.assertIn("User." + s.id, obj)

    def test_for_reload_State(self):
        """
        reload State
        """
        s = State()
        models.storage.new(s)
        models.storage.save()
        models.storage.reload()
        obj = FileStorage._FileStorage__objects
        self.assertIn("State." + s.id, obj)

    def test_for_reload_Place(self):
        """
        reload Place
        """
        s = Place()
        models.storage.new(s)
        models.storage.save()
        models.storage.reload()
        obj = FileStorage._FileStorage__objects
        self.assertIn("Place." + s.id, obj)

    def test_for_reload_City(self):
        """
        reload City
        """
        s = City()
        models.storage.new(s)
        models.storage.save()
        models.storage.reload()
        obj = FileStorage._FileStorage__objects
        self.assertIn("City." + s.id, obj)

    def test_for_reload_Amenity(self):
        """
        reload Amenity
        """
        s = Amenity()
        models.storage.new(s)
        models.storage.save()
        models.storage.reload()
        obj = FileStorage._FileStorage__objects
        self.assertIn("Amenity." + s.id, obj)

    def test_for_reload_Review(self):
        """
        reload Review
        """
        s = Review()
        models.storage.new(s)
        models.storage.save()
        models.storage.reload()
        obj = FileStorage._FileStorage__objects
        self.assertIn("Review." + s.id, obj)


if __name__ == "__main__":
    unittest.main()
