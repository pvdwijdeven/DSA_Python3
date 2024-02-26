from typing import Any


class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

    @property
    def var_next(self) -> Any:
        assert self.next
        return self.next


class Stack:
    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self) -> None:
        self.head = Node(data="head")
        self.size = 0

    # String representation of the stack
    def __str__(self) -> str:
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.data) + "->"
            cur = cur.next
        return out[:-3]

    # Get the current size of the stack
    def getSize(self) -> int:
        return self.size

    # Check if the stack is empty
    def isEmpty(self) -> bool:
        return self.size == 0

    # Get the top item of the stack
    def top(self) -> Any:
        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        assert self.head.next
        return self.head.next.data

    # Push a value into the stack.
    def push(self, value) -> None:
        temp = Node(data=value)
        temp.next = self.head.next
        assert self.head
        self.head.next = temp
        self.size += 1

    # Remove a value from the stack and return.
    def pop(self) -> Any:
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        assert self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        assert remove
        return remove.data
