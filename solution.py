import copy
from random import random, choice

from graphs import Graph

__author__ = 'imozerov'


class Solution:
    """
    Object with weights map.
    Map contains names of pairs as keys and weights as values
    This object is able to create it's neighbour by
    randomly changing one of weights.
    """

    def __init__(self, weights_map={}):
        self._weights_map = weights_map

    def cost(self, sentence):
        """
        Returns cost of given sentence with this solution
        """
        solution_tree = Graph(sentence, self).maximum_spanning_tree()
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
        for weight in range(random(neighbor.count())):
            neighbor.weights_map[choice(list(self._weights_map.keys()))] = random()
        return neighbor

    def get_weight(self, word, other_word):
        """"
        returns weight of given word pair
        """""
        key = self.create_pair(word.features, other_word.features)
        if key not in self.weights_map.keys():
            self._weights_map[key] = random()
            return self._weights_map[key]
        return self.weights_map[key]

    @staticmethod
    def create_pair(features1, features2):
        if features1 > features2:
            return features1 + features2
        else:
            return features2 + features1
