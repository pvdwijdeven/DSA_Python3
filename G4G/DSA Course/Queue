from collections import deque


class Solution:
    """
    Function Arguments :
                @param  : q (given list on which queue is implemented)
                @param  : x (value to be used accordingly)
                @return : None
    """

    # Function to push an element in queue.
    def enqueue(self, q, x):
        # code here
        if q == None:
            q = deque([])
        q.append(x)

    # Function to remove front element from queue.
    def dequeue(self, q):
        # code here
        return q.leftpop()

    # Function to find the front element of queue.
    def front(self, q):
        # code here
        return q[0]

    # Function to find an element in the queue.
    def find(self, q, x):
        # code here
        return q.index(x)
