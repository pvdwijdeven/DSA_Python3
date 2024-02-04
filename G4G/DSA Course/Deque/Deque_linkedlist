class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def listFromString(self, slist):
        llist = [int(x) for x in slist.split("->")]
        prev = Node(None)
        head = prev
        cur = None
        for x in llist:
            cur = Node(x)
            prev.next = cur  # type: ignore
            prev = cur
        self.front = head.next
        self.rear = cur
        return head.next

    def printList(self):
        array = []
        curr = self.front
        while True:
            array.append(curr.data)  # type: ignore
            if curr.next == None:  # type: ignore
                break
            curr = curr.next  # type: ignore
        return array

    def insertFront(self, data):
        # return: (front,rear)
        # code here
        temp = Node(data)
        if self.front == None:
            self.front = temp
            self.rear = temp
            return
        temp.next = self.front  # type: ignore
        self.front.prev = temp  # type: ignore
        self.front = temp
        return

    def insertRear(self, data):
        # return: (front,rear)
        # code here
        temp = Node(data)
        if self.rear == None:
            self.rear = temp
            self.front = temp
            return
        temp.prev = self.rear  # type: ignore
        self.rear.next = temp  # type: ignore
        self.rear = temp
        return

    def delFront(self):
        # return: (front, rear)
        # code here
        if self.front == None:
            return
        self.front = self.front.next
        if self.front == None:
            return
        self.front.prev = None
        return

    def delRear(self):
        # return: (front, rear)
        # code here
        if self.rear == None:
            return
        self.rear = self.rear.prev
        if self.rear == None:
            return
        self.rear.next = None
        return


deq = Deque()
deq.listFromString("1->2->3->4")
print(deq.printList())


deq.insertFront(10)
print(deq.printList())
deq.insertRear(20)
print(deq.printList())
deq.delRear()
print(deq.printList())
deq.delFront()
print(deq.printList())
