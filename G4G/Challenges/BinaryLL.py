class node:
    def __init__(self):
        self.data = None
        self.next = None


class Solution:
    def decimalValue(self, head):
        MOD = 10**9 + 7
        # Code here
        arr = []
        if head - None:
            return 0
        cur = head
        while cur:
            arr.append(cur.data)
            cur = cur.next
        p = len(arr) - 1
        total = 0
        for i in arr:
            total += i * (2**p)
            p -= 1
        return total % MOD


sol = Solution()

sol.decimalValue(5)
