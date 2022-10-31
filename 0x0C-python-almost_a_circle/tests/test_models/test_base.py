#!/usr/bin/python3
"""
Module to test the Base class and its methods
"""
import unittest
import models
import io


class testBase(unittest.TestCase):
    """
    Suite to test the Base class and its methods
    """
    def setUp(self):
        """
        This method is invoked for all the tests
        """
        Base._Base__nb_objects = 0

    def test_id(self):
        """
        tests instantiation without and with id attribute given
        """
        new = Base()
        self.assertEqual(new.id, 1)

        new = Base(30)
        self.assertEqual(new.id, 30)

    def test_id_nb_objects(self):
        """
        test nb_objects attribute
        """
        new = Base()
        new_1 = Base()
        new_2 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new_1.id, 2)
        self.assertEqual(new_2.id, 3)

    def test_mixed_id(self):
        """
        tests instantiation with mixed id
        """
        new = Base()
        new_1 = Base(40)
        new_2 = Base()
        new_3 = Base(100)
        self.assertEqual(new.id, 1)
        self.assertEqual(new_1.id, 40)
        self.assertEqual(new_2.id, 2)
        self.assertEqual(new_3.id, 100)

    def test_id_string(self):
        """
        tests instantiation with string id
        """
        new = Base("23")
        self.assertEqual(new.id, '23')

    def test_more_args(self):
        """
        tests intantiation with more arguments
        """
        with self.assertRaises(TypeError):
            new = Base(5, 20)

    def test_access_private_attrs(self):
        """
        tests access to private attributes
        """
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects
