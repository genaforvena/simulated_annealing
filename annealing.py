from random import random
import math
import copy

from unionFind import UnionFind
from graphs import is_undirected


__author__ = 'imozerov'


class Solution:
    """
    Object with weights map.
    Map contains names of pairs as keys and weights as values
    This object is able to create it's neighbour by
    randomly changing one of weights.
    """
    def __init__(self):
        self._weights_map = {}

    @property
    def weights_map(self):
        return self._weights_map

    @weights_map.setter
    def weights_map(self, new_map):
        self._weights_map = new_map

    def neighbor(self):
        neighbor = copy.deepcopy(self)
        neighbor.weights_map[random.choice(self._weights_map.keys())] = random()
        return neighbor

    def to_graph(self, sentence):
        """
        creates graph with given weight vectors.
        graph is represented as it minimum_spinning_tree requires
        """
        graph = []
        for word in sentence:
            
            graph[word.position] = word.parent
        pass


def anneal(sol):
    old_cost = cost(sol)
    T = 1.0
    T_min = 0.00001
    alpha = 0.99
    while T > T_min:
        i = 1
        while i <= 100:
            new_sol = sol.neighbor()
            new_cost = cost(new_sol)
            ap = acceptance_probability(old_cost, new_cost, T)
            if ap > random():
                sol = new_sol
                old_cost = new_cost
            i += 1
        T *= alpha
    return sol, cost


def cost(sol):
    """
    builds a tree with solution weight and after that
    calculates distance between new tree and same tree for
    same sentence from training dataset
    """
    pass

    return 0


def minimum_spanning_tree(graph):
    """
    Return the minimum spanning tree of an undirected graph G.
    G should be represented in such a way that iter(G) lists its
    vertices, iter(G[u]) lists the neighbors of u, G[u][v] gives the
    length of edge u,v, and G[u][v] should always equal G[v][u].
    The tree is returned as a list of edges.
    """
    if not is_undirected(graph):
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


def acceptance_probability(old_cost, new_cost, temperature):
    return math.exp((new_cost - old_cost) / temperature)


if __name__ == "__main__":
    pass
