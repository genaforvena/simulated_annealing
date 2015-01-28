from random import random
import math

__author__ = 'imozerov'

def anneal(sol):
    old_cost = cost(sol)
    T = 1.0
    T_min = 0.00001
    alpha = 0.99
    while T > T_min:
        i = 1
        while i <= 100:
            new_sol = neighbor(sol)
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
    # should calculate distance between my tree and training tree

def acceptance_probability(old_cost, new_cost, temperature):
    return math.exp((new_cost - old_cost)/temperature)

if __name__ == "__main__":
    pass
