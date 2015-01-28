from random import random
import math
from UnionFind import UnionFind
from Graphs import isUndirected

__author__ = 'imozerov'

class Solution:
    # Map-like object containing names of pairs as keys and weights as values
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
    pass
    # should build a tree with solution weights
    # and after that
    # calculate distance between new tree and same tree for same sentence from training dataset
    return 0


def minimum_spanning_tree(graph):
    """
    Return the minimum spanning tree of an undirected graph G.
    G should be represented in such a way that iter(G) lists its
    vertices, iter(G[u]) lists the neighbors of u, G[u][v] gives the
    length of edge u,v, and G[u][v] should always equal G[v][u].
    The tree is returned as a list of edges.
    """
    if not isUndirected(graph):
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
