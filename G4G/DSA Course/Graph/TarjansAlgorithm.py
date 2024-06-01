from functools import reduce


def sccs(adj):
    "Return sccs as list of vertices."
    ct = [0] * len(adj)  # circle time
    on_stack = ct[:]
    stack = []
    t = 0
    ccs = []

    def visit(n):
        if not ct[n]:
            nonlocal t
            ct[n] = vt = t = t + 1
            on_stack[n] = 1
            sl = len(stack)
            stack.append(n)
            ct[n] = reduce(min, map(visit, adj[n]), vt)

            if vt == ct[n]:
                cc = stack[sl:]
                del stack[sl:]
                for c in cc:
                    on_stack[c] = 0
                cc.sort()
                ccs.append(cc)
        return ct[n] if on_stack[n] else t

    all(map(visit, range(len(ct))))
    ccs.sort()
    return ccs


class Solution:

    # Function to return a list of lists of integers denoting the members
    # of strongly connected components in the given graph.
    def tarjans(self, V, adj):
        return sccs(adj)
