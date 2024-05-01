# Python3 program to find the maximum for
# each and every contiguous subarray of
# size K

from collections import deque

# A Deque (Double ended queue) based
# method for printing maximum element
# of all subarrays of size K


def get_max_in_K(arr, N, K):
    """Create a Double Ended Queue, Qi that
    will store indexes of array elements.
    The queue will store indexes of useful
    elements in every window and it will
    maintain decreasing order of values from
    front to rear in Qi, i.e., arr[Qi.front[]]
    to arr[Qi.rear()] are sorted in decreasing
    order"""
    Qi = deque()
    res = []

    # Process first k (or first window)
    # elements of array
    for i in range(K):

        # For every element, the previous
        # smaller elements are useless
        # so remove them from Qi
        while Qi and arr[i] >= arr[Qi[-1]]:
            Qi.pop()

        # Add new element at rear of queue
        Qi.append(i)

    # Process rest of the elements, i.e.
    # from arr[k] to arr[n-1]
    for i in range(K, N):

        # The element at the front of the
        # queue is the largest element of
        # previous window, so print it
        res.append(arr[Qi[0]])
        # print(str(arr[Qi[0]]) + " ", end="")

        # Remove the elements which are
        # out of this window
        while Qi and Qi[0] <= i - K:

            # remove from front of deque
            Qi.popleft()

        # Remove all elements smaller than
        # the currently being added element
        # (Remove useless elements)
        while Qi and arr[i] >= arr[Qi[-1]]:
            Qi.pop()

        # Add current element at the rear of Qi
        Qi.append(i)

    # Print the maximum element of last window
    # print(str(arr[Qi[0]]))
    res.append(arr[Qi[0]])
    return res


# Driver's code
if __name__ == "__main__":
    arr = [12, 1, 78, 90, 57, 89, 56]
    K = 2

    # Function call
    print(get_max_in_K(arr, len(arr), K))
