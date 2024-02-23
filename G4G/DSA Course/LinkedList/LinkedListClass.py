# Linked list class


from typing import Any


class Node:

    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self, arr=None) -> None:
        if not arr:
            self.head = Node(data=None)
            self.tail = Node(data=None)
        else:
            if isinstance(arr, list):
                self.list_from_arr(arr=arr)
            else:
                self.list_from_string(list_string=arr)

    def list_from_string(self, list_string) -> Node | None:
        # create linked list from string with "->"
        llist = [int(x) for x in list_string.split("->")]
        return self.list_from_arr(arr=llist)

    def list_from_arr(self, arr) -> Node | None:
        # create linked list from array
        prev = Node(data=None)
        head = prev
        for x in arr:
            cur = Node(data=x)
            prev.next = cur
            prev = cur
        self.tail = cur
        self.head = head.next
        return head.next

    def print_list(self) -> list[Any]:
        # return linked list as array
        array = []
        if not self.head:
            return array
        cur = self.head
        while True:
            array.append(cur.data)
            if not cur.next:
                break
            cur = cur.next
        print(self.head.data, self.tail.data)
        return array

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

    def insert_at_beginning(self, value) -> Node:
        # Insert value at beginning at linked list
        cur = Node(data=value)
        cur.next = self.head
        self.head = cur
        return cur

    def insert_at_end(self, value) -> Node:
        # Insert a node at the end of the linked list.
        if not self.head:
            return Node(data=value)
        cur = self.head
        while cur.next:
            cur = cur.next
        newNode = Node(data=value)
        cur.next = newNode
        self.tail = newNode
        return self.head

    def insert_at_position(self, pos, data) -> Node | None:
        # Insert a node at the given posiition
        temp = Node(data=data)
        if pos == 0:
            temp.next = self.head
            self.head = temp
            return temp
        cur = self.head
        for _i in range(0, pos - 1):
            if cur:
                cur = cur.next
                if not cur:
                    return self.head
        if cur:
            temp.next = cur.next
            cur.next = temp
        if not temp.next:
            self.tail = temp
        return self.head

    def delete_head(self) -> Node | None:
        # Delete head of linked list
        if not self.head:
            return self.head
        else:
            temp = self.head.next
            self.head.next = None
            self.head = temp
            return temp

    def delete_tail(self) -> Node | None:
        # Delete tail of linked list
        cur = self.head
        if not cur or not cur.next:
            return None
        while True:
            if not cur or not cur.next or not cur.next.next:
                break
            prev = cur
            cur = cur.next
        prev.next = None
        self.tail = prev
        return self.head

    def delete_node(self, ptr) -> None:
        # delete node as indicated by given pointer ptr
        if self.tail == ptr:
            self.delete_tail()
            return
        if self.head == ptr:
            self.head = ptr.next
        temp = ptr.next
        ptr.data = temp.data
        ptr.next = temp.next

    def delete_at_position(self, pos) -> Node | None:
        # delete node at given position
        cur = self.head
        if not cur:
            return None
        c = 0
        if pos == 0:
            self.head = cur.next
            return cur.next
        while cur:
            if c + 1 == pos and cur.next:
                temp = cur.next.next
                cur.next = temp
            elif c + 1 == pos:
                self.tail = cur
                return self.head
            cur = cur.next
            c += 1
        return self.head

    def insert_in_sorted(self, data) -> Node | None:
        # Insert value in sorted list

        temp = Node(data=data)
        if not self.head:
            return temp
        if self.head.data <= self.tail.data:
            if data < self.head.data:
                temp.next = self.head
                self.head = temp
                return temp
            else:
                cur = self.head
                while cur.next and cur.next.data < data:
                    cur = cur.next
                temp.next = cur.next
                cur.next = temp
                if self.tail == cur:
                    self.tail = temp
                return self.head
        else:
            if data > self.head.data:
                temp.next = self.head
                self.head = temp
                return temp
            else:
                cur = self.head
                while cur.next and cur.next.data > data:
                    cur = cur.next
                temp.next = cur.next
                cur.next = temp
                if self.tail == cur:
                    self.tail = temp
                return self.head

    def insert_in_mid(self, node) -> Node | None:
        # Insert node in middle of linked list
        node = Node(data=node)
        if not self.head:
            return node
        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            if slow:
                slow = slow.next
            fast = fast.next.next
        if slow:
            node.next = slow.next
            slow.next = node
        return self.head

    def is_sorted(self) -> bool:
        # Check if linked list is sorted
        curN = self.head
        if not curN:
            return True
        curD = curN.data
        direction = "equal"
        while curN.next:
            curN = curN.next
            if curD > curN.data:
                if direction == "equal" or direction == "decreasing":
                    direction = "decreasing"
                else:
                    return False
            if curD < curN.data:
                if direction == "equal" or direction == "increasing":
                    direction = "increasing"
                else:
                    return False
            curD = curN.data
        return True

    def get_Nth_from_last(self, N) -> Any | None:
        # Get value of nth node from end of linked list (0-based)
        N = N + 1
        if N == 0:
            return -1
        if not self.head:
            return -1
        cur1 = self.head
        cur2 = self.head
        while cur1:
            if N:
                cur1 = cur1.next
                N -= 1
            else:
                cur1 = cur1.next
                if cur2:
                    cur2 = cur2.next
        if N:
            return -1
        if cur2:
            return cur2.data

    @classmethod
    def join_the_lists(cls, head1, head2) -> Any:
        # Join linked list head2 with current one
        if not head1.head:
            return head2.head
        cur = head1.head
        while cur.next:
            cur = cur.next
        cur.next = head2.head
        head1.tail = head2.head
        return head1

    def remove_duplicates(self) -> Node | None:
        # Remove all duplicates in linked list
        if not self.head:
            return None
        cur = self.head
        while cur.next:
            if cur.data == cur.next.data:
                cur.next = cur.next.next
            else:
                cur = cur.next
        if cur != self.tail:
            self.tail = cur
        return self.head

    def reverse_list(self) -> Node | None:
        # Reverse the list
        stack = []
        if not self.head:
            return None
        cur = self.head
        self.tail = cur
        while cur.next:
            stack.append(cur)
            cur = cur.next
        self.head = cur
        while stack != []:
            cur.next = stack.pop()
            cur = cur.next
        cur.next = None
        self.tail = cur
        return self.head

    def maximum(self) -> int:
        # Get maximum number of linked list
        mx = 0
        cur = self.head
        if not cur:
            return 0
        while cur.next:
            if cur.data > mx:
                mx = cur.data
            cur = cur.next
        if cur.data > mx:
            mx = cur.data
        return mx

    def minimum(self) -> int:
        # get minimum number of linked list
        mn = 10**199
        cur = self.head
        if not cur:
            return 0
        while cur.next:
            if cur.data < mn:
                mn = cur.data
            cur = cur.next
        if cur.data < mn:
            mn = cur.data
        return mn

    @classmethod
    def are_identical(cls, head1, head2) -> bool:
        # Check if list head2 is identical to current linked list
        cur1 = head1.head
        cur2 = head2.head
        if not cur1:
            return not cur2
        if not cur2:
            return not cur1
        while cur1.next and cur2.next:
            if cur1.data != cur2.data:
                return False
            cur1 = cur1.next
            cur2 = cur2.next
        if cur1.next != cur2.next:
            return False
        if cur1.data != cur2.data:
            return False
        return True


