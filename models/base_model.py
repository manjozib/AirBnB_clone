#!/usr/bin/python3
"""Define a Basemodel class """
import uuid
import datetime


class BaseModel:
    """ defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """instantiation method"""
        if bool(kwargs):
            self.id = kwargs['id']
            self.created_at = datetime.datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            self.my_number = kwargs['my_number']
            self.name = kwargs['name']
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def save(self):
        """update the current time of updated_at attribute"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """dictionary containing all keys/values of __dict__ of the instance:

        Returns:
            dict: a dictonalry containing all of the attributes
        """
        class_dictonary = self.__dict__.copy()
        class_dictonary["__class__"] = self.__class__.__name__
        class_dictonary["created_at"] = self.created_at.isoformat()
        class_dictonary["updated_at"] = self.updated_at.isoformat()
        return class_dictonary

    def __str__(self):
        """print [<class name>] (<self.id>) <self.__dict__>

        Returns:
            str: string reprsentation of the class
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
