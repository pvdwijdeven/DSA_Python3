from math import inf
from typing import Any


class Node:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


def print_tree(arr, val="data", left="left", right="right") -> None:
    def build_tree(arr) -> Node | None:
        # funtion to build tree from an array, where "N" represents empty node
        def grab(it, next_level) -> Node | None:
            value = next(it, "N")
            if value != "N":
                node = Node(data=value)
                next_level.append(node)
                return node

        # Create the root of the tree
        it = iter(arr)
        next_level = []
        root = grab(it=it, next_level=next_level)

        while next_level:
            level = next_level
            next_level = []
            for node in level:
                node.left = grab(it=it, next_level=next_level)
                node.right = grab(it=it, next_level=next_level)

        return root

    # function to print tree in a grahical way
    def display(root, val=val, left=left, right=right) -> Any:
        # Returns list of strings, width, height, and horizontal coordinate of the root.
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = "%s" % getattr(root, val)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(root=getattr(root, left))
            s = "%s" % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in lines]
            return (
                [first_line, second_line] + shifted_lines,
                n + u,
                p + 2,
                n + u // 2,
            )

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(root=getattr(root, right))
            s = "%s" % getattr(root, val)
            u = len(s)
            first_line = s + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(root=getattr(root, left))
        right, m, q, y = display(root=getattr(root, right))
        s = "%s" % getattr(root, val)
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
        second_line = (
            x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
        )
        if p < q:
            left += [n * " "] * (q - p)
        elif q < p:
            right += [m * " "] * (p - q)
        zipped_lines = zip(left, right, strict=True)
        lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    root = build_tree(arr=arr)
    lines, *_ = display(root=root, val=val, left=left, right=right)
    for line in lines:
        print(line)


