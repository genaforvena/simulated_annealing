import pickle
from random import random
import math
import language
from networkx import *
from zss import *

SOLUTION_FILE = "solution.p"

__author__ = 'imozerov'


def anneal():
    distance = 9999999
    weights = {}

    temperature_current = 1.0
    temperature_min = 0.00001
    alpha = 0.99

    sentences = language.SentencesList()
    sentence = sentences.next()

    while temperature_current > temperature_min:
        i = 1
        while i <= 100:
            neighbour_weights = create_neighbour(weights)
            mst = maximum_spanning_tree(sentence, neighbour_weights)
            neighbour_distance = calculate_distance(mst, sentence.test_tree)
            accept_probability = acceptance_probability(distance, neighbour_distance, temperature_current)
            if accept_probability > random():
                weights = neighbour_weights
            i += 1
            sentence = sentences.next()
        temperature_current *= alpha
    return weights


def maximum_spanning_tree(sentence, weights):
    graph = nx.Graph()
    for word1 in sentence.words:
        for word2 in sentence.words:
            if word1.id != word2.id:
                if word1.features + word2.features in weights:
                    graph.add_edge(word1.id, word2.id, weight=weights[word1.features + word2.features])
                else:
                    graph.add_edge(word1.id, word2.id, weight=1)
                    weights[word1.features + word2.features] = 1

    return nx.maximum_spanning_tree(graph)


def calculate_distance(tree1, tree2):
    edges = [[x, y] for x, y in list(tree1.edges())]

    uncommonElemsCount = 0
    for edge in edges:
        if edge not in tree2:
            uncommonElemsCount += 1
    return uncommonElemsCount


def create_neighbour(weights_dict):
    for (k, v) in weights_dict.items():
        if random() < 0.1:
            weights_dict[k] = random()
    return weights_dict


def acceptance_probability(old_cost, new_cost, temperature):
    return math.exp((new_cost - old_cost) / temperature)

if __name__ == "__main__":
    weights_res = anneal()
    pickle.dump(weights_res, open(SOLUTION_FILE, "wb"))
