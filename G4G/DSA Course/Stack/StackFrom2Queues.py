from collections import deque

# Stack Class that acts as a queue


class Stack:
    def __init__(self):
        self.q = deque()

    # Push operation
    def push(self, data):
        # Get previous size of queue
        s = len(self.q)

        # Push the current element
        self.q.append(data)

        # Pop all the previous elements and put them after
        # current element
        for i in range(s):
            self.q.append(self.q.popleft())

    # Removes the top element
    def pop(self):
        if not self.q:
            print("No elements")
        else:
            self.q.popleft()

    # Returns top of stack
    def top(self):
        if not self.q:
            return
        return self.q[0]

    def size(self):
        return len(self.q)


if __name__ == "__main__":
    st = Stack()
    st.push(1)
    st.push(2)
    st.push(3)
    print("current size: ", st.size())
    print(st.top())
    st.pop()
    print(st.top())
    st.pop()
    print(st.top())
    print("current size: ", st.size())
