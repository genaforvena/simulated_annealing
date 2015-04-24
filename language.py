from xml.etree import ElementTree
from os import listdir
from os.path import isfile, join

__author__ = 'imozerov'


class SentencesList:
    def __init__(self):
        path_root = "/home/imozerov/Diploma/syntagrus/SynTagRus2014"
        dates = [x for x in range(2003, 2014)]
        self.files = []
        self.current_file_index = 0
        self.current_sentence_index = 0
        for i in dates:
            self.files.extend([path_root + "/" + str(i) + "/" + f for
                               f in listdir(path_root + "/" + str(i)) if isfile(join(path_root + "/" + str(i), f))])
        self.current_document = TgtDocument(self.files[self.current_file_index])
        self.current_sentence = self.current_document.sentences[self.current_sentence_index]

    def next(self):
        # TODO refactor to override __iter__
        self.current_sentence_index += 1
        try:
            if self.current_sentence_index > len(self.current_document.sentences) - 1:
                self.current_file_index += 1
                self.current_sentence_index = 0
                self.current_document = TgtDocument(self.files[self.current_file_index])
                if self.current_file_index > len(self.files) - 1:
                    self.current_file_index = 0
                    self.current_sentence_index = 0
                    self.current_document = TgtDocument(self.files[self.current_file_index])
        except:
            self.current_file_index = 0
            self.current_sentence_index = 0
            self.current_document = TgtDocument(self.files[self.current_file_index])
        return self.current_document.sentences[self.current_sentence_index]

class TgtDocument:
    def __init__(self, filename):
        tree = ElementTree.parse(filename)
        root = tree.getroot()
        body = root.find("body")
        self._sentences = [Sentence(x) for x in body.findall("S")]

    @property
    def sentences(self):
        return self._sentences

    def __str__(self, *args, **kwargs):
        return self._sentences


class Sentence:
    def __init__(self, element):
        self._words = [Word(x) for x in element.findall("W")]
        self._test_tree = self._build_tree()

    def _build_tree(self):
        tree = []
        for word in self._words:
            tree.append([word.id, self._find_parent(word).id])
        return tree

    def _find_parent(self, word):
        if word.parent != 0:
            return self._words[word.parent]
        else:
            return word

    @property
    def test_tree(self):
        return self._test_tree

    @property
    def words(self):
        return self._words

    def __str__(self, *args, **kwargs):
        return self._words


class Word:
    def __init__(self, element):
        self._word = element.text
        self._id = int(element.attrib["ID"]) - 1
        if element.attrib["DOM"] != "_root":
            self._parent = int(element.attrib["DOM"]) - 1
            self._features = element.attrib["FEAT"] + " " + element.attrib["LINK"]
        else:
            self._parent = self._id
            self._features = element.attrib["FEAT"]
        if "LEMMA" in element.attrib:
            self._lemma = element.attrib["LEMMA"]

    @property
    def word(self):
        return self._word

    @property
    def lemma(self):
        return self._lemma

    @property
    def id(self):
        return self._id

    @property
    def parent(self):
        return self._parent

    @property
    def features(self):
        return self._features

    def __str__(self, *args, **kwargs):
        return self.word + " " + str(self.id)

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.id < other.id

    def __hash__(self):
        return hash(self.id)

