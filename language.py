from xml.etree import ElementTree

__author__ = 'imozerov'

class TgtDocument:
    def __init__(self, filename):
        tree = ElementTree.parse(filename)
        root = tree.getroot()
        body = root.find("body")
        self._sentences = [Sentence(x) for x in body.findall("S")]

    @property
    def sentences(self):
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