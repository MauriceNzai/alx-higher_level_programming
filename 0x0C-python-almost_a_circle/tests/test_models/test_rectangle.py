#!/usr/bin/python3
"""
Module to test the Rectangle class

Created on Sat Oct, 29 2022

@author: Maurice Haro
"""
import io
import unittest
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleMethods(unittest.TestCase):
    """
    Suite to test the Rectangle class and its methods
    """

    def setUp(self):
        """
        invoked for each test
        """
        Base.__base__nb_objs = 0

    def test_new_rectangle(self):
        """
        Tests new Rectangle instance
        """
        new = Rectangle(1, 1)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 1)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        #self.assertEqual(new.id, 1)


    def test_new_rectangle_2(self):
        """
        Tests new Rectangle with all attributes initalised
        """
        new = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 2)
        self.assertEqual(new.x, 3)
        self.assertEqual(new.y, 4)
        self.assertEqual(new.id, 5)


    def test_new_rectangles(self):
        """
        Tests new rectangles
        """
        new = Rectangle(1, 2)
        new2 = Rectangle(1, 2)
        self.assertEqual(False, new is new2)
        self.assertEqual(False, new.id == new2.id)


    def test_is_Base_instance(self):
        """
        tests if an object is an instance of Base
        """
        new = Rectangle(1, 2)
        self.assertEqual(True, isinstance(new, Base))


    def test_fewer_attributes(self):
        """
        tests few of attributes given to instsnce
        """
        with self.assertRaises(TypeError):
            new = Rectangle(1)


    def test_more_attributes(self):
        """
        test more attributes given to instance
        """
        with self.assertRaises(TypeError):
            new = Rectangle(1, 2, 3, 4, 5, 6)


    def test_no_attributes(self):
        """
        tests error with no attributes given to instance
        """
        with self.assertRaises(TypeError):
            new = Rectangle()


    def test_string_value(self):
        """
        test string values passed
        """
        with self.assertRaises(TypeError):
            new = Rectangle("1", 2, 3, "4", 5)


    def test_values(self):
        """
        test validity of values passed
        """
        with self.assertRaises(ValueError):
            new = Rectangle(0, 1)

    def test_negative(self):
        """
        tests negative values passed
        """
        with self.assertRaises(ValueError):
            new = Rectangle(1, -2, 3, -4)


    def test_area_return(self):
        """
        tests the return value of the area() method
        """
        new = Rectangle(10, 20)
        self.assertEqual(new.area(), 200)


    def test_area_return_1(self):
        """
        tests the attributes given and the return value of area() method
        """
        new = Rectangle(20, 10)
        self.assertEqual(new.area(), 200)
        new.width = 40
        self.assertEqual(new.area(), 400)
        new.height = 15
        self.assertEqual(new.area(), 600)


    def test_area_return_2(self):
        """
        test return values with re-instantiations
        """
        new = Rectangle(10, 20)
        self.assertEqual(new.area(), 200)
        new_2 = Rectangle(20, 25)
        self.assertEqual(new_2.area(), 500)


    def test_dict_to_json(self):
        """
        tests dict to JSON string
        """
        new = Rectangle(10, 20)
        dictionary = new.to_dictionary()
        json_dictionary = new.to_json_string([dictionary])
        result = "[{}]\n".format(dictionary.__str__())

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
            self.assertEqual(str_out.getvalue(), result.replace("'", "\""))


    def test_create(self):
        """
        tests the create() method
        """
        dictionary = {"id": 76}
        new = Rectangle.create(**dictionary)
        self.assertEqual(new.id, 76)


    def test_create_1(self):
        """
        tests the create() method
        """
        dictionary = {"id": 76, "width": 10, "height": 20}
        new = Rectangle.create(**dictionary)
        self.assertEqual(new.id, 76)
        self.assertEqual(new.width, 10)
        self.assertEqual(new.height, 20)

    
    def test_create_1(self):
        """
        tests the create() method
        """
        dictionary = {"id": 76, "width": 10, "height": 20, "x": 4, "y": 6}
        new = Rectangle.create(**dictionary)
        self.assertEqual(new.id, 76)
        self.assertEqual(new.width, 10)
        self.assertEqual(new.height, 20)
        self.assertEqual(new.x, 4)
        self.assertEqual(new.y, 6)

    def test_load_frm_file(self):
        """
        tests load JSON file() method
        """
        load_file = Rectangle.load_from_file()
        #self.assertEqual(load_file, [])


    def test_load_from_file_1(self):
        """
        test load JSON file() method
        """
        new = Rectangle(10, 10)
        new_1 = Rectangle(5, 8, 3, 4)

        source = [new, new_1]
        Rectangle.save_to_file(source)
        dest = Rectangle.load_from_file()

        for i in range(len(source)):
            self.assertEqual(source[i].__str__(), dest[i].__str__())
