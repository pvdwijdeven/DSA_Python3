class TwoStacks:
    def __init__(self, n):
        self.n = n
        self.stack = [0] * self.n
        self.left_n = 0
        self.right_n = 0

    # Function to push an integer into stack 1
    def push1(self, x):
        if (self.left_n + self.right_n) < self.n:
            self.left_n += 1
            self.stack[self.left_n] = x
        else:
            print("stack1 full!")

    # Function to push an integer into stack 2
    def push2(self, x):
        if (self.left_n + self.right_n) < self.n:
            self.right_n += 1
            self.stack[self.n - 1 - self.right_n] = x
        else:
            print("stack2 full!")

    # Function to remove an element from top of stack 1
    def pop1(self):
        if self.left_n > 0:
            res = self.stack[self.left_n]
            self.left_n -= 1
        else:
            res = -1
        return res

    # Function to remove an element from top of stack 2
    def pop2(self):
        if self.right_n > 0:
            res = self.stack[self.n - 1 - self.right_n]
            self.right_n -= 1
        else:
            res = -1
        return res


if __name__ == "__main__":
    ts = TwoStacks(5)
    ts.push1(5)
    ts.push2(10)
    ts.push2(15)
    ts.push1(11)
    ts.push2(7)

    print("Popped element from stack1 is " + str(ts.pop1()))
    ts.push2(40)
    print("Popped element from stack2 is " + str(ts.pop2()))
