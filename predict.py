import pickle
from graphs import Graph
from language import SentencesList
import learn
from solution import Solution

__author__ = 'imozerov'


def predict(solution):
    sentences = SentencesList()
    for i in range(1000):
        try:
            sentence = sentences.next()
            print(sentence.test_tree)
            graph = Graph(sentence, solution)
            print(graph.maximum_spanning_tree())
        except:
            pass

if __name__ == "__main__":
    solution = Solution(pickle.load(open(learn.SOLUTION, "rb")))
    predict(solution)