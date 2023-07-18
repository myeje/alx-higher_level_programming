#!/usr/bin/python3
"""Class Base"""


import json
import csv
import os
import turtle


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Class method that serializes in CSV
        """
        filename = cls.__name__ + ".csv"

        with open(filename, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            if cls.__name__ == "Rectangle":
                fieldnames = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == "Square":
                fieldnames = ['id', 'size', 'x', 'y']

            writer.writerow(fieldnames)
            if list_objs is not None:
                for obj in list_objs:
                    row = [getattr(obj, field) for field in fieldnames]
                    writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """
        Class method that deserializes in CSV
        """
        filename = cls.__name__ + ".csv"
        temp_list = []

        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                header = next(reader)

                for row in reader:
                    dictionary = {k: int(v) for k, v in zip(header, row)}
                    instance = cls.create(**dictionary)
                    temp_list.append(instance)
        except FileNotFoundError:
            pass
        return (temp_list)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all the Rectangles and Squares
        """
        window = turtle.Screen()
        window.title("Shapes Drawing")
        window.bgcolor("white")

        pen = turtle.Turtle()
        pen.speed(2)

        pen.color("blue")
        for rect in list_rectangles:
            pen.penup()
            pen.goto(rect.x, rect.y)
            pen.pendown()
            pen.forward(rect.width)
            pen.right(90)
            pen.forward(rect.height)
            pen.right(90)
            pen.forward(rect.width)
            pen.right(90)
            pen.forward(rect.height)
            pen.right(90)

        pen.color("red")
        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            for _ in range(4):
                pen.forward(square.size)
                pen.right(90)

        window.exitonclick()
