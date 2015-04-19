import pickle
from graphs import Graph
from language import SentencesList
import learn
from solution import Solution

__author__ = 'imozerov'


def predict(solution):
    sentences = SentencesList()
    for sentence in sentences:
        print(Graph(sentence, solution).minimum_spanning_tree())

if __name__ == "__main__":
    solution = Solution(pickle.load(open(learn.SOLUTION, "rb")))
    predict(solution)