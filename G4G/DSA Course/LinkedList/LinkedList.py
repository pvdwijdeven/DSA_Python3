# Linked list class
class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)

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

    def printList(self, head):
        array = []
        curr = head
        while True:
            array.append(curr.data)
            if curr.next == None:
                break
            curr = curr.next
        return array

    def getCount(self, head):
        cur = head
        count = 1
        while cur.next != None:
            count += 1
            cur = cur.next
        return count

    def sumOfElements(self, head):
        cur = head
        total = cur.data
        while cur.next != None:
            cur = cur.next
            total += cur.data
        return total

    def searchLinkedList(self, head, x):
        cur = head
        index = 0
        while cur.next != None:
            if cur.data == x:
                return index
            index += 1
            cur = cur.next
        return index

    def insertAtBegining(self, head, x):
        # code here
        cur = Node(x)
        cur.next = head
        return cur

    # Function to insert a node at the end of the linked list.
    def insertAtEnd(self, head, x):
        # code here
        if head == None:
            return Node(x)
        cur = head
        while cur.next != None:
            cur = cur.next
        newNode = Node(x)
        cur.next = newNode
        return head

    def insertAtPosition(self, head, pos, data):
        temp = Node(data)
        if pos == 0:
            temp.next = head
            return temp
        curr = head
        for i in range(1, pos):
            curr = curr.next
            if curr == None:
                return head
        temp.next = curr.next
        curr.next = temp
        return head

    def deleteHead(self, head):
        # code here
        if head == None:
            return head
        else:
            temp = head.next
            head.next = None
            return temp

    def deleteTail(self, head):
        # code here
        if head == None or head.next == None:
            return None
        cur = head
        while cur.next.next != None:
            cur = cur.next
        cur.next = None
        return head

    def deleteNode(self, ptr):
        temp = ptr.next
        ptr.data = temp.data
        ptr.next = temp.next

    def deleteAtPosition(self, head, pos):
        curr = head
        c = 1
        if pos == 1:
            return head.next

        while curr != None:
            if c + 1 == pos:
                temp = curr.next.next
                curr.next = temp
            curr = curr.next
            c += 1
        return head


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


l1 = "1->2->3->4->5"
l2 = "2->4->6->7->5->1->0"

L1 = LinkedList()
L1.listFromString(l1)
print(L1.printList(L1.head))
print(L1.getCount(L1.head))
print(L1.sumOfElements(L1.head))
print(L1.searchLinkedList(L1.head, 3))

L1.head = L1.insertAtBegining(L1.head, 9)
L1.head = L1.insertAtEnd(L1.head, 8)

L1.head = L1.insertAtPosition(L1.head, 7, 3)

L1.head = L1.deleteHead(L1.head)

print(L1.printList(L1.head))
