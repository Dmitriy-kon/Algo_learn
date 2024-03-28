from typing import List, Optional


class Node:
    x: int
    _next: Optional["Node"]
    prev: Optional["Node"]

    def __init__(x: int, _next: Optional["Node"] = None, prev: Optional["Node"] = None):
        self.x = x
        self._next = _next
        self.prev = prev


class DLList:

    def __init__(self):
        #  You should store pointer to the first element of the list here
        self.begin: Optional[Node] = None
        #  You should store pointer to the last element of the list here
        self.end: Optional[Node] = None

    def push_front(self, x: int) -> None:
        """This method should add new element with value x to the front of the list."""

    def push_back(self, x: int) -> None:
        """This method should add new element with value x to the end of the list."""

    def print(self):
        """This method could be useful for debug purposes."""
        n = self.begin
        while n is not None:
            print(n.x, end=" ")
            n = n.next
        print("")

    def get_size(self) -> int:
        """This method should return the number of element in the list."""

    def to_array(self) -> List[int]:
        """This method should return an array with values the same as in list."""

    def remove(self, x: Node) -> None:
        """This method should remove the element x from the list."""

    def pop_front(self) -> int:
        """This method should remove first element in the list and return its value."""

    def pop_back(self) -> int:
        """This method should remove last element in the list and return its value."""

    def insert_after(self, x: Node, val: int) -> int:
        """This method should insert element with the value val after the element x."""

    def get_at(self, index: int) -> Node:
        """This method should return element at index."""

    @classmethod
    def from_array(cls, a: List[int]) -> "DLList":
        """This method construct list from the python list"""
        dllist = cls()
        for item in a:
            dllist.push_back(item)
        return dllist