class MinHeap:
    def __init__(self, arr=[]) -> None:
        self.heap = arr
        self.build_heap()

    def get_parent(self, pos) -> int:
        return (pos - 1) // 2

    def get_left_child(self, pos) -> int:
        return pos * 2 + 1

    def get_right_child(self, pos) -> int:
        return pos * 2 + 2

    def print_tree(self) -> None:
        print_tree(arr=self.heap)

    def build_heap(self) -> None:
        heap = self.heap
        n = len(heap)
        for i in range((n - 2) // 2, -1, -1):
            self.heapify(pos=i, len_heap=n)

    def heap_sort(self) -> None:
        self.build_heap()
        heap = self.heap
        n = len(heap)
        for i in range(n - 1, -1, -1):
            heap[i], heap[0] = heap[0], heap[i]
            self.heapify(pos=0, len_heap=i)
        return self.heap

    def insert(self, value) -> None:
        heap = self.heap
        heap.append(value)
        i = len(heap) - 1
        while i > 0 and heap[i] < heap[self.get_parent(pos=i)]:
            p = self.get_parent(pos=i)
            heap[i], heap[p] = heap[p], heap[i]
            i = p
        return

    def heapify(self, pos, len_heap) -> None:
        heap = self.heap
        lt = self.get_left_child(pos=pos)
        rt = self.get_right_child(pos=pos)
        smallest = pos
        if lt < len_heap and heap[lt] < heap[smallest]:
            smallest = lt
        if rt < len_heap and heap[rt] < heap[smallest]:
            smallest = rt
        if smallest != pos:
            heap[smallest], heap[pos] = heap[pos], heap[smallest]
            self.heapify(pos=smallest, len_heap=len_heap)

    def extract_min(self) -> Any:
        heap = self.heap
        len_heap = len(heap)
        if len_heap == 0:
            return inf
        res = heap[0]
        heap[0] = heap[len_heap - 1]
        heap.pop()
        self.heapify(pos=0, len_heap=len_heap)
        return res

    def decrease_key(self, pos, value) -> None:
        heap = self.heap
        heap[pos] = value
        par = self.get_parent(pos=pos)
        if par >= 0 and heap[par] > heap[pos]:
            heap[par], heap[pos] = heap[pos], heap[par]
            self.decrease_key(pos=par, value=value)
        else:
            return

    def delete_key(self, pos) -> int:
        heap = self.heap
        res = heap[pos]
        heap[pos] = heap[-1]
        heap.pop()
        self.heapify(pos=pos, len_heap=len(heap))
        return res


class MaxHeap:
    def __init__(self, heap=[]) -> None:
        self.heap = heap

    def get_parent(self, pos) -> int:
        return (pos - 1) // 2

    def get_left_child(self, pos) -> int:
        return pos * 2 + 1

    def get_right_child(self, pos) -> int:
        return pos * 2 + 2

    def print_tree(self) -> None:
        print_tree(arr=self.heap)

    def build_heap(self) -> None:
        heap = self.heap
        n = len(heap)
        for i in range((n - 2) // 2, -1, -1):
            self.heapify(pos=i, len_heap=n)

    def heap_sort(self) -> None:
        self.build_heap()
        heap = self.heap
        n = len(heap)
        for i in range(n - 1, -1, -1):
            heap[i], heap[0] = heap[0], heap[i]
            self.heapify(pos=0, len_heap=i)
        return self.heap

    def insert(self, value) -> None:
        heap = self.heap
        heap.append(value)
        i = len(heap) - 1
        while i > 0 and heap[i] > heap[self.get_parent(pos=i)]:
            p = self.get_parent(pos=i)
            heap[i], heap[p] = heap[p], heap[i]
            i = p
        return

    def heapify(self, pos, len_heap) -> None:
        heap = self.heap
        lt = self.get_left_child(pos=pos)
        rt = self.get_right_child(pos=pos)
        largest = pos
        if lt < len_heap and heap[lt] > heap[largest]:
            largest = lt
        if rt < len_heap and heap[rt] > heap[largest]:
            largest = rt
        if largest != pos:
            heap[largest], heap[pos] = heap[pos], heap[largest]
            self.heapify(pos=largest, len_heap=len_heap)

    def extract_max(self) -> Any:
        heap = self.heap
        len_heap = len(heap)
        if len_heap == 0:
            return -inf
        res = heap[0]
        heap[0] = heap[len_heap - 1]
        heap.pop()
        self.heapify(pos=0, len_heap=len_heap)
        return res

    def increase_key(self, pos, value) -> None:
        heap = self.heap
        heap[pos] = value
        par = self.get_parent(pos=pos)
        if par >= 0 and heap[par] < heap[pos]:
            heap[par], heap[pos] = heap[pos], heap[par]
            self.increase_key(pos=par, value=value)
        else:
            return

    def delete_key(self, pos) -> int:
        heap = self.heap
        res = heap[pos]
        heap[pos] = heap[-1]
        heap.pop()
        self.heapify(pos=pos, len_heap=len(heap))
        return res


if __name__ == "__main__":
    hp_min = MinHeap(arr=[100, 25, 10, 40, 50, 5, 20, 45])
    hp_min.print_tree()
    print(hp_min.heap_sort())
    hp_min.insert(value=12)
    hp_min.print_tree()
    hp_min.extract_min()
    hp_min.print_tree()
    hp_min.decrease_key(pos=7, value=5)
    hp_min.print_tree()
    hp_min.delete_key(pos=2)
    hp_min.print_tree()
    print(hp_min.heap_sort())

    hp_max = MaxHeap(heap=[100, 50, 25, 45, 40, 15, 20, 10])
    hp_max.print_tree()
    print(hp_max.heap_sort())
    hp_max.insert(value=75)
    hp_max.print_tree()
    hp_max.extract_max()
    hp_max.print_tree()
    hp_max.increase_key(pos=7, value=100)
    hp_max.print_tree()
    hp_max.delete_key(pos=2)
    hp_max.print_tree()
    print(hp_max.heap_sort())