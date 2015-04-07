from unionFind import UnionFind

class Graph:
    def __init__(self, words, solution):
        self._graph = self._create_graph(words, solution)
        pass

    def _create_graph(self, words, solution):
        """
        creates graph with given weight vectors.
        graph is represented as it minimum_spinning_tree function requires
        """
        graph = []
        for word in words:
            for other_word in words:
                if word is other_word:
                    continue
                graph[word] = graph[word] + [other_word, solution.get_weight(word, other_word)]
        return graph

    def minimum_spanning_tree(self, solution):
        """
        Return the minimum spanning tree of an undirected graph G.
        G should be represented in such a way that iter(G) lists its
        vertices, iter(G[u]) lists the neighbors of u, G[u][v] gives the
        length of edge u,v, and G[u][v] should always equal G[v][u].
        The tree is returned as a list of edges.
        """
        graph = self._to_graph(solution)
        if not is_undirected():
            raise ValueError("MinimumSpanningTree: input is not undirected")
        for u in graph:
            for v in graph[u]:
                if graph[u][v] != graph[v][u]:
                    raise ValueError("MinimumSpanningTree: asymmetric weights")

        # Kruskal's algorithm: sort edges by weight, and add them one at a time.
        # We use Kruskal's algorithm, first because it is very simple to
        # implement once UnionFind exists, and second, because the only slow
        # part (the sort) is sped up by being built in to Python.
        subtrees = UnionFind()
        tree = []
        for W, u, v in sorted((graph[u][v], u, v) for u in graph for v in graph[u]):
            if subtrees[u] != subtrees[v]:
                tree.append((u, v))
                subtrees.union(u, v)
        return tree

    def is_undirected():
        """Check that it is simple undirected graph."""
        for v in G:
            if v in G[v]:
                return False
            for w in G[v]:
                if v not in G[w]:
                    return False
        return True
