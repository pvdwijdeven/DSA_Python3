# Linked list class


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, arr=None):
        if not arr:
            self.head = Node(None)
            self.tail = Node(None)
        else:
            self.listFromString(arr)

    def listFromString(self, slist):
        llist = [int(x) for x in slist.split("->")]
        prev = Node(None)
        head = prev
        for x in llist:
            cur = Node(x)
            prev.next = cur  # type: ignore
            prev = cur
        self.head = head.next
        return head.next

    def printList(self):
        array = []
        if not self.head:
            return array
        curr = self.head
        while True:
            array.append(curr.data)
            if curr.next == None:
                break
            curr = curr.next
        return array

    def getCount(self):
        if not self.head:
            return 0
        cur = self.head
        count = 1
        while cur.next:
            count += 1
            cur = cur.next
        return count

    def sumOfElements(self):
        if not self.head:
            return 0
        cur = self.head
        total = cur.data
        while cur.next != None:
            cur = cur.next
            total += cur.data
        return total

    def searchLinkedList(self, x):
        if not self.head:
            return -1
        cur = self.head
        index = 0
        while cur.next != None:
            if cur.data == x:
                return index
            index += 1
            cur = cur.next
        return index

    def insertAtBegining(self, x):
        # code here
        cur = Node(x)
        cur.next = self.head
        self.head = cur
        return cur

    # Function to insert a node at the end of the linked list.
    def insertAtEnd(self, x):
        # code here
        if self.head == None:
            return Node(x)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        newNode = Node(x)
        cur.next = newNode
        return self.head

    def insertAtPosition(self, pos, data):
        temp = Node(data)
        if pos == 0:
            temp.next = self.head
            return temp
        curr = self.head
        for i in range(1, pos):
            curr = curr.next
            if curr == None:
                return self.head
        temp.next = curr.next
        curr.next = temp
        return self.head

    def deleteHead(self):
        # code here
        if self.head == None:
            return self.head
        else:
            temp = self.head.next
            self.head.next = None
            self.head = temp
            return temp

    def deleteTail(self):
        cur = self.head
        if not cur or not cur.next:
            return None
        while cur.next.next:
            cur = cur.next
        cur.next = None
        return self.head

    def deleteNode(self, ptr):
        temp = ptr.next
        ptr.data = temp.data
        ptr.next = temp.next

    def deleteAtPosition(self, pos):
        curr = self.head
        c = 1
        if pos == 1:
            return self.head.next

        while curr:
            if c + 1 == pos:
                temp = curr.next.next
                curr.next = temp
            curr = curr.next
            c += 1
        return self.head

    def insertInSorted(self, data):
        temp = Node(data)

        if not self.head:
            return temp
        elif data < self.head.data:
            temp.next = self.head
            self.head = temp
            return temp
        else:
            curr = self.head

            while curr.next != None and curr.next.data < data:
                curr = curr.next

            temp.next = curr.next
            curr.next = temp
            return self.head

    def insertInMid(self, node):
        if self.head == None:
            return node
        slow = self.head
        fast = self.head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        node.next = slow.next
        slow.next = node
        return self.head

    def isSorted(self):
        # code here
        curN = self.head
        curD = self.head.data
        direction = "equal"
        while curN.next != None:
            curN = curN.next
            if curD > curN.data:
                if direction == "equal" or direction == "decreasing":
                    direction = "decreasing"
                else:
                    return False
            if curD < curN.data:
                if direction == "equal" or direction == "increasing":
                    direction = "increasing"
                else:
                    return False
            curD = curN.data
        return True

    def getNthFromLast(self, n):
        # code here
        if n == 0:
            return -1

        if not self.head:
            return -1

        cur1 = self.head
        cur2 = self.head

        while cur1:
            if n:
                cur1 = cur1.next
                n -= 1
            else:
                cur1 = cur1.next
                cur2 = cur2.next
        if n:
            return -1

        return cur2.data

    def joinTheLists(self, head2):
        # code here
        if self.head == None:
            return head2
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = head2
        return self.head

    def removeDuplicates(self):
        # code here
        if not self.head:
            return None
        cur = self.head
        while cur.next != None:
            if cur.data == cur.next.data:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return self.head

    def reverseList(self):
        # Code here
        stack = []
        if not self.head:
            return None
        cur = self.head
        while cur.next != None:
            stack.append(cur)
            cur = cur.next
        head = cur
        while stack != []:
            cur.next = stack.pop()
            cur = cur.next
        cur.next = None
        return self.head

    def maximum(self):
        # code here
        mx = 0
        cur = self.head
        while cur.next != None:
            if cur.data > mx:
                mx = cur.data
            cur = cur.next
        if cur.data > mx:
            mx = cur.data
        return mx

    def minimum(self):
        # code here
        mn = 10**199
        cur = self.head
        while cur.next != None:
            if cur.data < mn:
                mn = cur.data
            cur = cur.next
        if cur.data < mn:
            mn = cur.data
        return mn

    def areIdentical(self, head2):
        # Code here
        cur1 = self.head
        cur2 = head2
        while cur1.next != None and cur2.next != None:
            if cur1.data != cur2.data:
                return False
            cur1 = cur1.next
            cur2 = cur2.next
        if cur1.next != cur2.next:
            return False
        if cur1.data != cur2.data:
            return False
        return True


l1 = "1->2->3->4->5"


L1 = LinkedList()
L1.listFromString(l1)
print(L1.printList())
print(L1.getCount())
print(L1.sumOfElements())
print(L1.searchLinkedList(3))

L1.insertAtBegining(9)
L1.insertAtEnd(8)

L1.insertAtPosition(7, 3)

L1.deleteHead()

print(L1.printList())
l2 = "1->1->1->3->3->3->4->4"
L2 = LinkedList(l2)
# L2.removeDuplicates(L2.head)
L2.reverseList()
print(L2.printList())
