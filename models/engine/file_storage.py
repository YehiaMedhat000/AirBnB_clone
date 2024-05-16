#!/usr/bin/env python3
""" Module for the `FileStorage` class definiton """
import json
from models.base_model import BaseModel
from models.review import Review
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.city import City

class FileStorage:
    """ Class for serializing instances to a JSON file
        and deserializing JSON file to instances

    Private class Attr:
        __file_path -- The file path where objects are saved
        __objects -- The list of objects to save

    Public methods:
        all -- Returns the dictionary __objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id

            Args:
                obj -- The object to assign in __objects dict
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """ Deserializes the JSON file to __objects. """
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = key.split('.')[0]
                    obj_cls = eval(class_name)
                    obj = obj_cls(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
