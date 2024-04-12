class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


def mergeKLists(arr, K):
    res = []
    for i in range(K):
        while arr[i]:
            res.append(arr[i].data)
            arr[i] = arr[i].next
    res.sort()
    head = Node(res[0])
    curr = head
    for i in res[1:]:
        curr.next = Node(i)
        curr = curr.next
    return head
