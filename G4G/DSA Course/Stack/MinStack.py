# Class to make a Node
class Node:
    # Constructor which assign argument to nade's value
    def __init__(self, value):
        self.value = value
        self.next: Node | None = None

    # This method returns the string representation of the object.
    def __str__(self):
        return "Node({})".format(self.value)

    # __repr__ is same as __str__
    __repr__ = __str__


# Stack class with get_minimum with O(1) time and O(n) space
class Stack:
    # Stack Constructor initialise top of stack and counter.
    def __init__(self):
        self.top = None
        self.count = 0
        self.minimum = None

    # This method returns the string representation of the object (stack).
    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = "\n".join(out)
        return "Top {} \n\nStack :\n{}".format(self.top, out)

    # __repr__ is same as __str__
    __repr__ = __str__

    # This method is used to get minimum element of stack
    def get_minimum(self):
        if self.top is None:
            return "Stack is empty"
        else:
            print("Minimum Element in the stack is: {}".format(self.minimum))

    # Method to check if Stack is Empty or not

    def is_empty(self):
        # If top equals to None then stack is empty
        if self.top == None:
            return True
        else:
            # If top not equal to None then stack is empty
            return False

    # This method returns length of stack
    def __len__(self):
        self.count = 0
        tempNode = self.top
        while tempNode:
            tempNode = tempNode.next
            self.count += 1
        return self.count

    # This method returns top of stack
    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            if self.top.value < self.minimum:
                print("Top Most Element is: {}".format(self.minimum))
            else:
                print("Top Most Element is: {}".format(self.top.value))

    # This method is used to add node to stack
    def push(self, value):
        if self.top is None:
            self.top = Node(value)
            self.minimum = value

        elif value < self.minimum:
            temp = (2 * value) - self.minimum
            new_node = Node(temp)
            new_node.next = self.top
            self.top = new_node
            self.minimum = value
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
        print("Number Inserted: {}".format(value))

    # This method is used to pop top of stack
    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            removedNode = self.top.value
            self.top = self.top.next
            if removedNode < self.minimum:
                print("Top Most Element Removed :{} ".format(self.minimum))
                assert self.minimum
                self.minimum = (2 * self.minimum) - removedNode
            else:
                print("Top Most Element Removed : {}".format(removedNode))


# Stack class with get_minimum with O(1) time and O(1) space
class Stack2:
    # Stack Constructor initialise top of stack and counter.
    def __init__(self):
        self.top = None
        self.count = 0
        self.minimum = None

    # This method returns the string representation of the object (stack).
    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = "\n".join(out)
        return "Top {} \n\nStack :\n{}".format(self.top, out)

    # __repr__ is same as __str__
    __repr__ = __str__

    # This method is used to get minimum element of stack
    def get_minimum(self):
        if self.top is None:
            return "Stack is empty"
        else:
            print("Minimum Element in the stack is: {}".format(self.minimum))

    # Method to check if Stack is Empty or not

    def is_empty(self):
        # If top equals to None then stack is empty
        if self.top == None:
            return True
        else:
            # If top not equal to None then stack is empty
            return False

    # This method returns length of stack
    def __len__(self):
        self.count = 0
        tempNode = self.top
        while tempNode:
            tempNode = tempNode.next
            self.count += 1
        return self.count

    # This method returns top of stack
    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            if self.top.value < self.minimum:
                print("Top Most Element is: {}".format(self.minimum))
            else:
                print("Top Most Element is: {}".format(self.top.value))

    # This method is used to add node to stack
    def push(self, value):
        if self.top is None:
            self.top = Node(value)
            self.minimum = value

        elif value < self.minimum:
            temp = (2 * value) - self.minimum
            new_node = Node(temp)
            new_node.next = self.top
            self.top = new_node
            self.minimum = value
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
        print("Number Inserted: {}".format(value))

    # This method is used to pop top of stack
    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            removedNode = self.top.value
            self.top = self.top.next
            if removedNode < self.minimum:
                print("Top Most Element Removed :{} ".format(self.minimum))
                assert self.minimum
                self.minimum = (2 * self.minimum) - removedNode
            else:
                print("Top Most Element Removed : {}".format(removedNode))


# Driver program to test above class
if __name__ == "__main__":

    stack = Stack()
    stack2 = Stack2()

    # Function calls
    stack.push(3)
    stack.push(5)
    stack.get_minimum()
    stack.push(2)
    stack.push(1)
    stack.get_minimum()
    stack.pop()
    stack.get_minimum()
    stack.pop()
    stack.peek()

    stack2.push(3)
    stack2.push(5)
    stack2.get_minimum()
    stack2.push(2)
    stack2.push(1)
    stack2.get_minimum()
    stack2.pop()
    stack2.get_minimum()
    stack2.pop()
    stack2.peek()
