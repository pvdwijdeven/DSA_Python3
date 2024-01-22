class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def listFromString(slist):
    llist = [int(x) for x in slist.split("<->")]
    prev = Node(None)
    prevprev = None
    head = prev
    cur = Node(None)
    for x in llist:
        cur = Node(x)
        prev.next = cur  # type: ignore
        prev.prev = prevprev  # type: ignore
        prevprev = prev
        prev = cur
    cur.next = head.next
    head.next.prev = cur  # type: ignore
    return head.next


def displayList(head):
    # code here
    res = []
    cur = head
    while cur.next != head:
        res.append(cur.data)
        cur = cur.next
    res.append(cur.data)
    return res


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


L1 = listFromString("1<->2<->3<->4<->5")
print(displayList(L1))
