from collections import deque


# Function to push an element in queue.
def enqueue(q, x):
	# code here
	if not q:
		q = deque([])
	q.append(x)


# Function to remove front element from queue.
def dequeue(q):
	# code here
	return q.leftpop()


# Function to find the front element of queue.
def front(q):
	# code here
	return q[0]


# Function to find an element in the queue.
def find(q, x):
	# code here
	return q.index(x)
