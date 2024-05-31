def isBridge(V, adj, c, d):
    # code here
    if c in adj[d]:
        adj[d].remove(c)
    if d in adj[c]:
        adj[c].remove(d)
    else:
        return 0

    def dfs(node):
        visit.add(node)
        for ngh in adj[node]:
            if ngh not in visit:
                dfs(ngh)

    visit = set()
    dfs(c)
    if d in visit:
        return 0
    return 1
