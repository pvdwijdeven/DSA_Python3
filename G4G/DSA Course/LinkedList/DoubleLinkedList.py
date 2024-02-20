class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    @property
    def var_next(self):
        assert self.next is not None
        return self.next

    @property
    def var_prev(self):
        assert self.prev is not None
        return self.prev

    def print(self):
        print(self.data, end=":")
        print(" prev: ", end="")
        if not self.prev:
            print("NONE", end=",")
        else:
            print(self.prev.data, end=",")
        print(" next: ", end="")
        if not self.next:
            print("NONE")
        else:
            print(self.next.data)


class DoubleLinkedList:
    def __init__(self, arr=None):
        if not arr:
            self.head = Node(None)
        else:
            if isinstance(arr, list):
                self.listFromArr(arr)
            else:
                self.listFromString(arr)

    def listFromString(self, slist):
        llist = [int(x) for x in slist.split("<->")]
        return self.listFromArr(llist)

    def listFromArr(self, arr):
        if arr == []:
            self.head = Node(None)
            return self.head
        prevNode = Node(None)
        prevprev = None
        head = prevNode
        for x in arr:
            cur = Node(x)
            prevNode.next = cur
            prevNode.prev = prevprev
            prevprev = prevNode
            prevNode = cur
        cur.prev = prevprev
        if head.next:
            head.next.prev = None
        self.head = head.next
        return head.next

    def printList(self):
        # code here
        res = []
        cur = self.head
        if not cur:
            return []
        while cur.next:
            res.append(cur.data)
            cur = cur.next
        res.append(cur.data)
        return res

    def insertInhead(self, data):
        # code here
        temp = Node(data)
        temp.prev = None
        temp.next = self.head
        if self.head:
            self.head.prev = temp
        self.head = temp
        return temp

    def insertInTail(self, data):
        # code here
        temp = Node(data)
        if not self.head:
            return temp
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = temp
        temp.prev = cur
        return self.head

    def insertAtPosition(self, p, data):
        temp = Node(data)
        curr = self.head
        for i in range(0, p):
            if curr:
                curr = curr.next
            if not curr:
                return self.head
        if curr:
            temp.next = curr.next
            curr.next = temp
            temp.prev = curr
            if temp.next != None:
                temp.next.prev = temp
        return self.head

    def delHead(self):
        if not self.head:
            return None
        if not self.head.next:
            return None
        else:
            self.head = self.head.next
            self.head.prev = None
            return self.head

    def deleteNode(self, x):
        # Code here
        cur = self.head
        for pos in range(1, x):
            if cur:
                cur = cur.next
        if cur:
            if cur.prev:
                cur.prev.next = cur.next
            if cur.next:
                cur.next.prev = cur.prev
        return self.head

    def deleteTail(self):
        # code here
        if not self.head:
            return None
        if not self.head.next:
            return None
        cur = self.head
        prev = Node(None)
        while cur.next:
            prev = cur
            cur = cur.next
        prev.next = None
        return self.head

    def findMiddle(self):
        # code here
        if self.head:
            curl = self.head
            curr = self.head.prev
        if curr and curl:
            while curl != curr:
                if curr and curl:
                    curl = curl.next
                    curr = curr.prev
            return curr.data

    def printall(self):
        cur = self.head
        if cur:
            while cur.next:
                cur.print()
                cur = cur.next
            cur.print()
        return

    def reverseDLL(self):
        # return head after reversing
        if not self.head:
            return None
        cur = self.head
        while cur.next:
            cur.next, cur.prev = cur.prev, cur.next
            cur = cur.prev
        cur.next, cur.prev = cur.prev, cur.next
        self.head = cur
        return cur

    def sortedInsert(self, x):
        # code here
        cur = self.head
        if not cur:
            return None
        if cur.data >= x:
            temp = Node(x)
            cur.prev = temp
            temp.next = cur
            return temp
        while cur.next:
            if cur.data >= x:
                temp = Node(x)
                if cur.prev:
                    cur.prev.next = temp
                temp.prev = cur.prev
                temp.next = cur
                cur.prev = temp
                return self.head
            else:
                cur = cur.next
        temp = Node(x)
        cur.next = temp
        temp.prev = cur
        return self.head


L1 = DoubleLinkedList("1<->2<->3<->4<->5")
L1.printall()
print(L1.printList())

L1.insertInhead(20)
L1.insertInTail(44)
L1.insertAtPosition(2, 50)
print(L1.printList())

L2 = DoubleLinkedList("2<->4<->5")
L2.insertAtPosition(2, 6)
print(L2.printList())
L2.printall()
L2.reverseDLL()
# L2.printall()
print(L2.printList())

L3 = DoubleLinkedList([1, 9, 16, 25, 78])
L3.sortedInsert(0)
print(L3.printList())
