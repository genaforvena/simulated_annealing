import unittest
from solution import SentencesList

__author__ = 'imozerov'

class TestSentencesList(unittest.TestCase):
    def test_next(self):
        sentences = SentencesList()
        for i in range(100):
            sentences.next()
