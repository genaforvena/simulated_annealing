from random import random
import math
import copy

from langAbstractions import *

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

    def cost(self, sentence):
        """
        Returns cost of given sentence with this solution
        Tree distance algorithm needs to be implemented
        """
        solution_tree = sentence.minimum_spanning_tree(self)
        distance = 0
        for node in solution_tree:
            if node not in sentence.test_tree:
                distance += 1
        return distance

    @property
    def weights_map(self):
        return self._weights_map

    @weights_map.setter
    def weights_map(self, new_map):
        self._weights_map = new_map

    def neighbor(self):
        """
        maybe change to not random but some close value
        """
        neighbor = copy.deepcopy(self)
        neighbor.weights_map[random.choice(self._weights_map.keys())] = random()
        return neighbor

    def get_weight(self, word, other_word):
        """"
        returns weight of given word pair
        """""
        key = self._create_pair(word.features + other_word.features)
        if not self.weights_map[key]:
            return random(1)
        return self.weights_map[key]

    @staticmethod
    def _create_pair(features1, features2):
        if features1 > features2:
            return features1 + features2
        else:
            return features2 + features1


def anneal(sol):
    # TODO read sentence
    sentence = None
    old_cost = sol.cost(sentence)
    T = 1.0
    T_min = 0.00001
    alpha = 0.99
    while T > T_min:
        i = 1
        while i <= 1000:
            new_sol = sol.neighbor()
            new_cost = new_sol.cost(sentence)
            ap = acceptance_probability(old_cost, new_cost, T)
            if ap > random():
                sol = new_sol
                old_cost = new_cost
            i += 1
            # TODO read next sentence
        T *= alpha
    return sol, sol.cost


def acceptance_probability(old_cost, new_cost, temperature):
    return math.exp((new_cost - old_cost) / temperature)


if __name__ == "__main__":
    pass
