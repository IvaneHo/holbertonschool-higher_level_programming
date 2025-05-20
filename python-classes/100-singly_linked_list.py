#!/usr/bin/python3
"""Defines a Node and a SinglyLinkedList."""


class Node:
    """Node of a singly linked list."""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set data, must be int."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set next node, must be Node or None."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list with sorted insertion."""

    def __init__(self):
        """Initialize an empty list."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert value in sorted order (ascending)."""
        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Return string of all data values line by line."""
        values = []
        current = self.__head
        while current:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)