if __name__ == "__main__":
    l1 = "1->2->3->4->5"
    L1 = LinkedList()
    L1.list_from_string(list_string=l1)
    print(L1.print_list())
    print(L1.get_count())
    print(L1.sum_of_elements())
    print(L1.search_linked_list(value=3))
    L1.insert_at_beginning(value=9)
    L1.insert_at_end(value=8)
    L1.insert_at_position(pos=3, data=99)
    print(L1.print_list())
    L1.delete_head()
    L1.delete_tail()
    print(L1.print_list())
    print(L1.is_sorted())
    if L1.head and L1.head.next and L1.head.next.next:
        L1.delete_node(ptr=L1.head.next.next)
    print(L1.print_list())

    L1.delete_at_position(pos=2)
    print(L1.print_list())

    l2 = "1->1->1->3->3->3->4->4"
    L2 = LinkedList(arr=l2)
    print(L2.print_list())
    L2.reverse_list()
    print(L2.print_list())
    L2.remove_duplicates()
    print(L2.print_list())
    print(L2.is_sorted())
    L2.insert_in_sorted(data=2)
    print(L2.print_list())
    L2.insert_in_mid(node=99)
    print(L2.print_list())
    L2.insert_in_mid(node=-99)
    print(L2.print_list())
    print(L2.get_Nth_from_last(N=2))

    L3 = LinkedList(arr=[1, 2, 3, 4, 6, 7, 8, 9])
    print(L3.print_list())
    L3.insert_in_sorted(data=5)
    print(L3.print_list())

    L4 = LinkedList(arr=[1, 2, 3, 4, 5])
    L5 = LinkedList(arr=[6, 7, 8, 9])
    L6 = LinkedList.join_the_lists(head1=L4, head2=L5)
    print(L6.print_list())

    print(LinkedList.are_identical(head1=L4, head2=L5))
    print(LinkedList.are_identical(head1=L3, head2=L6))
    print(L2.maximum())
    print(L2.minimum())
