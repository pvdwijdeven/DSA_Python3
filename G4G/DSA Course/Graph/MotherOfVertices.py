from collections import defaultdict

# This class represents a directed graph using adjacency list
# representation


class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary

    # A recursive function to print DFS starting from v
    def DFSUtil(self, v, visited):

        # Mark the current node as visited and print it
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    # Add w to the list of v
    def addEdge(self, v, w):
        self.graph[v].append(w)

    # Returns a mother vertex if exists. Otherwise returns -1
    # uses Kosaraju's algorithm
    def findMother(self):

        # visited[] is used for DFS. Initially all are
        # initialized as not visited
        visited = [False] * (self.V)

        # To store last finished vertex (or mother vertex)
        v = 0

        # Do a DFS traversal and find the last finished
        # vertex
        for i in range(self.V):
            if visited[i] == False:
                self.DFSUtil(i, visited)
                v = i

        # If there exist mother vertex (or vertices) in given
        # graph, then v must be one (or one of them)

        # Now check if v is actually a mother vertex (or graph
        # has a mother vertex). We basically check if every vertex
        # is reachable from v or not.

        # Reset all values in visited[] as false and do
        # DFS beginning from v to check if all vertices are
        # reachable from it or not.
        visited = [False] * (self.V)
        self.DFSUtil(v, visited)
        if any(i == False for i in visited):
            return -1
        else:
            return v


class Solution:

    # Function to find a Mother Vertex in the Graph.
    def findMotherVertex(self, V, adj):
        g = Graph(V)
        g.graph = adj
        return g.findMother()
