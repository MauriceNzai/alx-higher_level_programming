#!/usr/bin/python3
"""
Module to test the Square class and its methods
"""
import unittest
from io import StringIO
from unittest.mock import patch
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """
    Suite tests the Square class and its methods
    """
    def setUp(self):
        """
        This method is invoked for each test method
        """
        Base._Base__nb_objects = 0

    def test_new_square(self):
        """
        tests new square instance given size attr
        """
        new = Square(5)
        self.assertEqual(new.size, 5)
        self.assertEqual(new.width, 5)
        self.assertEqual(new.height, 5)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_new_square_1(self):
        """
        tests square instance given all attributes
        """
        new = Square(5, 2, 3, 4)
        self.assertEqual(new.size, 5)
        self.assertEqual(new.width, 5)
        self.assertEqual(new.height, 5)
        self.assertEqual(new.x, 2)
        self.assertEqual(new.y, 3)
        self.assertEqual(new.id, 4)

    def test_square_instances(self):
        """
        test instances of square
        """
        new = Square(2, 2)
        new_1 = Square(2, 2)
        self.assertEqual(False, new is new_1)
        self.assertEqual(False, new.id == new_1.id)

    def test_is_Base_instance(self):
        """
        tests if it is an instance of Base, and Rectangle classes
        """
        new = Square(5)
        self.assertEqual(True, isinstance(new, Base))
        self.assertEqual(True, isinstance(new, Rectangle))

    def test_no_attrs(self):
        """
        tests instantiation with no arguments, and more arguments passed
        """
        with self.assertRaises(TypeError):
            new = Square()
        with self.assertRaises(TypeError):
            new = Square(5, 1, 2, 3, 4)

    def test_access_private_attrs(self):
        """
        tests access to private attributes
        """
        new = Square(5)
        with self.assertRaises(AttributeError):
            new.__width
        with self.assertRaises(AttributeError):
            new.__height
        with self.assertRaises(AttributeError):
            new.__x
        with self.assertRaises(AttributeError):
            new.__y

    def test_attrs_validity(self):
        """
        tests if attributes given are valid
        """
        with self.assertRaises(TypeError):
            new = Square(5, 1, "2", 3)
        with self.assertRaises(ValueError):
            new = Square(0)
        with self.assertRaises(ValueError):
            new = Square(-5)

    def test_area(self):
        """
        tests return value of area() method
        """
        new = Square(2)
        self.assertEqual(new.area(), 4)

        new.size = 5
        self.assertEqual(new.area(), 25)

    def test_load_from_file(self):
        """
        tests load JSON file
        """
        load_file = Square.load_from_file()
        self.assertEqual(load_file, load_file)

    def test_dict_to_json(self):
        """
        tests dict to JSON string 
        """
        new = Square(2)
        dictionary = new.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        result = "[{}]\n".format(dictionary.__str__())

        with patch('sys.stdout', new=StringIO()) as string_out:
            print(json_dictionary)
            self.assertEqual(string_out.getvalue(), result.replace("'", "\""))

    def test_create_method(self):
        """
        tests the create() method
        """
        dictionary = {"id": 76}
        new = Square.create(**dictionary)
        self.assertEqual(new.id, 76)

        dictionary = {"id": 76,"size": 5}
        new = Square.create(**dictionary)
        self.assertEqual(new.id, 76)
        self.assertEqual(new.size, 5)

        dictionary = {"id": 76, "size": 5, "x": 2}
        new = Square.create(**dictionary)
        self.assertEqual(new.id, 76)
        self.assertEqual(new.size, 5)
        self.assertEqual(new.x, 2)
        self.assertEqual(new.y, 0)
        
        dictionary = {"id": 76, "size": 5, "x": 2, "y": 4}
        new = Square.create(**dictionary)
        self.assertEqual(new.id, 76)
        self.assertEqual(new.size, 5)
        self.assertEqual(new.x, 2)
        self.assertEqual(new.y, 4)
