from collections import deque


def bfs(graph, S, par, dist):
    # Queue to store the nodes in the order they are visited
    q = deque()
    # Mark the distance of the source node as 0
    dist[S] = 0
    # Push the source node to the queue
    q.append(S)

    # Iterate until the queue is not empty
    while q:
        # Pop the node at the front of the queue
        node = q.popleft()

        # Explore all the neighbors of the current node
        for neighbor in graph[node]:
            # Check if the neighboring node is not visited
            if dist[neighbor] == float("inf"):
                # Mark the current node as the parent of the neighboring node
                par[neighbor] = node
                # Mark the distance of the neighboring node as the distance of the current node + 1
                dist[neighbor] = dist[node] + 1
                # Insert the neighboring node to the queue
                q.append(neighbor)


def print_shortest_distance(graph, S, D, V):
    # par[] array stores the parent of nodes
    par = [-1] * V

    # dist[] array stores the distance of nodes from S
    dist = [float("inf")] * V

    # Function call to find the distance of all nodes and their parent nodes
    bfs(graph, S, par, dist)

    if dist[D] == float("inf"):
        return -1

    # List path stores the shortest path
    path = []
    current_node = D
    path.append(D)
    while par[current_node] != -1:
        path.append(par[current_node])
        current_node = par[current_node]
    return len(path) - 1


class Solution:
    def levelOfX(self, V, adj, X):
        return print_shortest_distance(adj, 0, X, V)


if __name__ == "__main__":
    inp = """6 7
0 1 
0 2 
1 3 
1 4 
1 5 
2 4
3 5"""
    X = 5

    inp = inp.split("\n")
    V, E = map(int, inp[0].split())
    adj = [[] for i in range(V)]
    for i in range(E):
        u, v = map(int, inp[i + 1].split())
        adj[u].append(v)
        adj[v].append(u)
    obj = Solution()
    print(obj.levelOfX(V, adj, X))
