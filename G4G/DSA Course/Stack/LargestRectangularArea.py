# Python3 program to find maximum
# rectangular area in linear time
def max_area_histogram(histogram) -> int:

    # This function calculates maximum
    # rectangular area under given
    # histogram with n bars

    # Create an empty stack. The stack
    # holds indexes of histogram[] list.
    # The bars stored in the stack are
    # always in increasing order of
    # their heights.
    stack: list[int] = list()

    max_area: int = 0  # Initialize max area

    # Run through all bars of
    # given histogram
    index: int = 0
    while index < len(histogram):

        # If this bar is higher
        # than the bar on top
        # stack, push it to stack

        if (not stack) or (histogram[stack[-1]] <= histogram[index]):
            stack.append(index)
            index += 1

        # If this bar is lower than top of stack,
        # then calculate area of rectangle with
        # stack top as the smallest (or minimum
        # height) bar.'i' is 'right index' for
        # the top and element before top in stack
        # is 'left index'
        else:
            # pop the top
            top_of_stack: int = stack.pop()

            # Calculate the area with
            # histogram[top_of_stack] stack
            # as smallest bar
            area: int = histogram[top_of_stack] * (
                (index - stack[-1] - 1) if stack else index
            )

            # update max area, if needed
            max_area = max(max_area, area)

    # Now pop the remaining bars from
    # stack and calculate area with
    # every popped bar as the smallest bar
    while stack:

        # pop the top
        top_of_stack: int = stack.pop()

        # Calculate the area with
        # histogram[top_of_stack]
        # stack as smallest bar
        area: int = histogram[top_of_stack] * (
            (index - stack[-1] - 1) if stack else index
        )

        # update max area, if needed
        max_area: int = max(max_area, area)

    # Return maximum area under
    # the given histogram
    return max_area


# Python3 code for the above approach


def get_max_area(arr) -> int:
    s: list[int] = [-1]
    n: int = len(arr)
    area: int = 0
    i: int = 0
    left_smaller: list[int] = [-1] * n
    right_smaller: list[int] = [n] * n
    while i < n:
        while s and (s[-1] != -1) and (arr[s[-1]] > arr[i]):
            right_smaller[s[-1]] = i
            s.pop()
        if (i > 0) and (arr[i] == arr[i - 1]):
            left_smaller[i] = left_smaller[i - 1]
        else:
            left_smaller[i] = s[-1]
        s.append(i)
        i += 1
    for j in range(0, n):
        area: int = max(area, arr[j] * (right_smaller[j] - left_smaller[j] - 1))
    return area


# Driver code
if __name__ == "__main__":
    hist = [6, 2, 5, 4, 5, 1, 6]

    # Function call
    print("maxArea = ", get_max_area(hist))
    print("Maximum area is", max_area_histogram(histogram=hist))
