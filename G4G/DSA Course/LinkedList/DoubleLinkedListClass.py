class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    @property
    def var_next(self):
        assert self.next is not None
        return self.next

    @property
    def var_prev(self):
        assert self.prev is not None
        return self.prev

    def print(self):
        print(self.data, end=":")
        print(" prev: ", end="")
        if not self.prev:
            print("NONE", end=",")
        else:
            print(self.prev.data, end=",")
        print(" next: ", end="")
        if not self.next:
            print("NONE")
        else:
            print(self.next.data)


class DoubleLinkedList:
    def __init__(self, arr=None):
        if not arr:
            self.head = Node(None)
        else:
            if isinstance(arr, list):
                self.list_from_arr(arr)
            else:
                self.list_from_string(arr)

    def list_from_string(self, slist):
        llist = [int(x) for x in slist.split("<->")]
        return self.list_from_arr(llist)

    def list_from_arr(self, arr):
        if arr == []:
            self.head = Node(None)
            return self.head
        prev_node = Node(None)
        prev_prev = None
        head = prev_node
        for x in arr:
            cur = Node(x)
            prev_node.next = cur
            prev_node.prev = prev_prev
            prev_prev = prev_node
            prev_node = cur
        cur.prev = prev_prev
        if head.next:
            head.next.prev = None
        self.head = head.next
        return head.next

    def print_list(self):
        # code here
        res = []
        cur = self.head
        if not cur:
            return []
        while cur.next:
            res.append(cur.data)
            cur = cur.next
        res.append(cur.data)
        return res

    def insert_in_head(self, data):
        # code here
        temp = Node(data)
        temp.prev = None
        temp.next = self.head
        if self.head:
            self.head.prev = temp
        self.head = temp
        return temp

    def insert_in_tail(self, data):
        # code here
        temp = Node(data)
        if not self.head:
            return temp
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = temp
        temp.prev = cur
        return self.head

    def insert_at_position(self, p, data):
        temp = Node(data)
        cur = self.head
        for i in range(0, p):
            if cur:
                cur = cur.next
            if not cur:
                return self.head
        if cur:
            temp.next = cur.next
            cur.next = temp
            temp.prev = cur
            if temp.next != None:
                temp.next.prev = temp
        return self.head

    def delete_head(self):
        if not self.head:
            return None
        if not self.head.next:
            return None
        else:
            self.head = self.head.next
            self.head.prev = None
            return self.head

    def delete_node(self, x):
        # Code here
        cur = self.head
        for pos in range(1, x):
            if cur:
                cur = cur.next
        if cur:
            if cur.prev:
                cur.prev.next = cur.next
            if cur.next:
                cur.next.prev = cur.prev
        return self.head

    def delete_tail(self):
        # code here
        if not self.head:
            return None
        if not self.head.next:
            return None
        cur = self.head
        prev = Node(None)
        while cur.next:
            prev = cur
            cur = cur.next
        prev.next = None
        return self.head

    def find_middle(self):
        # code here
        if self.head:
            curl = self.head
            cur = self.head.prev
        if cur and curl:
            while curl != cur:
                if cur and curl:
                    curl = curl.next
                    cur = cur.prev
            return cur.data

    def print_all(self):
        cur = self.head
        if cur:
            while cur.next:
                cur.print()
                cur = cur.next
            cur.print()
        return

    def reverse_list(self):
        # return head after reversing
        if not self.head:
            return None
        cur = self.head
        while cur.next:
            cur.next, cur.prev = cur.prev, cur.next
            cur = cur.prev
        cur.next, cur.prev = cur.prev, cur.next
        self.head = cur
        return cur

    def sorted_insert(self, x):
        # code here
        cur = self.head
        if not cur:
            return None
        if cur.data >= x:
            temp = Node(x)
            cur.prev = temp
            temp.next = cur
            return temp
        while cur.next:
            if cur.data >= x:
                temp = Node(x)
                if cur.prev:
                    cur.prev.next = temp
                temp.prev = cur.prev
                temp.next = cur
                cur.prev = temp
                return self.head
            else:
                cur = cur.next
        temp = Node(x)
        cur.next = temp
        temp.prev = cur
        return self.head


if __name__ == "__main__":
    L1 = DoubleLinkedList("1<->2<->3<->4<->5")
    L1.print_all()
    print(L1.print_list())

    L1.insert_in_head(20)
    L1.insert_in_tail(44)
    L1.insert_at_position(2, 50)
    print(L1.print_list())

    L2 = DoubleLinkedList("2<->4<->5")
    L2.insert_at_position(2, 6)
    print(L2.print_list())
    L2.print_all()
    L2.reverse_list()
    print(L2.print_list())

    L3 = DoubleLinkedList([1, 9, 16, 25, 78])
    L3.sorted_insert(0)
    print(L3.print_list())
