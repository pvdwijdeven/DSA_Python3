class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self):
        self.stack = []

    # String representation of the stack
    def __str__(self):
        return "".join([str(x) for x in self.stack])

    # Get the current size of the stack
    def getSize(self):
        return len(self.stack)

    # Check if the stack is empty
    def isEmpty(self):
        return self.stack == []

    # Get the top item of the stack
    def top(self):
        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.stack[-1]

    # Push a value into the stack.
    def push(self, value):
        self.stack.append(value)

    # Remove a value from the stack and return.
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        return self.stack.pop()
