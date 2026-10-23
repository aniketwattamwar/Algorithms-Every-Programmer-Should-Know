from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.popleft()

    def front(self):
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0


def main():
    queue = Queue()
    for value in ("first", "second", "third"):
        queue.enqueue(value)
    print(f"Front: {queue.front()}")
    print(f"Dequeued: {queue.dequeue()}")


if __name__ == "__main__":
    main()
