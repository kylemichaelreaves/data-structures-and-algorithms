# !/usr/bin/python
""" A modeule containing List class"""
from node import Node


class List:
    """Linked List class with a pre-defined Node class"""

    def __init__(self):
        """Initialize a List
        """
        self._head = None
        self._tail = None
        self._count = 0

    def get_size(self):
        """Return the size of the list

        Returns:
            int : size of the list
        """
        return self._count

    def access(self, index):
        """Access a node with its index

        Args:
            index: index of a specified node

        Returns:
            Node: a pointer of the specified node if the specifid node exists; None, otherwise
        """
        if index < 0 or index > self._count - 1:
            return None

        # access the front node
        if index == 0:
            return self._head

        # access the tail node
        if index == self._count - 1:
            return self._tail

        if index <= self.get_size() / 2:  # access the first half
            current = self._head
            for i in range(index):
                current = current.next
            return current
        else:  # access the second half
            current = self._tail
            for i in range(self.get_size() - index - 1):
                current = current.prev
            return current

        return None

    def insert(self, index, v):
        """Insert a valude to make the list maintain ascending order

        Args:
            v : data which can be saved in a node
            index : location of insertion, 0 is the location before the first element,
                    1 is the location after the first element

        Returns:
            Node: True, if the value is inserted succefully; False, otherwise
        """
        if index < 0 or index > self._count:
            return False

        n = Node(v)  # create a node

        # insert a node into an empty list
        if self.get_size() == 0:
            self._head = n
            self._tail = n
            self._count += 1
            return True

        # insert a node in the front
        if index == 0:
            n.next = self._head
            self._head.prev = n
            self._head = n
            self._count += 1
            return True

        # insert a node at the end
        if index == self.get_size():
            n.prev = self._tail
            self._tail.next = n
            self._tail = n
            self._count += 1
            return True

        if index <= self.get_size() / 2:
            current = self._head
            for i in range(index - 1):
                current = current.next
            n.next = current.next
            n.prev = current
            current.next.prev = n
            current.next = n
            self._count += 1
            return True
        else:
            current = self._tail
            for i in range(self.get_size() - index - 1):
                current = current.prev
            n.next = current
            n.prev = current.prev
            current.prev.next = n
            current.prev = n
            self._count += 1
            return True

        return False

    def delete(self, index):
        """Delete a valude located at a specific location in the list

        Args:
            index (int): location of deletion, 0 is the location before the first element, 1 is the location after the first element

        Returns:
            boolean: the value of removed node, if the node is deleted succefully; None, otherwise
        """
        if index < 0 or index > self._count - 1:
            return None

        if index == 0:
            n = self._head
            self._head = self._head.next
            self._head.prev = None
            self._count -= 1
            return n

        if index == self._count - 1:
            n = self._tail
            self._tail = self._tail.prev
            self._tail.next = None
            self._count -= 1
            return n

        if index <= self._count / 2:
            current = self._head
            for i in range(index - 1):
                current = current.next
            n = current.next
            current.next = current.next.next
            current.next.prev = current
            self._count -= 1
            return n
        else:
            current = self._tail
            for i in range(self.get_size() - index - 2):
                current = current.prev
            n = current.prev
            current.prev = current.prev.prev
            current.prev.next = current
            self._count -= 1
            return n

        return None

    def __str__(self):
        """Convert the list to a string

        Returns:
            string : a string represents the list
        """
        if self.get_size() == 0:
            return "Empty"

        current = self._head
        output = []

        while current is not None:
            output.append(str(current))
            current = current.next

        return " -> ".join(output)
