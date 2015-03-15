from langAbstractions import TgtDocument

__author__ = 'imozerov'

import unittest


class TestTgtDocument(unittest.TestCase):
    def test_create_sentences_from_file(self):
        tgt_file = TgtDocument("test_sentence")
        self.assertIsNotNone(tgt_file)
        self.assertEqual(1, len(tgt_file.sentences))
        self.assertEqual(10, len(tgt_file.sentences[0].words))
        self.assertEqual("нему", tgt_file.sentences[0].words[7].word)
        self.assertEqual(7, tgt_file.sentences[0].words[7].id)
        self.assertEqual(6, tgt_file.sentences[0].words[7].parent)
        self.assertEqual("S ЕД МУЖ ДАТ ОД предл", tgt_file.sentences[0].words[7].features)
        self.assertEqual("ОН", tgt_file.sentences[0].words[7].lemma)
        tree_from_txt = [[1, 2], [2, 2], [3, 2], [4, 5], [5, 2], [6, 5], [7, 6], [8, 7], [9, 6], [10, 9]]
        tree_should_be = []
        for pair in tree_from_txt:
            tree_should_be.append([(x - 1) for x in pair])
        self.assertListEqual(tree_should_be,
                             tgt_file.sentences[0].tree)


if __name__ == '__main__':
    unittest.main()
