import unittest
from language import SentencesList

__author__ = 'imozerov'


class TestSentencesList(unittest.TestCase):
    def test_next(self):
        sentences = SentencesList()
        for i in range(10000):
            sentences.next()
