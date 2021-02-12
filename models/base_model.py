#!/usr/bin/python3

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
    def __init__(self):
        """ initialization """
        