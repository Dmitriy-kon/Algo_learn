from typing import Self


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next: Self = None
        self.prev: Self = None

    def __repr__(self) -> str:
        return f"{self.data}"


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None

    def push_front(self, data: Node) -> None:
        if self.head:
            prev_head = self.head
            self.head = data
            self.head.next = prev_head

            prev_head.prev = self.head
        else:
            self.head = data
            self.tail = data

    def push_back(self, data: Node) -> None:
        if self.tail:
            prev_tail = self.tail
            self.tail = data
            self.tail.prev = prev_tail

            prev_tail.next = self.tail
        else:
            self.head = data
            self.tail = data

    def instert_after(self, node: Node, new_node: Node) -> None:
        # new_node = Node(data)
        next_node = node.next

        if node == self.tail:
            self.push_back(new_node)
            return

        if not next_node:
            new_node.next = None
            node.next = new_node
            new_node.prev = node
            return

        next_node.prev = new_node
        new_node.next = next_node

        node.next = new_node
        new_node.prev = node

    def delete(self, node: Node) -> None:
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev

        if node.prev:
            node.prev.next = node.next
            node.prev = None
        if node.next:
            node.next.prev = node.prev
            node.next = None

    def pop_front(self) -> Node:
        self.delete(self.head)
        return self.head

    def pop_back(self) -> Node:
        self.delete(self.tail)
        return self.tail

    def merge_dll(self, dll: "DoublyLinkedList") -> None:
        if not self.tail:
            self.head = dll.head
            self.tail = dll.tail
            return

        if not dll.head:
            return

        prev_tail = self.tail

        prev_tail.next = dll.head
        dll.head.prev = prev_tail

        self.tail = dll.tail

    def revert(self):
        if not self.head:
            return

        current = self.head
        self.tail = current
        while current:
            current.prev, current.next = current.next, current.prev
            # Если current.prev равно None, значит мы достигли нового head списка
            if not current.prev:
                self.head = current
            current = current.prev

    def find_cycle_floid(self, get_elem: bool = False) -> bool | Node:
        slow = self.head
        fast = self.head
        flag = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                flag = True
                break
        if get_elem:
            return self.find_elem_in_cycle(fast)
        return flag

    def find_elem_in_cycle(self, fast):
        slow = self.head
        fast = fast

        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

    def __repr__(self) -> str:
        return f"LinkedList({self.head})"

    def __iter__(self):
        start = self.head
        while start:
            yield start
            start = start.next


nodes = [Node(i) for i in range(10)]
nodes2 = [Node(i) for i in range(10, 20)]
dll = DoublyLinkedList()
for node in nodes:
    dll.push_back(node)


for node in dll:
    print(node, end=" ")
print()
dll.revert()

for node in dll:
    print(node, end=" ")
# res = Node(-1)
# dll.instert_after(nodes[3], res)
# print()
# for node in dll:
#     print(node, end=" ")
# dll.delete(res)
# print()
# for node in dll:
#     print(node, end=" ")

# print()
# print(dll.tail)
