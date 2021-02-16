#!/usr/bin/python3
""" This module is used for the Base Model of the AirBNB Clone """
from datetime import datetime
import uuid
from models import storage


class BaseModel():
    """
    defines all common attributes/methods for other classes
    Public instance attributes
    id - string assigned with uuid when an instance is created
    created_at - current datetime when an instance is created
    updated_at - current datetime updated when object is changed
    __str__ - should print [<class name>] (<self.id>) <self.__dict__>
    Public instance methods
    save(self) - updates updated_at with current datetime
    to_dict(self) - returns a dictionary representation of the instance
    by using self.__dict__ only instance attributes are returned
    a key __class__ must be added to the dictionary w class name of object
    created_at and updated_at must be converted to string object in ISO format
    """
    def __init__(self, *args, **kwargs):
        """ initialization """
        if len(kwargs) > 1:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "created_at":
                    self.created_at = str(value)
                if key == "updated_at":
                    self.updated_at = str(value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            storage.new(self)

    def save(self):
        """  updates the public instance attribute updated_at with the
        current datetime """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of 
        __dict__ of the instance """
        new_dict = self.__dict__
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = datetime.isoformat(self.created_at)
        new_dict['updated_at'] = datetime.isoformat(self.updated_at)
        return new_dict

    def __str__(self):
        """ should print: [<class name>] (<self.id>) <self.__dict__> """
        return f"[{self.__class__.__name__}] " + f'({self.id}) {self.__dict__}'
