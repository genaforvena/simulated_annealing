import pickle
from random import random
import math
from language import SentencesList

from solution import Solution

SOLUTION = "solution.p"

__author__ = 'imozerov'


def anneal(solution):
    temperature_current = 1.0
    temperature_min = 0.00001
    alpha = 0.99

    sentences = SentencesList()
    sentence = sentences.next()
    old_cost = solution.cost(sentence)
    while temperature_current > temperature_min:
        i = 1
        while i <= 1000:
            new_solution = solution.neighbor()
            new_cost = new_solution.cost(sentence)
            accept_probability = acceptance_probability(old_cost, new_cost, temperature_current)
            if accept_probability > random():
                solution = new_solution
                old_cost = new_cost
            i += 1
            sentence = sentences.next()
        temperature_current *= alpha
    return solution, solution.cost


def acceptance_probability(old_cost, new_cost, temperature):
    return math.exp((new_cost - old_cost) / temperature)

if __name__ == "__main__":
    (solution, solution_cost) = anneal(Solution())
    pickle.dump(solution, open(SOLUTION, "wb"))
