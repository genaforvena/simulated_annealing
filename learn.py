import pickle
from random import random
import math
import language

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
    weights = add_missing_features(sentence, weights)

    while temperature_current > temperature_min:
        i = 1
        while i <= 100:
            neighbour_weights = create_neighbour(weights)
            mst = maximum_spanning_tree(sentence)
            neighbour_distance = calculate_distance(mst, sentence.test_tree)
            accept_probability = acceptance_probability(distance, neighbour_distance, temperature_current)
            if accept_probability > random():
                weights = neighbour_weights
            i += 1
            sentence = sentences.next()
            weights = add_missing_features(sentence)
        temperature_current *= alpha
    return weights


def add_missing_features(sentence, weights):
    for feature in [x.features for x in sentence.words]:
        if weights.get(feature) is None:
            weights[feature] = 0

    return weights

def maximum_spanning_tree(sentence, weights):
    return


def calculate_distance(tree1, tree2):
    return 0


def create_neighbour(weights_dict):
    for (k, v) in weights_dict:
        if random() < 0.1:
            weights_dict[k] = random()
    return weights_dict


def acceptance_probability(old_cost, new_cost, temperature):
    return math.exp((new_cost - old_cost) / temperature)

if __name__ == "__main__":
    weights_res = anneal()
    pickle.dump(weights_res, open(SOLUTION_FILE, "wb"))
