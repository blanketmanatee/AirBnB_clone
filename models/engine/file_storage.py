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
    def __init__(self, file_path, objects):
        """ initialization """
        self.__file_path = file_path
        self.__objects = objects

    def all(self):
        return __objects

    def new(self, obj):
    
    def save(self):
    
    def reload(self):
