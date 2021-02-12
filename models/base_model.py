#!/usr/bin/python3
from datetime import datetime
import uuid


class BaseModel():
    """ 
    defines all common attributes/methods for other classes
    Public instance attributes
    id - string assigned with uuid when an instance is created
    created_at - datetime assign with current datetime when an instance is created
    updated_at - datetime assign with current datetime & updated when object is changed
    __str__ - should print [<class name>] (<self.id>) <self.__dict__>

    Public instance methods
    save(self) - updates updated_at with current datetime
    to_dict(self) - returns a dictionary containing all keys/values of __dict__ of the instance
    by using self.__dict__ only instance attributes are returned
    a key __class__ must be added to the dictionary w class name of object
    created_at and updated_at must be converted to string object in ISO format
    """
    def __init__(self, id='', created_at='', updated_at=''):
        """ initialization """
        self.id= str(uuid.uuid4())
        self.created_at= str(datetime.now)
        self.updated_at= str(datetime.now)
        
    def save(self):
        self.updated_at= str(datetime.now)
        
    def to_dict(self):
        new_dict = self.__dict__
        new_dict['__class__'] = type(self).__name__
        return new_dict
        
    def __str__(self):
        return ("[{}] ({}) {}".format(self).__class__, self.id, self.to_dict())
        