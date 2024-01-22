class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def listFromString(slist):
    llist = [int(x) for x in slist.split("->")]
    prev = Node(None)
    head = prev
    for x in llist:
        cur = Node(x)
        prev.next = cur  # type: ignore
        prev = cur
    prev.next = head.next
    return head.next


def printList(head):
    array = []
    curr = head
    while curr.next != head:
        array.append(curr.data)
        curr = curr.next
    array.append(curr.data)
    return array


def getLength(head):
    # code here
    count = 0
    curr = head
    while curr.next != head:
        count += 1
        curr = curr.next
    count += 1
    return count


def insertInHead(head, x):
    temp = Node(x)
    # code here
    if head == None:
        temp.next = temp  # type: ignore
        return temp
    temp = Node(x)
    temp.next = head.next
    head.next = temp
    temp.data, head.data = head.data, temp.data
    return head


def insertInTail(head, x):
    temp = Node(x)
    # code here
    if head == None:
        temp.next = temp  # type: ignore
        return temp
    temp = Node(x)
    temp.next = head.next
    head.next = temp
    temp.data, head.data = head.data, temp.data
    return head.next


def deleteTail(head):
    curr = head
    prev = Node(None)
    if head == None or curr.next == head:
        return None
    while curr.next != head:
        prev = curr
        curr = curr.next
    prev.next = head
    return head


def isCircular(head):
    # Code here
    curr = head
    if head == None:
        return 0
    while curr.next != head and curr.next != None:
        curr = curr.next
    if curr.next == None:
        return 0
    return 1


def deleteHead(head):
    # code here
    curr = head
    if head == None or curr.next == head:
        return None
    head.data = head.next.data
    head.next = head.next.next
    return head


def delKth(head, k):
    if head == None:
        return head
    elif k == 1:
        return deleteHead(head)
    else:
        curr = head
        for i in range(k - 2):
            curr = curr.next
        curr.next = curr.next.next
        return head


def insertAtPosition(head, pos, data):
    # code here
    temp = Node(data)
    c_pos = 1
    if head == None:
        if pos == 1:
            temp.next = temp  # type: ignore
            return temp
        else:
            return None
    cur = head
    while pos > c_pos and cur.next != head:
        cur = cur.next
        c_pos += 1
    if pos == c_pos:
        temp.next = cur.next
        cur.next = temp
    return head


L1 = listFromString("1->2->3->4->5")
print(printList(L1))
print(getLength(L1))
L1 = insertInTail(L1, 10)
print(printList(L1))
L1 = deleteTail(L1)
print(printList(L1))
L1 = insertAtPosition(L1, 3, 20)
print(printList(L1))
