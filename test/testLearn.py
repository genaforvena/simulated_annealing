import unittest
from language import *
from learn import *


class AddMissingFeaturesTest(unittest.TestCase):
    def test_add_missing_features(self):
        weights = {}
        sentence = Sentence(ElementTree.fromstring("<S><W DOM=\"2\" FEAT=\"A МН ИМ\" ID=\"1\" LEMMA=\"РУССКИЙ\" LINK=\"опред\">РУССКИЕ</W> <W DOM=\"_root\" FEAT=\"S МН МУЖ ИМ ОД\" ID=\"2\" LEMMA=\"АНГЛИЧАНИН\">АНГЛИЧАНЕ</W> </S>"))
        weights = add_missing_features(sentence, weights)
        self.assertIn("A МН ИМ опред", weights.keys())
        self.assertIn("S МН МУЖ ИМ ОД", weights.keys())


if __name__ == '__main__':
    unittest.main()