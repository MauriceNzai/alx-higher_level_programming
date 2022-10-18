#!/usr/bin/python3
"""
This module implements unitest for the function max_integer([..])
Created on Tue Oct 18 2022
@author: Maurice Haro
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Class for testing 6-max_integer_test.py
    without arguments
    """
    def test_empty(self):
        """
        Test case if empty list is passed
        With no arguments
        """
        test_list = []
        self.assertEqual(max_integer(test_list), None)

    def test_one(self):
        """
        Test case if list has one element
        With no arguments
        """
        test_list = [1]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_first(self):
        """
        Test case if the first element is the max
        With no arguments
        """
        test_list = [10, 3, 5, 7, 4, 0]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_last(self):
        """
        Test case if the last element is the max
        With no arguments
        """
        test_list = [3, 8, 7, 4, 8, 4, 10]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_equal(self):
        """
        Test case if the all elements are equal
        With no arguments
        """
        test_list = [10, 10, 10, 10, 10]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_positive(self):
        """
        Test case with list of positive integers
        With no arguments
        """
        test_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_negative(self):
        """
        Test case with list of negative integers
        With no arguments
        """
        test_list = [-7, -2, -9, -4, -5]
        self.assertEqual(max_integer(test_list), max(test_list))


    def test_positive_negative(self):
        """
        Test case with list of both positive and negative integers
        With no arguments
        """
        test_list = [-1, 7, -2, 9, 3, -4, 5, -10]
        self.assertEqual(max_integer(test_list), max(test_list))


    def test_Positive_floats(self):
        """
        Test case with list of positive floats
        With no arguments
        """
        test_list = [1.3, 44.02, 2.36, 33.3, 33.0, 15.6]
        self.assertEqual(max_integer(test_list), max(test_list))


    def test_negative_floats(self):
        """
        Test case with list of negative floats
        With no arguments
        """
        test_list = [-1.3, -44.02, -2.36, -33.3, -33.0, -15.6]
        self.assertEqual(max_integer(test_list), max(test_list))


    def test_-tive_+tive_floats(self):
        """
        Test case with list of both positive and negative floats
        With no arguments
        """
        test_list = [11.3, -44.02, 2.36, -33.3, 33.0, -15.6]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_int_and_floats(self):
        """
        Test case with list of both positive and negative integers and floats
        With no arguments
        """
        test_list = [11.3, -4, 4.0, 2, 2.36, -33.3, 33, -15.6]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_combination(self):
        """
        Test case with list of any types combined
        With no arguments
        """
        test_list = [(11, 3), -44, '2', 2.36, -33.3, 'name', -15.6]
        self.assertEqual(max_integer(test_list), max(test_list))
