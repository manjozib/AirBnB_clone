#!/usr/bin/python3
"""Define a Basemodel class """
import uuid
import datetime
import models


class BaseModel:
    """ defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """
        instantiation method

        Args:
            *args(any) - not used
            **kwargs(dict) - attribute name and values
        """
        if len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                elif k == 'created_at':
                    self.created_at = \
                        datetime.datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                elif k == 'updated_at':
                    self.updated_at = \
                        datetime.datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def save(self):
        """update the current time of updated_at attribute"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

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
