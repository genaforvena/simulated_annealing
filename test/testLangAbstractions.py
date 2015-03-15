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
        self.assertEqual(8, tgt_file.sentences[0].words[7].id)
        self.assertEqual(7, tgt_file.sentences[0].words[7].parent)
        self.assertEqual("S ЕД МУЖ ДАТ ОД предл", tgt_file.sentences[0].words[7].features)
        self.assertEqual("ОН", tgt_file.sentences[0].words[7].lemma)

if __name__ == '__main__':
    unittest.main()
