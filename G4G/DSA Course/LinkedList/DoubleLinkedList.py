class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def print(self):
        print(self.data, end=":")
        print(" prev: ", end="")
        if self.prev == None:
            print("None", end=",")
        else:
            print(self.prev.data, end=",")
        print(" next: ", end="")
        if self.next == None:
            print("None")
        else:
            print(self.next.data)


def listFromString(slist):
    llist = [int(x) for x in slist.split("<->")]
    prev = Node(None)
    prevprev = None
    head = prev
    for x in llist:
        cur = Node(x)
        prev.next = cur  # type: ignore
        prev.prev = prevprev
        prevprev = prev
        prev = cur
    cur.prev = prevprev
    return head.next


def displayList(head):
    # code here
    res = []
    cur = head
    while cur.next != None:
        res.append(cur.data)
        cur = cur.next
    res.append(cur.data)
    return res


def insertInhead(head, data):
    # code here
    temp = Node(data)
    temp.prev = None
    temp.next = head
    head.prev = temp
    return temp


def insertInTail(head, data):
    # code here
    temp = Node(data)
    if head == None:
        return temp
    cur = head
    while cur.next != None:
        cur = cur.next
    cur.next = temp
    temp.prev = cur
    return head


def insertAtPosition(head, p, data):
    temp = Node(data)
    # if p == 0:
    #     temp.prev = head
    #     temp.next = head.next
    #     head.next = temp
    #     return temp
    curr = head
    for i in range(0, p):
        curr = curr.next
        if curr == None:
            return head
    temp.next = curr.next
    curr.next = temp
    temp.prev = curr
    if temp.next != None:
        temp.next.prev = temp
    return head


def delHead(head):
    if head == None:
        return None
    if head.next == None:
        return None
    else:
        head = head.next
        head.prev = None
        return head


def deleteNode(head, x):
    # Code here
    cur = head
    for pos in range(1, x):
        cur = cur.next
    if cur.prev != None:
        cur.prev.next = cur.next
    if cur.next != None:
        cur.next.prev = cur.prev
    return head


def deleteTail(head):
    # code here
    if head == None:
        return None
    if head.next == None:
        return None
    cur = head
    while cur.next != None:
        prev = cur
        cur = cur.next
    prev.next = None
    return head


def findMiddle(head):
    # code here
    curl = head
    curr = head.prev
    while curl != curr:
        curl = curl.next
        curr = curr.prev
    return curr.data


def printall(head):
    cur = head
    while cur.next != None:
        cur.print()
        cur = cur.next
    cur.print()
    return


L1 = listFromString("1<->2<->3<->4<->5")
L1 = insertInhead(L1, 20)
L1 = insertInTail(L1, 44)
L1 = insertAtPosition(L1, 2, 50)
print(displayList(L1))


L2 = listFromString("2<->4<->5")
L2 = insertAtPosition(L2, 2, 6)
print(displayList(L2))
printall(L2)
