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
        __file_path = "file.json"
        __objects = {}

    def all(self):
        return __objects

    def new(self, obj):
    
    def save(self):
        with open('file.json', 'w') as outfile:
        json_object = json.dump(__objects, file.json)   

    def reload(self):
        with open('file.json') as json_file:
            data = json.load(json_file)
