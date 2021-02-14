#!/usr/bin/python3
""" serializes instances to JSON and deserializes JSON file to instances """

import json
from os.path import exists
from models.user import User


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

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        temp = {}
        for keys in self.__objects.keys():
            temp[keys] = self.__objects[keys].to_dict()
        with open(self.__file_path, 'w+') as j_file:
            json.dump(temp, j_file)

    def reload(self):
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as j_file:
                data = json.load(j_file)
