from collections import deque


def get_min_stack_at_pop(arr: list[int]) -> list[int]:

    # Function to push all the elements into the stack.
    def _push(arr: list[int]) -> deque[int]:
        stack: deque[int] = deque()
        # iterating over the array elements and pushing them into the stack.
        for i in arr:
            stack.append(i)
        return stack

    # Function to print minimum value in stack each time while popping.
    def _getMinAtPop(stack: deque[int]) -> deque[int]:
        reverseStack: deque[int] = deque()
        # storing the stack elements in reverse order in reverseStack.
        while len(stack):
            reverseStack.append(stack.pop())
        # now stack will be used as minStack:
        stack.append(reverseStack.pop())
        while len(reverseStack):
            # comparing the top element of original stack with top element of
            # reverseStack and pushing the minimum value into stack.
            if stack[-1] < reverseStack[-1]:
                stack.append(stack[-1])
                reverseStack.pop()
            else:
                stack.append(reverseStack.pop())
        # printing all the elements in stack one by one.
        return stack

    return list(_getMinAtPop(stack=_push(arr=arr)))[::-1]


def main() -> None:
    arr: list[int] = [1, 6, 43, 1, 2, 0, 5]
    print(get_min_stack_at_pop(arr=arr))


if __name__ == "__main__":
    main()
