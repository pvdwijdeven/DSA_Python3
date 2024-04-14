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
            self.tail = Node(data=None)
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
        cur = None
        for value in arr:
            cur = Node(data=value)
            prev_node.next = cur
            prev_node.prev = prev_prev
            prev_prev = prev_node
            prev_node = cur
        assert cur
        cur.prev = prev_prev
        assert head.next
        head.next.prev = None
        self.head = head.next
        self.tail = cur
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

    def get_count(self) -> int:
        # return number of elements in linked list
        if not self.head:
            return 0
        cur = self.head
        count = 1
        while cur.next:
            count += 1
            cur = cur.next
        return count

    def sum_of_elements(self) -> int:
        # return sum of elements in linked list
        if not self.head:
            return 0
        cur = self.head
        total = cur.data
        while cur.next:
            cur = cur.next
            total += cur.data
        return total

    def search_linked_list(self, value) -> int:
        # search for value in linked list and return first found
        if not self.head:
            return -1
        cur = self.head
        index = 0
        while cur.next:
            if cur.data == value:
                return index
            index += 1
            cur = cur.next
        return index

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
        self.tail = temp
        return self.head

    def insert_at_position(self, pos, value) -> Node | None:
        temp = Node(data=value)
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
            if temp.next:
                temp.next.prev = temp
            else:
                self.tail = temp
        return self.head

    def delete_head(self) -> Node | None:
        if not self.head:
            return None
        if not self.head.next:
            self.head = None
            self.tail = None
            return None
        else:
            self.head = self.head.next
            self.head.prev = None
            return self.head

    def delete_node(self, ptr) -> None:
        # delete node as indicated by given pointer ptr
        if self.tail == ptr:
            self.delete_tail()
            return
        if self.head == ptr:
            self.delete_head()
        ptr.prev.next = ptr.next
        ptr.next.prev = ptr.prev

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
            else:
                self.tail = cur
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
        self.tail = prev
        return self.head

    def find_middle(self, show=True) -> Any | None:
        cur = None
        curl = None
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
        cur_node = "head>"
        if cur:
            while cur.next:
                print(cur_node, end=" ")
                cur_node = "node "
                cur.print()
                cur = cur.next
            print("tail<", end=" ")
            assert cur == self.tail
            cur.print()
        return

    def reverse_list(self) -> Node | None:
        # return head after reversing
        if not self.head:
            return None
        self.tail = self.head
        cur = self.head
        while cur.next:
            cur.next, cur.prev = cur.prev, cur.next
            cur = cur.prev
        cur.next, cur.prev = cur.prev, cur.next
        self.head = cur
        return cur

    def insert_in_sorted(self, value) -> Node | None:
        # Insert value in sorted list

        temp = Node(data=value)
        if not self.head:
            return temp
        assert self.tail
        if self.head.data <= self.tail.data:
            if value < self.head.data:
                self.insert_in_head(data=value)
                # temp.next = self.head
                # self.head = temp
                # return temp
            else:
                cur = self.head
                while cur.next and cur.next.data < value:
                    cur = cur.next
                temp.next = cur.next
                temp.prev = cur
                cur.next = temp
                if self.tail == cur:
                    self.tail = temp
                return self.head
        else:
            if value > self.head.data:
                self.insert_in_head(data=value)
                # temp.next = self.head
                # self.head = temp
                # return temp
            else:
                cur = self.head
                while cur.next and cur.next.data > value:
                    cur = cur.next
                temp.next = cur.next
                temp.prev = cur
                cur.next = temp
                if self.tail == cur:
                    self.tail = temp
                return self.head

    def merge(self, head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        if head1.data < head2.data:
            head1.next = self.merge(head1.next, head2)
            head1.next.prev = head1
            head1.prev = None
            return head1
        else:
            head2.next = self.merge(head1, head2.next)
            head2.next.prev = head2
            head2.prev = None
            return head2

    def merge_sort(self, head):
        if head is None:
            return head
        if head.next is None:
            return head
        second = self.split(head)
        head = self.merge_sort(head)
        second = self.merge_sort(second)
        return self.merge(head, second)

    def split(self, head):
        fast = slow = head
        while True:
            if fast.next is None:
                break
            if fast.next.next is None:
                break
            fast = fast.next.next
            slow = slow.next
        temp = slow.next
        slow.next = None
        return temp

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node


if __name__ == "__main__":
    L1 = DoubleLinkedList(arr="1<->2<->3<->4<->5")
    L1.print_all()
    L1.print_list()

    L1.insert_in_head(data=20)
    L1.insert_in_tail(data=44)
    L1.insert_at_position(pos=2, value=50)
    L1.print_list()

    L2 = DoubleLinkedList(arr="2<->4<->5")
    L2.insert_at_position(pos=2, value=6)
    L2.print_list()
    L2.print_all()
    L2.reverse_list()
    L2.print_all()
    L2.print_list()

    L3 = DoubleLinkedList(arr=[1, 9, 16, 25, 78])
    L3.reverse_list()
    L3.insert_in_sorted(value=79)
    L3.print_list()
    L3.find_middle()
