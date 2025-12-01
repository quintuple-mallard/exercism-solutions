from functools import reduce

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

    def __repr__(self):
        return f"Node({self._value}, {self._next})"

class LinkedList:
    def __init__(self, values = None):
        if values is None:
            self._head = None
        else:
            self._head = reduce(lambda node, val: Node(val, node), values, None)
        
    def __iter__(self):
        if self._head is None:
            return iter([])

        current = self._head
        yield current.value()
        while current.next() is not None:
            current = current.next() 
            yield current.value()

    def __len__(self):
        if self._head is None:
            return 0
        current = self._head
        count = 1
        while current.next() is not None:
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
        return LinkedList(list(self))
