from collections import defaultdict


class Solution:
    def __init__(self):
        self.count = 0

    def possible_paths(self, adj, V, source, destination):
        graph = defaultdict(list)
        for x in adj:
            graph[x[0]].append(x[1])
        self.dfs(source, destination, graph)
        return self.count

    def dfs(self, node, destination, adj):
        if node == destination:
            self.count += 1
        for nbr in adj[node]:
            self.dfs(nbr, destination, adj)


# {
# Driver Code Starts

# Initial Template for Python 3
inp = """0 1
0 3
1 2
3 2""".split(
    "\n"
)
if __name__ == "__main__":
    T = 1
    for i in range(T):
        n, m, s, d = 4, 4, 0, 2
        n = int(n)
        m = int(m)
        s = int(s)
        d = int(d)
        edges = []
        for i in range(m):
            x, y = inp[i].split()
            x = int(x)
            y = int(y)
            edges.append([x, y])
        obj = Solution()
        ans = obj.possible_paths(edges, n, s, d)
        print(ans)
