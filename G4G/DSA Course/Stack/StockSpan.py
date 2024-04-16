# Python linear time solution for stock span problem
# A stack based efficient method to calculate s
def calculateSpan(arr):

    n = len(arr)
    # Create a stack and push index of first element to it
    stack = []
    stack.append(0)
    res = [0] * n
    # Span value of first element is always 1
    res[0] = 1

    # Calculate span values for rest of the elements
    for i in range(1, n):

        # Pop elements from stack while stack is not
        # empty and top of stack is smaller than price[i]
        while len(stack) > 0 and arr[stack[-1]] <= arr[i]:
            stack.pop()

        # If stack becomes empty, then price[i] is greater
        # than all elements on left of it, i.e. price[0],
        # price[1], ..price[i-1]. Else the price[i] is
        # greater than elements after top of stack
        res[i] = i + 1 if len(stack) <= 0 else (i - stack[-1])

        # Push this element to stack
        stack.append(i)
    return res


def main():
    price = [10, 4, 5, 90, 120, 80]
    print(calculateSpan(arr=price))


if __name__ == "__main__":
    main()
