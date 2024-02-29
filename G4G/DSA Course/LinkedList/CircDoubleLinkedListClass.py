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


class CircularDoubleLinkedList:
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
        cur = None
        for value in arr:
            cur = Node(data=value)
            prev_node.next = cur
            prev_node.prev = prev_prev
            prev_prev = prev_node
            prev_node = cur
        assert cur
        cur.prev = prev_prev
        cur.next = head.next
        if head.next:
            head.next.prev = cur
        self.head = head.next
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
            cur = root.head
            while cur.prev and cur.prev != root.head:
                cur = cur.prev
            if cur.prev == None:
                return False
            return True

        res = test_circular(root=root)
        if show:
            print(res)
        return res

    @classmethod
    def compare_CLL(cls, CLL1, CLL2, show=True) -> bool:
        def test_CLL(CLL1, CLL2) -> bool:
            curr1 = CLL1.head
            curr2 = CLL2.head

            while True:
                if curr1.data != curr2.data:
                    return False
                curr1 = curr1.next
                curr2 = curr2.next

                if curr1.next == CLL1.head and curr2.next == CLL2.head:
                    return True

                if curr1.next == CLL1.head or curr2.next == CLL2.head:
                    return False

        res = test_CLL(CLL1=CLL1, CLL2=CLL2)
        if show:
            print(res)
        return res


if __name__ == "__main__":
    L1 = CircularDoubleLinkedList(arr="1<->2<->3<->4<->5")
    L1.print_list()
    L2 = CircularDoubleLinkedList(arr=[1, 2, 3, 4, 5])
    CircularDoubleLinkedList.compare_CLL(CLL1=L1, CLL2=L2)
    L2 = CircularDoubleLinkedList(arr=[1, 2, 3, 5])
    CircularDoubleLinkedList.compare_CLL(CLL1=L1, CLL2=L2)
    CircularDoubleLinkedList.is_circular(root=L1)
    if L1.head:
        L1.head.prev = None
        CircularDoubleLinkedList.is_circular(root=L1)
