#!/usr/bin/python3
"""
Base class of the project

Created on Thur Oct, 27 2022

@author: Maurice Haro
"""
import json
import csv
import os


class Base():
    """
    Base class: Manages the id attribute

    Attributes:
        __no_objects: The number of instances
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializing the class instance variables

        Args:
        id (int): the id for a particular instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a JSON string representation of the list of dictionaries

        Args:
            list_dictionaries - a list of dictionaries

        Returns:
            JSON string representation
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of the list of objs to a file

        Args:
            cls - instance of class who inherits Base
            list_objs - a list of the instances
        """
        filename = cls.__name__ + ".json"
        with open(filename, mode='w', encoding='utf-8') as class_file:
            if list_objs is None:
                class_file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                class_file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns a Python object representation of a given JSON string

        Args:
            json_string - the JSON string to convert to a python obj

        Returns:
            The python obj
        """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns a class instatiated from a dictionary of attribute values

        Args:
            **dictionary (dict): key/value pairs of attribute values

        Returns:
            A class instantiated by the dictionary of values
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)

            new.update(**dictionary)

            return new

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of classes instantiated fron a JSON file
        Reads from <cls.__name__>.json

        Returns:
            An empty list if file does not exist
            Or a list of the instantiated clases
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, mode='r', encoding='utf-8') as class_file:
                list_dicts = Base.from_json_string(class_file.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return "[]"

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        serializes in CSV
        """
        filename = "{}.csv".format(cls.__name__)

        csvs = [x.to_dictionary() for x in list_objs]
        keys = csvs[0].keys()
        with open(filename, 'w') as f:
            writer = csv.DictWriter(f, keys)
            writer.writeheader()
            writer.writerows(csvs)

    @classmethod
    def load_from_file_csv(cls):
        """
        deserializes/loads a CSV file
        """
        filename = "{}.csv".format(cls.__name__)

        if not os.path.isfile(filename):
            return []

        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            csv_list = [row for row in reader]
            for row in csv_list:
                for key, value in row.items():
                    row[key] = int(value)

        return [cls.create(**dic) for dic in csv_list]
