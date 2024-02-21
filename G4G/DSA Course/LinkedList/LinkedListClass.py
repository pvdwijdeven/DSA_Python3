# Linked list class


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, arr=None):
        if not arr:
            self.head = Node(None)
            self.tail = Node(None)
        else:
            if isinstance(arr, list):
                self.listFromArr(arr)
            else:
                self.listFromString(arr)

    def listFromString(self, slist):
        # create linked list from string with "->"
        llist = [int(x) for x in slist.split("->")]
        return self.listFromArr(llist)

    def listFromArr(self, arr):
        # create linked list from array
        prev = Node(None)
        head = prev
        for x in arr:
            cur = Node(x)
            prev.next = cur
            prev = cur
        self.tail = cur
        self.head = head.next
        return head.next

    def printList(self):
        # return linked list as array
        array = []
        if not self.head:
            return array
        curr = self.head
        while True:
            array.append(curr.data)
            if not curr.next:
                break
            curr = curr.next
        print(self.head.data, self.tail.data)
        return array

    def getCount(self):
        # return number of elements in linked list
        if not self.head:
            return 0
        cur = self.head
        count = 1
        while cur.next:
            count += 1
            cur = cur.next
        return count

    def sumOfElements(self):
        # return sum of elements in linked list
        if not self.head:
            return 0
        cur = self.head
        total = cur.data
        while cur.next:
            cur = cur.next
            total += cur.data
        return total

    def searchLinkedList(self, x):
        # search for value in linked list and return first found
        if not self.head:
            return -1
        cur = self.head
        index = 0
        while cur.next:
            if cur.data == x:
                return index
            index += 1
            cur = cur.next
        return index

    def insertAtBegining(self, x):
        # Insert value at beginning at linked list
        cur = Node(x)
        cur.next = self.head
        self.head = cur
        return cur

    def insertAtEnd(self, x):
        # Insert a node at the end of the linked list.
        if not self.head:
            return Node(x)
        cur = self.head
        while cur.next:
            cur = cur.next
        newNode = Node(x)
        cur.next = newNode
        self.tail = newNode
        return self.head

    def insertAtPosition(self, pos, data):
        # Insert a node at the given posiition
        temp = Node(data)
        if pos == 0:
            temp.next = self.head
            self.head = temp
            return temp
        curr = self.head
        for _i in range(0, pos - 1):
            if curr:
                curr = curr.next
                if not curr:
                    return self.head
        if curr:
            temp.next = curr.next
            curr.next = temp
        if not temp.next:
            self.tail = temp
        return self.head

    def deleteHead(self):
        # Delete head of linked list
        if not self.head:
            return self.head
        else:
            temp = self.head.next
            self.head.next = None
            self.head = temp
            return temp

    def deleteTail(self):
        # Delete tail of linked list
        cur = self.head
        if not cur or not cur.next:
            return None
        while True:
            if not cur or not cur.next or not cur.next.next:
                break
            prev = cur
            cur = cur.next
        prev.next = None
        self.tail = prev
        return self.head

    def deleteNode(self, ptr):
        # delete node as indicated by given pointer ptr
        # does not work if prt == tail!!!
        if self.tail == ptr:
            print("Error: tail cannot be removed!")
            return
        if self.head == ptr:
            self.head = ptr.next
        temp = ptr.next
        ptr.data = temp.data
        ptr.next = temp.next

    def deleteAtPosition(self, pos):
        # delete node at given position
        curr = self.head
        if not curr:
            return None
        c = 0
        if pos == 0:
            self.head = curr.next
            return curr.next
        while curr:
            if c + 1 == pos and curr.next:
                temp = curr.next.next
                curr.next = temp
            elif c + 1 == pos:
                self.tail = curr
                return self.head
            curr = curr.next
            c += 1
        return self.head

    def insertInSorted(self, data):
        # Insert value in sorted list

        temp = Node(data)
        if not self.head:
            return temp
        if self.head.data <= self.tail.data:
            if data < self.head.data:
                temp.next = self.head
                self.head = temp
                return temp
            else:
                curr = self.head
                while curr.next and curr.next.data < data:
                    curr = curr.next
                temp.next = curr.next
                curr.next = temp
                if self.tail == curr:
                    self.tail = temp
                return self.head
        else:
            if data > self.head.data:
                temp.next = self.head
                self.head = temp
                return temp
            else:
                curr = self.head
                while curr.next and curr.next.data > data:
                    curr = curr.next
                temp.next = curr.next
                curr.next = temp
                if self.tail == curr:
                    self.tail = temp
                return self.head

    def insertInMid(self, node):
        # Insert node in middle of linked list
        node = Node(node)
        if not self.head:
            return node
        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            if slow:
                slow = slow.next
            fast = fast.next.next
        if slow:
            node.next = slow.next
            slow.next = node
        return self.head

    def isSorted(self):
        # Check if linked list is sorted
        curN = self.head
        if not curN:
            return True
        curD = curN.data
        direction = "equal"
        while curN.next:
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
        # Get value of nth node from end of linked list (0-based)
        n = n + 1
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
                if cur2:
                    cur2 = cur2.next
        if n:
            return -1
        if cur2:
            return cur2.data

    def joinTheLists(self, head2):
        # Join linked list head2 with current one
        if not self.head:
            return head2
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = head2.head
        self.tail = head2.tail
        return self.head

    def removeDuplicates(self):
        # Remove all duplicates in linked list
        if not self.head:
            return None
        cur = self.head
        while cur.next:
            if cur.data == cur.next.data:
                cur.next = cur.next.next
            else:
                cur = cur.next
        if cur != self.tail:
            self.tail = cur
        return self.head

    def reverseList(self):
        # Reverse the list
        stack = []
        if not self.head:
            return None
        cur = self.head
        self.tail = cur
        while cur.next:
            stack.append(cur)
            cur = cur.next
        self.head = cur
        while stack != []:
            cur.next = stack.pop()
            cur = cur.next
        cur.next = None
        self.tail = cur
        return self.head

    def maximum(self):
        # Get maximum number of linked list
        mx = 0
        cur = self.head
        if not cur:
            return 0
        while cur.next:
            if cur.data > mx:
                mx = cur.data
            cur = cur.next
        if cur.data > mx:
            mx = cur.data
        return mx

    def minimum(self):
        # get minimum number of linked list
        mn = 10**199
        cur = self.head
        if not cur:
            return 0
        while cur.next:
            if cur.data < mn:
                mn = cur.data
            cur = cur.next
        if cur.data < mn:
            mn = cur.data
        return mn

    def areIdentical(self, head2):
        # Check if list head2 is identical to current linked list
        cur1 = self.head
        cur2 = head2.head
        if not cur1:
            return not cur2
        if not cur2:
            return not cur1
        while cur1.next and cur2.next:
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
L1.insertAtPosition(3, 99)
print(L1.printList())
L1.deleteHead()
L1.deleteTail()
print(L1.printList())
print(L1.isSorted())
if L1.head and L1.head.next and L1.head.next.next:
    L1.deleteNode(L1.head.next.next)
print(L1.printList())

L1.deleteAtPosition(2)
print(L1.printList())


l2 = "1->1->1->3->3->3->4->4"
L2 = LinkedList(l2)
print(L2.printList())
L2.reverseList()
print(L2.printList())
L2.removeDuplicates()
print(L2.printList())
print(L2.isSorted())
L2.insertInSorted(2)
print(L2.printList())
L2.insertInMid(99)
print(L2.printList())
L2.insertInMid(-99)
print(L2.printList())
print(L2.getNthFromLast(2))

L3 = LinkedList([1, 2, 3, 4, 6, 7, 8, 9])
print(L3.printList())
L3.insertInSorted(5)
print(L3.printList())

L4 = LinkedList([1, 2, 3, 4, 5])
L5 = LinkedList([6, 7, 8, 9])
L4.joinTheLists(L5)
print(L4.printList())
print(L4.areIdentical(L5))
print(L4.areIdentical(L3))
print(L2.maximum())
print(L2.minimum())
