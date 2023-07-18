#!/usr/bin/python3
"""Class Base"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class Constructor"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """"
        Method shows the JSON string representation
        of a list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class method that writes the JSON string representation of
        list objects to a file
        """
        filename = cls.__name__ + ".json"
        temp_list = []
        with open(filename, "w") as json_file:
            if list_objs is None:
                json_file.write("")
            else:
                temp_list = [obj.to_dictionary() for obj in list_objs]
                json_file.write(Base.to_json_string(temp_list))

    @staticmethod
    def from_json_string(json_string):
        """"
        Static Method that returns the list of the JSON string
        representation of a list of dictionaries
        """
        if json_string is None or json_string == []:
            return ("[]")
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        Method returns an instance with all attributes aready set

        This method uses a "dummy" instance
        """
        dummy = None

        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """
        Class method that returns a list of instances
        """
        filename = cls.__name__ + ".json"
        temp_list = []

        try:
            with open(filename, "r") as json_file:
                json_list = json_file.read()
                obj_list = cls.from_json_string(json_list)
                temp_list = [cls.create(**obj) for obj in obj_list]
        except FileNotFoundError:
            pass
        return (temp_list)
