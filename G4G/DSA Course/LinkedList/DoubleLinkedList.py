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
        prevNode = Node(None)
        prevprev = None
        head = prevNode
        cur = Node(None)
        for x in arr:
            cur = Node(x)
            prevNode.next = cur
            prevNode.prev = prevprev
            prevprev = prevNode
            prevNode = cur
        cur.prev = prevprev
        self.head = head.next
        return head.next

    def printList(self):
        # code here
        res = []
        cur = self.head
        if not cur:
            return []
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
    prev = Node(None)
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


def reverseDLL(head):
    # return head after reversing
    if head == None:
        return None
    cur = head
    while cur.next != None:
        cur.next, cur.prev = cur.prev, cur.next
        cur = cur.prev
    cur.next, cur.prev = cur.prev, cur.next
    return cur


def sortedInsert(head, x):
    # code here
    cur = head
    if cur.data >= x:
        temp = Node(x)
        cur.prev = temp
        temp.next = cur
        return temp
    while cur.next != None:
        if cur.data >= x:
            temp = Node(x)
            if cur.prev != None:
                cur.prev.next = temp
            temp.prev = cur.prev
            temp.next = cur
            cur.prev = temp
            return head
        else:
            cur = cur.next
    temp = Node(x)
    cur.next = temp
    temp.prev = cur
    return head


L1 = DoubleLinkedList("1<->2<->3<->4<->5")
print(L1.printList())

# L1 = listFromString("1<->2<->3<->4<->5")
# L1 = insertInhead(L1, 20)
# L1 = insertInTail(L1, 44)
# L1 = insertAtPosition(L1, 2, 50)
# print(displayList(L1))


# L2 = listFromString("2<->4<->5")
# L2 = insertAtPosition(L2, 2, 6)
# print(displayList(L2))
# printall(L2)
# print(displayList(reverseDLL(L1)))

# L3 = listFromString("1")  # <->9<->16<->25<->78")
# L3 = sortedInsert(L3, 0)
# printall(L3)
