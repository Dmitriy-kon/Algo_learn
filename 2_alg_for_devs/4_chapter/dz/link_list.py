from typing import Self
from array import array


class Node:
    def __init__(self, x: int, _next: Self | None = None):
        self.x = x
        self._next = _next


class LinkedList:
    def __init__(self):
        # Pointer to the beginning of the list
        self.begin: Node | None = None

    def push_front(self, x: int) -> None:
        """Adds element to the beginning of the list."""
        node = Node(x)
        node._next = self.begin
        self.begin = node

    def print(self) -> None:
        """This function could be useful for debugging and testing."""
        n = self.begin
        while n:
            print(n.x, end=" ")
            n = n._next
        print()

    def copy_every_second(self) -> "LinkedList":
        """
        This function should return copy of the list where every second element
        is removed. Initial list should not be changed. E.g. if we run
        copy_every_second on list [1, 2, 3, 4, 5, 6, 7, 100, 120, 162, 0, 1] new
        list with values [1, 3, 5, 7, 120, 0] should be returned.
        """
        # size = self.get_size()
        check = 1
        spam = self.begin
        new_list = LinkedList()
        last_added = None

        while spam:
            if check % 2 == 0:
                check += 1
                spam = spam._next
                continue

            # new_list.push_front(spam.x)
            # new_list.insert_after(new_list.begin, spam.x)
            if not new_list.begin:
                new_list.begin = Node(spam.x)
                last_added = new_list.begin
            else:
                new_node = Node(spam.x)
                last_added._next = new_node

                last_added = new_node

            spam = spam._next

            check += 1

        return new_list

    def get_size(self) -> int:
        """Returns number of elements in list."""
        size = 0
        spam = self.begin

        while spam:
            size += 1
            spam = spam._next

        return size

    def to_array(self) -> list[int | None]:
        """
        Converts our list to an array. New array is created with values the
        same as in list.
        """
        size = self.get_size()
        arr1 = array("i", [0] * size)
        start = 0
        spam = self.begin

        while start < size:
            # arr[start] = self.begin.x
            arr1[start] = spam.x
            spam = spam._next
            start += 1

        return arr1.tolist()

    def remove_after(self, x: Node) -> None:
        """
        Removes elements x._next from the list.
        O(1) time is expected.
        """
        # x._next = x._next._next
        if x._next:
            spam = x._next
            x._next = spam._next

    def insert_after(self, x: Node, val: int):
        """
        Inserts new element with value val right after the element x.
        O(1) time is expected
        """
        spam = x._next
        new_node = Node(val)

        x._next = new_node
        new_node._next = spam

    def filter_divisible(self, x: int):
        """
        Removes all elements from the list that are divisible by x.
        E.g. list {1, 2, 3, 4, 4, 10, 7}  after filter_divisible(2) would look like {1, 3, 7}.
        O(N) time is expected.
        """
        spam = self.begin
        while spam:
            if spam.x % x == 0:
                self.remove_after(spam)

            spam = spam._next

    def get_at(self, index: int) -> Node | None:
        """Returns Node from the list by index. O(N) time is expected."""
        # TODO IMPLEMENT THIS
        return None

    @classmethod
    def from_array(cls, a: list[int]) -> "LinkedList":
        """Creates LinkedList from python list."""
        l = cls()
        for item in a:
            l.push_front(item)
        return l


link_list = LinkedList()
link_list.push_front(1)
link_list.push_front(2)
link_list.push_front(3)
link_list.push_front(4)
link_list.push_front(5)
link_list.push_front(6)
link_list.push_front(7)
link_list.push_front(100)
link_list.push_front(120)
link_list.push_front(162)
link_list.push_front(0)
link_list.push_front(1)
link_list.print()

print(link_list.get_size())
print(link_list.to_array())
new_list = link_list.copy_every_second()
new_list.print()
new_list.remove_after(new_list.begin)
new_list.print()
new_list.remove_after(new_list.begin)
new_list.print()

new_list.insert_after(new_list.begin, 1)
print(new_list.to_array())
new_list.insert_after(new_list.begin, 3)
print(new_list.to_array())
new_list.insert_after(new_list.begin, 5)
new_list.print()

new_list.filter_divisible(2)
new_list.print()
