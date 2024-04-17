# Python3 program to print previous greater element
# An efficient solution to print previous greater
# element for every element in an array.
def previous_greater(arr) -> list[int]:
    n = len(arr)
    stack = []
    stack.append(arr[0])
    # Previous greater for first element
    # is always -1.
    res = [-1]

    # Traverse remaining elements
    for i in range(1, n):
        # Pop elements from stack while stack is
        # not empty and top of stack is smaller
        # than arr[i]. We always have elements in
        # decreasing order in a stack.
        while len(stack) > 0 and stack[-1] < arr[i]:
            stack.pop()
        # If stack becomes empty, then no element
        # is greater on left side. Else top of stack
        # is previous greater.
        if len(stack) == 0:
            res.append(-1)
        else:
            res.append(stack[-1])
        stack.append(arr[i])
    return res


def main() -> None:
    arr = [10, 4, 2, 20, 40, 12, 30]
    n = len(arr)
    print(previous_greater(arr=arr))


if __name__ == "__main__":
    main()
