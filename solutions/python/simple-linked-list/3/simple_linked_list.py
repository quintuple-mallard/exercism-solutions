import functools

class EmptyListException(Exception):
    pass


class Node:
    def __init__(self, value, next):
        self._value = value
        self._next = next
        
    def value(self):
        return self._value

    def next(self):
        return self._next

    def __str__(self):
        return f"Node({self._value}, {self._next})"


class LinkedList:
    def __init__(self, values = None):
        self._head = None
        if values is not None:
            for value in values:
                self.push(value)
        
    def __iter__(self):
        current = self._head
        while current is not None:
            yield current.value()
            current = current.next() 

    def __len__(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.next()
        return count
             
    def head(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")
        return self._head
        
    def push(self, value):
        self._head = Node(value, self._head)
    
    def pop(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")
        tmp = self._head.value()
        self._head = self._head.next()
        return tmp

    def reversed(self):
        return LinkedList(self)
