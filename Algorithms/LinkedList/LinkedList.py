# Linked list class


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)


def listFromString(slist):
    llist = [int(x) for x in slist.split("->")]
    prev = Node(None)
    head = prev
    for x in llist:
        cur = Node(x)
        prev.next = cur  # type: ignore
        prev = cur
    return head.next


def printList(head):
    array = []
    curr = head
    while True:
        array.append(curr.data)
        if curr.next == None:
            break
        curr = curr.next
    return array


def getCount(head):
    cur = head
    count = 1
    while cur.next:
        count += 1
        cur = cur.next
    return count


def sumOfElements(head):
    cur = head
    total = cur.data
    while cur.next != None:
        cur = cur.next
        total += cur.data
    return total


def searchLinkedList(head, x):
    cur = head
    index = 0
    while cur.next != None:
        if cur.data == x:
            return index
        index += 1
        cur = cur.next
    return index


def insertAtBegining(head, x):
    # code here
    cur = Node(x)
    cur.next = head
    return cur


# Function to insert a node at the end of the linked list.
def insertAtEnd(head, x):
    # code here
    if head == None:
        return Node(x)
    cur = head
    while cur.next != None:
        cur = cur.next
    newNode = Node(x)
    cur.next = newNode
    return head


def insertAtPosition(head, pos, data):
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


def deleteHead(head):
    # code here
    if head == None:
        return head
    else:
        temp = head.next
        head.next = None
        return temp


def deleteTail(head):
    # code here
    if head == None or head.next == None:
        return None
    cur = head
    while cur.next.next != None:
        cur = cur.next
    cur.next = None
    return head


def deleteNode(ptr):
    temp = ptr.next
    ptr.data = temp.data
    ptr.next = temp.next


def deleteAtPosition(head, pos):
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


def insertInSorted(head, data):
    temp = Node(data)

    if head == None:
        return temp
    elif data < head.data:
        temp.next = head
        return temp
    else:
        curr = head

        while curr.next != None and curr.next.data < data:
            curr = curr.next

        temp.next = curr.next
        curr.next = temp
        return head


def insertInMid(head, node):
    if head == None:
        return node
    slow = head
    fast = head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    node.next = slow.next
    slow.next = node
    return head


def isSorted(head):
    # code here
    curN = head
    curD = head.data
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


def getNthFromLast(head, n):
    # code here
    if n == 0:
        return -1

    if not head:
        return -1

    cur1 = head
    cur2 = head

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


def joinTheLists(head1, head2):
    # code here
    if head1 == None:
        return head2
    cur = head1
    while cur.next != None:
        cur = cur.next
    cur.next = head2
    return head1


def removeDuplicates(head):
    # code here
    if head == None:
        return None
    cur = head
    while cur.next != None:
        if cur.data == cur.next.data:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head


def reverseList(head):
    # Code here
    stack = []
    if head == None:
        return None
    cur = head
    while cur.next != None:
        stack.append(cur)
        cur = cur.next
    head = cur
    while stack != []:
        cur.next = stack.pop()
        cur = cur.next
    cur.next = None
    return head


def maximum(head):
    # code here
    mx = 0
    cur = head
    while cur.next != None:
        if cur.data > mx:
            mx = cur.data
        cur = cur.next
    if cur.data > mx:
        mx = cur.data
    return mx


def minimum(head):
    # code here
    mn = 10**199
    cur = head
    while cur.next != None:
        if cur.data < mn:
            mn = cur.data
        cur = cur.next
    if cur.data < mn:
        mn = cur.data
    return mn


def areIdentical(head1, head2):
    # Code here
    cur1 = head1
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
l2 = "2->4->6->7->5->1->0"

L1 = listFromString(l1)
print(printList(L1))
print(getCount(L1))
print(sumOfElements(L1))
print(searchLinkedList(L1, 3))

L1 = insertAtBegining(L1, 9)
L1 = insertAtEnd(L1, 8)

L1 = insertAtPosition(L1, 7, 3)

L1 = deleteHead(L1)

print(printList(L1))

L2 = listFromString("1->1->1->3->3->3->4->4")
# L2.removeDuplicates(L2.head)
L2 = reverseList(L2)
print(printList(L2))
