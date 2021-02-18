#!/usr/bin/python3
""" serializes instances to JSON and deserializes JSON file to instances """

import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity


class FileStorage():
    """
    private class attributes
    __file_path: string - path to JSON file
    __objects: dictionary - empty will store all objects by <class name>.id
    public instance methods
    all(self): returns the dictionary __objects
    new(self, obj): sets in __objects the obj with key <obj class name>.id
    save(self): serializes __objects to the JSON file
    reload(self): deserializes JSON file to __objects
    """

    __file_path = "file.json"
    __objects = {}
    class_ctrs = {"User": User, "City": City, "Place": Place, "State": State,
                  "Review": Review, "BaseModel": BaseModel, "Amenity": Amenity}

    def all(self):
        """ returns dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """  serializes __objects to the JSON file (path: __file_path) """
        temp = {}
        for keys in self.__objects.keys():
            temp[keys] = self.__objects[keys].to_dict()
        with open(self.__file_path, 'w+') as j_file:
            json.dump(temp, j_file)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing.
        If the file doesnt exist, no exception should be raised) """
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as j_file:
                data = json.load(j_file)
                for key in data.keys():
                    class_name = str(data[key]['__class__'])
                    if class_name in self.class_ctrs:
                        self.__objects[key] = self.class_ctrs[class_name](
                            **data[key])
