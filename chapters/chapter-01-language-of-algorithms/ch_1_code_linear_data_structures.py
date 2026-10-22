from collections import deque
from typing import Any


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Node | None = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def display(self) -> None:
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))


class DNode:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: DNode | None = None
        self.prev: DNode | None = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: DNode | None = None

    def append(self, data: Any) -> None:
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def display_forward(self) -> None:
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print(" <-> ".join(elements))


class Stack:
    def __init__(self) -> None:
        self.items: list[Any] = []

    def push(self, item: Any) -> None:
        self.items.append(item)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def is_empty(self) -> bool:
        return len(self.items) == 0


class Queue:
    def __init__(self) -> None:
        self.items: deque[Any] = deque()

    def enqueue(self, item: Any) -> None:
        self.items.append(item)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.popleft()

    def front(self) -> Any:
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self.items[0]

    def is_empty(self) -> bool:
        return len(self.items) == 0


def main() -> None:
    linked_list = LinkedList()
    for value in (10, 20, 30):
        linked_list.append(value)
    print("Singly linked list:")
    linked_list.display()

    doubly_linked_list = DoublyLinkedList()
    for value in ("A", "B", "C"):
        doubly_linked_list.append(value)
    print("Doubly linked list:")
    doubly_linked_list.display_forward()

    stack = Stack()
    for value in (1, 2, 3):
        stack.push(value)
    print(f"Stack top: {stack.peek()}; popped: {stack.pop()}")

    queue = Queue()
    for value in ("first", "second", "third"):
        queue.enqueue(value)
    print(f"Queue front: {queue.front()}; dequeued: {queue.dequeue()}")


if __name__ == "__main__":
    main()
