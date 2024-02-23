from typing import Any


class Node:
    def __init__(self, data, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

    @property
    def var_next(self) -> Any:
        assert self.next is not None
        return self.next

    @property
    def var_prev(self) -> Any:
        assert self.prev is not None
        return self.prev

    def print(self) -> None:
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
    def __init__(self, arr=None) -> None:
        if not arr:
            self.head = Node(data=None)
        else:
            if isinstance(arr, list):
                self.list_from_arr(arr=arr)
            else:
                self.list_from_string(slist=arr)

    def list_from_string(self, slist) -> Node | None:
        llist = [int(x) for x in slist.split("<->")]
        return self.list_from_arr(arr=llist)

    def list_from_arr(self, arr) -> Node | None:
        if arr == []:
            self.head = Node(data=None)
            return self.head
        prev_node = Node(data=None)
        prev_prev = None
        head = prev_node
        for value in arr:
            cur = Node(data=value)
            prev_node.next = cur
            prev_node.prev = prev_prev
            prev_prev = prev_node
            prev_node = cur
        cur.prev = prev_prev
        if head.next:
            head.next.prev = None
        self.head = head.next
        return head.next

    def print_list(self, show=True) -> list[Any]:
        res = []
        cur = self.head
        if not cur:
            if show:
                print("[]")
            return []
        while cur.next:
            res.append(cur.data)
            cur = cur.next
        res.append(cur.data)
        if show:
            print(res)
        return res

    def insert_in_head(self, data) -> Node:
        temp = Node(data=data)
        temp.prev = None
        temp.next = self.head
        if self.head:
            self.head.prev = temp
        self.head = temp
        return temp

    def insert_in_tail(self, data) -> Node:
        temp = Node(data=data)
        if not self.head:
            return temp
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = temp
        temp.prev = cur
        return self.head

    def insert_at_position(self, pos, data) -> Node | None:
        temp = Node(data=data)
        cur = self.head
        for i in range(0, pos):
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

    def delete_head(self) -> Node | None:
        if not self.head:
            return None
        if not self.head.next:
            return None
        else:
            self.head = self.head.next
            self.head.prev = None
            return self.head

    def delete_Nth_node(self, N) -> Node | None:
        cur = self.head
        for pos in range(1, N):
            if cur:
                cur = cur.next
        if cur:
            if cur.prev:
                cur.prev.next = cur.next
            if cur.next:
                cur.next.prev = cur.prev
        return self.head

    def delete_tail(self) -> Node | None:
        if not self.head:
            return None
        if not self.head.next:
            return None
        cur = self.head
        prev = Node(data=None)
        while cur.next:
            prev = cur
            cur = cur.next
        prev.next = None
        return self.head

    def find_middle(self, show=True) -> Any | None:
        if self.head:
            curl = self.head
            cur = self.head.prev
        if cur and curl:
            while curl != cur:
                if cur and curl:
                    curl = curl.next
                    cur = cur.prev
            if show:
                print(cur.data)
            return cur.data

    def print_all(self) -> None:
        cur = self.head
        if cur:
            while cur.next:
                cur.print()
                cur = cur.next
            cur.print()
        return

    def reverse_list(self) -> Node | None:
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

    # def insert_in_sorted(self, data) -> Node | None:
    #     # Insert value in sorted list

    #     temp = Node(data=data)
    #     if not self.head:
    #         return temp
    #     if self.head.data <= self.tail.data:
    #         if data < self.head.data:
    #             temp.next = self.head
    #             self.head.prev = temp
    #             self.head = temp
    #             return temp
    #         else:
    #             cur = self.head
    #             while cur.next and cur.next.data < data:
    #                 cur = cur.next
    #             temp.next = cur.next
    #             cur.next = temp
    #             return self.head
    #     else:
    #         if data > self.head.data:
    #             temp.next = self.head
    #             self.head = temp
    #             return temp
    #         else:
    #             cur = self.head
    #             while cur.next and cur.next.data > data:
    #                 cur = cur.next
    #             temp.next = cur.next
    #             cur.next = temp
    #             return self.head


if __name__ == "__main__":
    L1 = DoubleLinkedList(arr="1<->2<->3<->4<->5")
    L1.print_all()
    L1.print_list()

    L1.insert_in_head(data=20)
    L1.insert_in_tail(data=44)
    L1.insert_at_position(pos=2, data=50)
    L1.print_list()

    L2 = DoubleLinkedList(arr="2<->4<->5")
    L2.insert_at_position(pos=2, data=6)
    L2.print_list()
    L2.print_all()
    L2.reverse_list()
    L2.print_list()

    L3 = DoubleLinkedList(arr=[1, 9, 16, 25, 78])
    # L3.sorted_insert(value=26)
    L3.print_list()
    L3.find_middle()
