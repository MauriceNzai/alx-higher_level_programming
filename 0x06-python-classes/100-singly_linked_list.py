#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thur Oct 13 2022
@author: Maurice Haro
"""


class Node:
    """Modelling a Node class with attributes

    Attributes:
        data: The data part of the Node
        next_node: Points to the next Node
    """

    def __init__(self, data, next_node=None):
        """The __init__ methode to initialise instance attributes

        Args:
            data: The data part of the Node
            next_node: Points to the next Node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Gets the data of the node

        Returns:
            The data of the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data property and checks for errors

        Args:
            value: Data value to be checked

        Raises:
            TypeError: Exception if value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets the next_node property

        Returns:
            The next_node
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Sets the next_node property and checks for errors

        Args:
            value: The item to check

        Raises:
            TypeError: Exception if value is not a Node
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Modelling the SinglyLinkedList class

    Attributes:
        head: The head of the linked list
    """

    def __str__(self):
        """Creating the __str__ method

        Args:

        Returns:
            The rtn attribute
        """
        rtn = ""
        ptr = self.__head

        while ptr is not None:
            rtn += str(ptr.data)
            if ptr.next_node is not None:
                rtn += "\n"
            ptr = ptr.next_node

        return rtn

    def __init__(self):
        """The __init__ method to initialise the attributes

        Args:
            head: The head of the Node
        """
        self.__head = None

    def sorted_insert(self, value):
        """Inserts to the node in sorted manner

        Args:
        value: The value to insert
        """
        ptr = self.__head

        while ptr is not None:
            if ptr.data > value:
                break
            ptr_prev = ptr
            ptr = ptr.next_node

        newNode = Node(value, ptr)
        if ptr == self.__head:
            self.__head = newNode
        else:
            ptr_prev.next_node = newNode
