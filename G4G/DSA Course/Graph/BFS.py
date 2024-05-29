import queue
from typing import List


def BFSUtil(u, adj, visited):
    res = []
    # Create a queue for BFS
    q = queue.Queue()

    # Mark the current node as visited
    # and enqueue it
    visited[u] = True
    q.put(u)

    # 'i' will be used to get all adjacent
    # vertices 4 of a vertex list<int>::iterator i

    while not q.empty():

        # Dequeue a vertex from queue
        # and print it
        u = q.queue[0]
        res.append(u)
        q.get()

        # Get all adjacent vertices of the
        # dequeued vertex s. If an adjacent
        # has not been visited, then mark
        # it visited and enqueue it
        i = 0
        while i != len(adj[u]):
            if not visited[adj[u][i]]:
                visited[adj[u][i]] = True
                q.put(adj[u][i])
            i += 1
    return res


# This function does BFSUtil() for all
# unvisited vertices.
def BFS_disconnected(adj):
    res = []
    V = len(adj)
    visited = [False] * (V + 1)
    for u in range(V):
        if visited[u] == False:
            res += BFSUtil(u, adj, visited)
    return res


def BFS_connected(adj: List[List[int]]) -> List[int]:
    # Mark all the vertices as not visited
    s = 0
    visited = [False] * (len(adj) + 1)
    res = []
    # Create a queue for BFS
    queue = []

    # Mark the source node as
    # visited and enqueue it
    queue.append(s)
    visited[s] = True

    while queue:

        # Dequeue a vertex from
        # queue and print it
        s = queue.pop(0)
        res.append(s)

        # Get all adjacent vertices of the
        # dequeued vertex s. If a adjacent
        # has not been visited, then mark it
        # visited and enqueue it
        for i in adj[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
    return res


def main():
    adj = [[1, 2, 3], [], [4], [], []]

    print(BFS_connected(adj))
    print(BFS_disconnected(adj))

    adj = [[1, 2], [], [4], [], []]
    print(BFS_connected(adj))
    print(BFS_disconnected(adj))


if __name__ == "__main__":
    main()
