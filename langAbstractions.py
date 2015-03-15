from xml.etree import ElementTree
from unionFind import UnionFind
from graphs import is_undirected

__author__ = 'imozerov'

# Check this tutorial http://effbot.org/zone/element.htm 

class TgtDocument:
    def __init__(self, filename):
        tree = ElementTree.parse(filename)
        root = tree.getroot()
        body = root.find("body")
        self._senteces = [Sentence(x) for x in body.findall("S")]

    @property
    def sentences(self):
        return self._senteces


class Sentence:
    def __init__(self, element):
        self._words = [Word(x) for x in element.findall("W")]
        self._test_tree = self._build_tree()

    def _to_graph(self, solution):
        """
        creates graph with given weight vectors.
        graph is represented as it minimum_spinning_tree function requires
        """
        graph = [[[]]]
        for (i, word) in enumerate(self.words):
            other_words = [w for w in self._words if w != word]
            for (j, other_word) in enumerate(other_words):
                graph[i[j]] = solution.get_weight(word, other_word)
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

    def _build_tree(self):
        tree = []
        subtrees = UnionFind()
        for word in self._words:
            tree.append([word.id, self._find_parent(word).id])
        return tree

    def _find_parent(self, word):
        if word.parent != 0:
            return self._words[word.parent]
        else:
            return word

    @property
    def test_tree(self):
        return self._test_tree

    @property
    def words(self):
        return self._words


class Word:
    def __init__(self, element):
        self._word = element.text
        self._id = int(element.attrib["ID"]) - 1
        if element.attrib["DOM"] != "_root":
            self._parent = int(element.attrib["DOM"]) - 1
            self._features = element.attrib["FEAT"] + " " + element.attrib["LINK"]
        else:
            self._parent = self._id
            self._features = element.attrib["FEAT"]
        self._lemma = element.attrib["LEMMA"]

    @property
    def word(self):
        return self._word

    @property
    def lemma(self):
        return self._lemma

    @property
    def id(self):
        return self._id

    @property
    def parent(self):
        return self._parent

    @property
    def features(self):
        return self._features