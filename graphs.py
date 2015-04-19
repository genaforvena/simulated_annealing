import itertools
from unionFind import UnionFind


class Graph:
    def __init__(self, words, solution):
        word_pairs = itertools.combinations(words, 2)
        self._graph = [[word1, word2, solution.get_weight(word1, word2)] for (word1, word2) in word_pairs]

    def minimum_spanning_tree(self):
        """
        Return the minimum spanning tree of an undirected graph G.
        G should be represented in such a way that iter(G) lists its
        vertices, iter(G[u]) lists the neighbors of u, G[u][v] gives the
        length of edge u,v, and G[u][v] should always equal G[v][u].
        The tree is returned as a list of edges.
        """
        subtrees = UnionFind()
        tree = []
        for u, v, W in sorted(self._graph, key=lambda x: x[2]):
            if subtrees[u] != subtrees[v]:
                tree.append((u, v))
                subtrees.union(u, v)
        return tree

    @property
    def graph(self):
        return self._graph
