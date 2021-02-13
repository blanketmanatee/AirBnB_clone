#!/usr/bin/python3
""" serializes instances to JSON and deserializes JSON file to instances """

import json

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
    def __init__(self, file_path, __objects):
        """ initialization """
        __file_path = "file.json"
        __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        __objects = {}
        with open('self.file.json', 'w') as outfile:
            json.dump(__objects, outfile)   

    def reload(self):
        with open('self.__file_path', 'r') as json_file:
            data = json.load(json_file)
