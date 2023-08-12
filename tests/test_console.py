#!/usr/bin/python3
"""
Defines unittests for console.py.
"""
import os
import unittest
from unittest.mock import patch
from io import StringIO
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from models import storage


class TestHBNBCommand_prompting(unittest.TestCase):
    """Unittests for prompting of the HBNB command interpreter"""

    def test_prompt_start(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class TestHBNBCommand_help(unittest.TestCase):
    """Unittests for help cmd of the HBNB command interpreter"""

    def test_help_EOF(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual("EOF command to exit the program",
                             output.getvalue().strip())

    def test_help_all(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("help all")
            self.assertEqual("print All", output.getvalue().strip())

    def test_help_count(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("help count")
            self.assertEqual("Count instances of class",
                             output.getvalue().strip())

    def test_help_create(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("help create")
            self.assertEqual("create new instance", output.getvalue().strip())

    def test_help_destroy(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual("destroy", output.getvalue().strip())

    def test_help_help(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("help help")
            self.assertEqual(
                'List available commands with "help" or detailed help with "help cmd".', output.getvalue().strip())

    def test_help_quit(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("help quit")
            self.assertEqual("Quit command to exit the program",
                             output.getvalue().strip())

    def test_help_show(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("help show")
            self.assertEqual("show obj", output.getvalue().strip())

    def test_help_update(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("help update")
            self.assertEqual("Update", output.getvalue().strip())


class TestHBNBCommand_count(unittest.TestCase):
    """Unittests for count cmd of the HBNB command interpreter"""

    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_count_invalid_class_name(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.count()"))
            self.assertEqual("0",
                             output.getvalue().strip())

    def test_count_valid_class_name(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.count()"))
            self.assertEqual("1", output.getvalue().strip())


class TestHBNBCommand_quit(unittest.TestCase):
    """Unittests for count cmd of the HBNB command interpreter"""

    def test_quit(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))


class TestHBNBCommand_EOF(unittest.TestCase):
    """Unittests for Ctrl + d of the HBNB command interpreter"""

    def test_EOF(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


class TestHBNBCommand_create(unittest.TestCase):
    """Unittests for create cmd of the HBNB command interpreter"""

    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_create_missing_class(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual("** class name missing **",
                             output.getvalue().strip())

    def test_create_invalid_class_name(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual("** class doesn't exist **",
                             output.getvalue().strip())

    def test_create_class_user(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            key_name = "User.{}".format(output.getvalue().strip())
            self.assertIn(key_name, storage.all().keys())

    def test_create_class_BaseModel(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            key_name = "BaseModel.{}".format(output.getvalue().strip())
            self.assertIn(key_name, storage.all().keys())

    def test_create_class_Place(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            key_name = "Place.{}".format(output.getvalue().strip())
            self.assertIn(key_name, storage.all().keys())

    def test_create_class_State(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            key_name = "State.{}".format(output.getvalue().strip())
            self.assertIn(key_name, storage.all().keys())

    def test_create_class_City(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            key_name = "City.{}".format(output.getvalue().strip())
            self.assertIn(key_name, storage.all().keys())

    def test_create_class_Review(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            key_name = "Review.{}".format(output.getvalue().strip())
            self.assertIn(key_name, storage.all().keys())

    def test_create_class_Amenity(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            key_name = "Amenity.{}".format(output.getvalue().strip())
            self.assertIn(key_name, storage.all().keys())


class TestHBNBCommand_show(unittest.TestCase):
    """Unittests for show cmd of the HBNB command interpreter"""

    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_show_missing_class(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual("** class name missing **",
                             output.getvalue().strip())

    def test_show_invalid_class_name(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show MyModel"))
            self.assertEqual("** class doesn't exist **",
                             output.getvalue().strip())

    def test_show_missing_class_id(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('User.show()'))
            self.assertEqual("** instance id missing **",
                             output.getvalue().strip())

    def test_show_invalid_class_id(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('User.show("1")'))
            self.assertEqual("** no instance found **",
                             output.getvalue().strip())

    def test_show_class_user(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            cls_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("all User")
            user_dict = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('User.show("{}")'.format(cls_id))
            self.assertIn(output.getvalue().strip(), user_dict)

    def test_show_class_BaseModel(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            cls_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("all BaseModel")
            user_dict = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('BaseModel.show("{}")'.format(cls_id))
            self.assertIn(output.getvalue().strip(), user_dict)

    def test_show_class_Place(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            cls_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("all Place")
            user_dict = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('Place.show("{}")'.format(cls_id))
            self.assertIn(output.getvalue().strip(), user_dict)

    def test_show_class_State(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            cls_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("all State")
            user_dict = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('State.show("{}")'.format(cls_id))
            self.assertIn(output.getvalue().strip(), user_dict)

    def test_show_class_City(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            cls_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("all City")
            user_dict = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('City.show("{}")'.format(cls_id))
            self.assertIn(output.getvalue().strip(), user_dict)

    def test_show_class_Amenity(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            cls_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("all Amenity")
            user_dict = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('Amenity.show("{}")'.format(cls_id))
            self.assertIn(output.getvalue().strip(), user_dict)

    def test_show_class_Review(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            cls_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("all Review")
            user_dict = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('Review.show("{}")'.format(cls_id))
            self.assertIn(output.getvalue().strip(), user_dict)


class TestHBNBCommand_all(unittest.TestCase):
    """Unittests for all cmd of the HBNB command interpreter"""

    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_all_no_classes(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("all User")
            self.assertEqual('[]', output.getvalue().strip())

    def test_all_invalid_classes(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("all MyModel")
            self.assertEqual("** class doesn't exist **",
                             output.getvalue().strip())

    def test_all_classes_available(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("create Place")
            HBNBCommand().onecmd("create State")
            HBNBCommand().onecmd("create City")
            HBNBCommand().onecmd("create Amenity")
            HBNBCommand().onecmd("create Review")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("all")
            self.assertIn("User", output.getvalue().strip())
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertIn("Place", output.getvalue().strip())
            self.assertIn("State", output.getvalue().strip())
            self.assertIn("City", output.getvalue().strip())
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertIn("Review", output.getvalue().strip())


class TestHBNBCommand_destroy(unittest.TestCase):
    """Unittests for destroy cmd of the HBNB command interpreter"""

    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_destroy_missing_class(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertIn("** class name missing **",
                          output.getvalue().strip())

    def test_destroy_invalid_class(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Omartalat"))
            self.assertIn("** class doesn't exist **",
                          output.getvalue().strip())

    def test_destroy_missing_id(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy User"))
            self.assertIn("** instance id missing **",
                          output.getvalue().strip())

    def test_destroy_invalid_id(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('User.destroy("1")'))
            self.assertIn("** no instance found **", output.getvalue().strip())

    def test_destroy_user(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('create User')
            cls_id = output.getvalue().strip
            key_name = "User.{}".format(cls_id)
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('User.destroy("{}")'.format(cls_id))
            self.assertNotIn(key_name, storage.all().keys())

    def test_destroy_BaseModel(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('create BaseModel')
            cls_id = output.getvalue().strip
            key_name = "BaseModel.{}".format(cls_id)
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('BaseModel.destroy("{}")'.format(cls_id))
            self.assertNotIn(key_name, storage.all().keys())

    def test_destroy_Place(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('create Place')
            cls_id = output.getvalue().strip
            key_name = "Place.{}".format(cls_id)
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('Place.destroy("{}")'.format(cls_id))
            self.assertNotIn(key_name, storage.all().keys())

    def test_destroy_State(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('State User')
            cls_id = output.getvalue().strip
            key_name = "State.{}".format(cls_id)
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('State.destroy("{}")'.format(cls_id))
            self.assertNotIn(key_name, storage.all().keys())

    def test_destroy_City(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('create City')
            cls_id = output.getvalue().strip
            key_name = "City.{}".format(cls_id)
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('City.destroy("{}")'.format(cls_id))
            self.assertNotIn(key_name, storage.all().keys())

    def test_destroy_Amenity(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('create Amenity')
            cls_id = output.getvalue().strip
            key_name = "Amenity.{}".format(cls_id)
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('Amenity.destroy("{}")'.format(cls_id))
            self.assertNotIn(key_name, storage.all().keys())

    def test_destroy_Review(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('create Review')
            cls_id = output.getvalue().strip
            key_name = "Review.{}".format(cls_id)
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('Review.destroy("{}")'.format(cls_id))
            self.assertNotIn(key_name, storage.all().keys())


if __name__ == "__main__":
    unittest.main()
