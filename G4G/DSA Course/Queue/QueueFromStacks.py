def Push(x, stack1, stack2):
    """
    x: value to push
    stack1: list
    stack2: list
    """
    # code here
    stack1.append(x)


# Function to pop an element from queue by using 2 stacks.
def Pop(stack1, stack2):
    """
    stack1: list
    stack2: list
    """
    for i in range(len(stack1)):
        stack2.append(stack1.pop())
    res = stack2.pop()
    for i in range(len(stack2)):
        stack1.append(stack2.pop())
    return res
