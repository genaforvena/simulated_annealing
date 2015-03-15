import os
from random import random
import math
import copy

from os import listdir
from os.path import isfile, join

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


def acceptance_probability(old_cost, new_cost, temperature):
    return math.exp((new_cost - old_cost) / temperature)

def anneal(sol):
    sentences = SentencesList()
    sentence = sentences.next()
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
            sentence = sentences.next()

        T *= alpha
    return sol, sol.cost


class SentencesList:
    def __init__(self):
        dates = [x for x in range(2003, 2014)]
        path_root = "/home/imozerov/Diploma/syntagrus/SynTagRus2014"
        self.files = []
        self.current_file_index = 0
        self.current_sentence_index = 0
        for i in dates:
            self.files.extend([path_root + "/" + str(i) + "/" + f for f in listdir(path_root + "/" + str(i)) if isfile(join(path_root + "/" + str(i), f))])
        self.current_document = TgtDocument(self.files[self.current_file_index])
        self.current_sentence = self.current_document.sentences[self.current_sentence_index]

    def next(self):
        self.current_sentence_index += 1
        if self.current_sentence_index > len(self.current_document.sentences) - 1:
            self.current_file_index += 1
            self.current_sentence_index = 0
            self.current_document = TgtDocument(self.files[self.current_file_index])
            if self.current_file_index > len(self.files) - 1:
                self.current_file_index = 0
                self.current_sentence_index = 0
                self.current_document = TgtDocument(self.files[self.current_file_index])
        return self.current_document.sentences[self.current_sentence_index]


if __name__ == "__main__":
    pass
