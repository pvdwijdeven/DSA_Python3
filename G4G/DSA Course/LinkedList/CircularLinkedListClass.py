from typing import Any


class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


class CircularLinkedList:
    def __init__(self, arr) -> None:
        if not arr:
            self.head = Node(data=None)
        else:
            if isinstance(arr, list):
                self.head = self.list_from_arr(arr=arr)
            else:
                self.head = self.list_from_string(string_list=arr)

    def list_from_string(self, string_list) -> Node | None:
        llist = [int(x) for x in string_list.split("->")]
        return self.list_from_arr(arr=llist)

    def list_from_arr(self, arr) -> Node | None:
        prev = Node(data=None)
        head = prev
        for value in arr:
            cur = Node(data=value)
            prev.next = cur
            prev = cur
        prev.next = head.next
        return head.next

    def print_list(self, show=True) -> list[Any]:
        array = []
        if not self.head:
            if show:
                print("[]")
            return []
        cur = self.head
        while cur.next and cur.next != self.head:
            array.append(cur.data)
            cur = cur.next
        array.append(cur.data)
        if show:
            print(array)
        return array

    def get_length(self) -> int:
        count = 0
        if not self.head:
            return 0
        cur = self.head
        while cur.next and cur.next != self.head:
            count += 1
            cur = cur.next
        count += 1
        return count

    def insert_in_head(self, value) -> Node:
        temp = Node(data=value)
        if not self.head:
            temp.next = temp
            return temp
        temp.next = self.head.next
        self.head.next = temp
        temp.data, self.head.data = self.head.data, temp.data
        return self.head

    def insert_in_tail(self, value) -> Node:
        temp = Node(data=value)
        if not self.head:
            temp.next = temp
            return temp
        cur = self.head
        prev = Node(data=None)
        while cur.next and cur.next != self.head:
            cur = cur.next
        temp.data, cur.data = cur.data, temp.data
        return self.head

    def delete_tail(self) -> Node | None:
        if not self.head:
            return None
        cur = self.head
        prev = Node(data=None)
        if cur.next == self.head:
            return None
        while cur.next and cur.next != self.head:
            prev = cur
            cur = cur.next
        prev.next = self.head
        return self.head

    @classmethod
    def is_circular(cls, root, show=True) -> bool:
        def test_circular(root) -> bool:
            if not root.head:
                return False
            cur = root.head
            if not root.head:
                return False
            while cur.next and cur.next != root.head:
                cur = cur.next
            if cur.next == None:
                return False
            return True

        res = test_circular(root=root)
        if show:
            print(res)
        return res

    def delete_head(self) -> Node | None:
        if not self.head:
            return None
        cur = self.head
        if not self.head or cur.next == self.head:
            return None
        if self.head.next:
            self.head.data = self.head.next.data
            self.head.next = self.head.next.next
        return self.head

    def del_Nth(self, N) -> Node | None:
        if not self.head:
            return self.head
        elif N == 0:
            return self.delete_head()
        else:
            cur = self.head
            for i in range(N - 1):
                if cur:
                    cur = cur.next
            if cur and cur.next:
                cur.next = cur.next.next
            return self.head

    def insert_at_position(self, pos, data) -> Node | None:
        temp = Node(data=data)
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
    L1 = CircularLinkedList(arr="1->2->3->4->5")
    L1.print_list()
    L1.get_length()
    L1.insert_in_head(value=99)
    L1.print_list()
    L1.insert_in_tail(value=10)
    L1.print_list()
    L1.delete_tail()
    L1.print_list()
    L1.insert_at_position(pos=3, data=20)
    L1.print_list()
    L1.delete_head()
    L1.print_list()
    L1.del_Nth(3)
    L1.print_list()
    L2 = CircularLinkedList(arr=[1, 2, 3, 4])
    L2.print_list()
    CircularLinkedList.is_circular(root=L2)
