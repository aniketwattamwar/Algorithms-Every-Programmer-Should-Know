class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


def main():
    stack = Stack()
    for value in (1, 2, 3):
        stack.push(value)
    print(f"Top: {stack.peek()}")
    print(f"Popped: {stack.pop()}")


if __name__ == "__main__":
    main()
