from __future__ import annotations
import functools
from typing import  Iterator, TypeVar, Optional

T = TypeVar('T')


class EmptyListException(Exception):
    pass


class Node:
    def __init__(self, value: T, next: Optional[Node]):
        self._value = value
        self._next = next
        
    def value(self) -> T:
        return self._value

    def next(self) -> Optional[Node]:
        return self._next

    def __str__(self):
        return f"Node({self._value}, {self._next})"


class LinkedList:
    def __init__(self, values: Optional[list[T]] = None):
        self._head = None
        if values is not None:
            for value in values:
                self.push(value)
        
    def __iter__(self) -> Iterator[T]:
        current = self._head
        while current is not None:
            yield current.value()
            current = current.next() 

    def __len__(self) -> int:
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.next()
        return count
             
    def head(self) -> Node[T]:
        if self._head is None:
            raise EmptyListException("The list is empty.")
        return self._head
        
    def push(self, value: T):
        self._head = Node(value, self._head)
    
    def pop(self) -> T:
        if self._head is None:
            raise EmptyListException("The list is empty.")
        tmp = self._head.value()
        self._head = self._head.next()
        return tmp

    def reversed(self) -> LinkedList[T]:
        return LinkedList(self)
