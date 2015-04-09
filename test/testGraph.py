import unittest
from xml.etree import ElementTree
from graphs import Graph
from language import Word, Sentence
from solution import Solution

__author__ = 'imozerov'


class TestGraph(unittest.TestCase):
    def test_minimum_spanning_tree(self):
        sentence_str = "<S CLASS=\"LF\" ID=\"1\">" \
                       "<W DOM=\"2\" FEAT=\"S ЕД МУЖ ИМ НЕОД\" ID=\"1\" LEMMA=\"ШАНХАЙ\" LINK=\"предик\">Шанхай</W> " \
                       "<W DOM=\"_root\" FEAT=\"V НЕСОВ ИЗЪЯВ НЕПРОШ ЕД 3-Л\" ID=\"2\" LEMMA=\"КАЗАТЬСЯ\">кажется</W>" \
                       "<W DOM=\"2\" FEAT=\"A ЕД МУЖ ТВОР\" ID=\"3\" LEMMA=\"НЕРЕАЛЬНЫЙ\" " \
                       "LINK=\"1-компл\">нереальным</W></S>"
        sentence = Sentence(ElementTree.fromstring(sentence_str))
        word1 = sentence.words[0]
        word2 = sentence.words[1]
        word3 = sentence.words[2]
        words = [word1, word2, word3]
        solution = Solution()
        solution.weights_map = {Solution.create_pair(word1.features, word2.features): 1,
                                Solution.create_pair(word2.features, word3.features): 1}
        graph_under_test = Graph(words, solution)

        self.assertEqual([[word1, word2, 1], [word2, word3, 1]], graph_under_test.minimum_spanning_tree())