class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class CircularLinkedList:
    def __init__(self, arr):
        if not arr:
            self.head = Node(None)
        else:
            if isinstance(arr, list):
                self.head = self.list_from_arr(arr)
            else:
                self.head = self.list_from_string(arr)

    def list_from_string(self, slist):
        llist = [int(x) for x in slist.split("->")]
        return self.list_from_arr(llist)

    def list_from_arr(self, arr):
        prev = Node(None)
        head = prev
        for x in arr:
            cur = Node(x)
            prev.next = cur
            prev = cur
        prev.next = head.next
        return head.next

    def print_list(self):
        array = []
        if not self.head:
            return []
        cur = self.head
        while cur.next and cur.next != self.head:
            array.append(cur.data)
            cur = cur.next
        array.append(cur.data)
        return array

    def get_length(self):
        count = 0
        if not self.head:
            return 0
        cur = self.head
        while cur.next and cur.next != self.head:
            count += 1
            cur = cur.next
        count += 1
        return count

    def insert_in_head(self, x):
        temp = Node(x)
        if not self.head:
            temp.next = temp
            return temp
        temp.next = self.head.next
        self.head.next = temp
        temp.data, self.head.data = self.head.data, temp.data
        return self.head

    def insert_in_tail(self, x):
        temp = Node(x)
        if not self.head:
            temp.next = temp
            return temp
        cur = self.head
        prev = Node(None)
        while cur.next and cur.next != self.head:
            cur = cur.next
        temp.data, cur.data = cur.data, temp.data
        return self.head

    def delete_tail(self):
        if not self.head:
            return None
        cur = self.head
        prev = Node(None)
        if cur.next == self.head:
            return None
        while cur.next and cur.next != self.head:
            prev = cur
            cur = cur.next
        prev.next = self.head
        return self.head

    def is_circulrat(self):
        if not self.head:
            return False
        cur = self.head
        if not self.head:
            return False
        while cur.next and cur.next != self.head:
            cur = cur.next
        if cur.next == None:
            return False
        return True

    def delete_head(self):
        if not self.head:
            return None
        cur = self.head
        if not self.head or cur.next == self.head:
            return None
        if self.head.next:
            self.head.data = self.head.next.data
            self.head.next = self.head.next.next
        return self.head

    def del_Nth(self, k):
        if not self.head:
            return self.head
        elif k == 1:
            return self.delete_head()
        else:
            cur = self.head
            for i in range(k - 2):
                if cur:
                    cur = cur.next
            if cur and cur.next:
                cur.next = cur.next.next
            return self.head

    def insert_at_position(self, pos, data):
        temp = Node(data)
        c_pos = 1
        if not self.head:
            if pos == 1:
                temp.next = temp
                return temp
            else:
                return None
        cur = self.head
        while pos > c_pos and cur.next and cur.next != self.head:
            cur = cur.next
            c_pos += 1
        if pos == c_pos:
            temp.next = cur.next
            cur.next = temp
        return self.head


if __name__ == "__main__":
    L1 = CircularLinkedList("1->2->3->4->5")
    print(L1.print_list())
    print(L1.get_length())
    L1.insert_in_tail(10)
    print(L1.print_list())
    L1.delete_tail()
    print(L1.print_list())
    L1.insert_at_position(3, 20)
    print(L1.print_list())
