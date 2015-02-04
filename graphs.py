def is_undirected(G):
    """Check that G represents a simple undirected graph."""
    for v in G:
        if v in G[v]:
            return False
        for w in G[v]:
            if v not in G[w]:
                return False
    return True
