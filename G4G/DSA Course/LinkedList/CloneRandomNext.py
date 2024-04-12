class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None
        self.arb = None


# Function to clone a linked list with next and random pointer.
def clone_list_random_next(head) -> Node:
    d = {}
    d[None] = None
    curr = head
    while curr != None:
        d[curr] = Node(curr.data)
        curr = curr.next
    curr = head
    while curr != None:
        d[curr].next = d[curr.next]
        d[curr].arb = d[curr.arb]
        curr = curr.next
    return d[head]
