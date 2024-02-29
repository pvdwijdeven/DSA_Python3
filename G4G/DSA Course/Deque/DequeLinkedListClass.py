from typing import Any


class Node:
    def __init__(self, data, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev


class Deque:
    def __init__(self) -> None:
        self.front = None
        self.rear = None

    def list_from_string(self, list_string) -> Node | None:
        llist = [int(x) for x in list_string.split("->")]
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
        self.front = head.next
        self.rear = cur
        return head.next

    def print_list(self, show=True) -> list[Any]:
        res = []
        cur = self.front
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

    def insert_front(self, data) -> None:
        temp = Node(data=data)
        if not self.front:
            self.front = temp
            self.rear = temp
            return
        temp.next = self.front
        self.front.prev = temp
        self.front = temp
        return

    def insert_rear(self, data) -> None:
        temp = Node(data=data)
        if not self.rear:
            self.rear = temp
            self.front = temp
            return
        temp.prev = self.rear
        self.rear.next = temp
        self.rear = temp
        return

    def delete_front(self) -> None:
        if not self.front:
            return
        res = self.front.data
        self.front = self.front.next
        if not self.front:
            return
        self.front.prev = None
        return res

    def delete_rear(self) -> None:
        if not self.rear:
            return
        res = self.rear.data
        self.rear = self.rear.prev
        if not self.rear:
            return
        self.rear.next = None
        return res

    def get_front(self) -> Any | None:
        if self.front:
            return self.front.data

    def get_rear(self) -> Any | None:
        if self.rear:
            return self.rear.data


if __name__ == "__main__":
    deq = Deque()
    deq.list_from_string(list_string="1->2->3->4")
    deq.print_list()
    deq.insert_front(data=10)
    deq.print_list()
    deq.insert_rear(data=20)
    deq.print_list()
    print(deq.delete_rear())
    print(deq.get_rear())
    deq.print_list()
    print(deq.delete_front())
    print(deq.get_front())
    deq.print_list()
