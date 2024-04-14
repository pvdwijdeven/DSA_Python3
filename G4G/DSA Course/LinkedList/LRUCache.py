# this class is a least recently used (LRU) cache
# if more elements than capacity, the least recently used
# (written OR read) element is deleted.
class LRUCache:

    def __init__(self, cap):
        # code here
        self.cap = cap
        self.mp = {}
        self.head = None
        self.tail = None
        self.cnt = 0

    class Node:
        def __init__(self, data, next=None, prev=None, key=None):
            self.data = data
            self.next = next
            self.prev = prev
            self.key = key

    def delete_node(self, ptr):
        # delete node as indicated by given pointer ptr
        if self.tail == ptr:
            self.delete_tail()
            return
        if self.head == ptr:
            self.delete_head()
            return
        prev = ptr.prev
        next = ptr.next
        prev.next = next
        next.prev = prev

    def delete_head(self):
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

    def delete_tail(self):
        if not self.head:
            self.head = None
            self.tail = None
            return None
        if not self.tail:
            self.tail = None
            self.head = None
            return None
        prev = self.tail.prev
        if not prev:
            self.tail = None
            self.head = None
            return None
        prev.next = None
        self.tail = prev
        return self.head

    def insert_in_tail(self, data, key):
        temp = self.Node(data=data, key=key)
        if not self.head:
            self.tail = temp
            self.head = temp
            return temp, temp
        temp2 = self.tail
        assert temp2
        temp2.next = temp
        temp.prev = temp2
        self.tail = temp
        return self.head, temp

    # Function to return value corresponding to the key.
    def get(self, key):
        if key in self.mp:
            self.delete_node(ptr=self.mp[key])
            self.head, self.mp[key] = self.insert_in_tail(
                data=self.mp[key].data, key=key
            )
            return self.mp[key].data
        else:
            return -1

    # Function for storing key-value pair.
    def set(self, key, value):
        if key in self.mp:
            self.delete_node(ptr=self.mp[key])
            self.cnt -= 1
        # create node and add to end of tail
        self.head, self.mp[key] = self.insert_in_tail(data=value, key=key)
        self.cnt += 1
        if self.cnt > self.cap:
            del self.mp[self.head.key]
            self.delete_head()
            self.cnt -= 1

    def print_list(self):
        cur = self.head
        while cur != None:
            if cur.next:
                key_next = cur.next.key
            else:
                key_next = None
            if cur.prev:
                key_prev = cur.prev.key
            else:
                key_prev = None

            print(f"{cur.key} {cur.data} {key_next} {key_prev}")
            cur = cur.next
        print("____")


if __name__ == "__main__":
    cap = 4
    commands = 87
    commands = "SET 94 16 SET 93 87 SET 63 22 SET 60 91 SET 41 27 GET 73 GET 12 GET 68 SET 31 83 GET 24 SET 30 36 GET 23 GET 70 SET 57 94 SET 30 43 SET 20 22 GET 38 GET 25 SET 14 71 GET 92 GET 57 SET 71 63 GET 82 SET 85 26 SET 6 37 GET 30 SET 25 58 SET 46 83 GET 68 GET 65 SET 88 51 GET 77 GET 89 GET 4 SET 100 55 GET 61 GET 69 SET 27 13 GET 95 SET 71 96 GET 79 SET 98 2 GET 18 GET 53 GET 2 GET 87 SET 90 66 GET 20 GET 30 SET 98 18 SET 76 82 SET 68 28 GET 98 SET 66 87 GET 84 SET 29 25 SET 30 33 SET 71 20 GET 9 SET 50 41 GET 24 GET 46 GET 52 SET 80 56 GET 65 GET 42 GET 94 GET 35 GET 25 GET 88 GET 44 SET 66 28 SET 33 37 SET 29 38 SET 75 8 SET 96 59 SET 36 38 SET 29 19 SET 29 12 SET 5 77 SET 14 64 GET 7 GET 5 GET 29 GET 70 SET 97 18 GET 44"
    l = LRUCache(cap)

    coms = commands.split(" ")
    n = 0
    while n < len(coms):
        if coms[n] == "SET":
            l.set(key=coms[n + 1], value=coms[n + 2])
            n += 3

        elif coms[n] == "GET":
            print(l.get(key=coms[n + 1]))
            n += 2
