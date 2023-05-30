#!/usr/bin/python3
class Node:
    """A class that defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """
        Initialize a Node instance.

        Args:
            data (int): The data value of the node.
            next_node (Node, optional): The next node in the linked list. Defaults to None.
        
        Raises:
            TypeError: If data is not an integer.
            TypeError: If next_node is not None or a Node instance.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get the data value of the node.

        Returns:
            int: The data value of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data value of the node.

        Args:
            value (int): The new data value.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Get the next node in the linked list.

        Returns:
            Node: The next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the linked list.

        Args:
            value (Node): The next node.
        
        Raises:
            TypeError: If value is not None or a Node instance.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class that defines a singly linked list."""

    def __init__(self):
        """Initialize a SinglyLinkedList instance."""
        self.head = None

    def sorted_insert(self, value):
        """
        Insert a new node into the correct sorted position in the list (in increasing order).

        Args:
            value (int): The value of the new node.
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and value > current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Get a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return '\n'.join(values)
