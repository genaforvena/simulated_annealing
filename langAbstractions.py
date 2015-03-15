from xml.etree.ElementTree import Element, SubElement
from xml.etree import ElementTree

__author__ = 'imozerov'

# Check this tutorial http://effbot.org/zone/element.htm 

class TgtDocument:
    def __init__(self, filename):
        tree = ElementTree.parse(filename)
        root = tree.getroot()
        body = root.find("body")
        self._senteces = [Sentence(x) for x in body.findall("S")]

    @property
    def sentences(self):
        return self._senteces


class Sentence:
    def __init__(self, element):
        self._words = [Word(x) for x in element.findall("W")]

    @property
    def words(self):
        return self._words


class Word:
    def __init__(self, element):
        self._word = element.text
        if element.attrib["DOM"] != "_root":
            self._parent = int(element.attrib["DOM"])
            self._features = element.attrib["FEAT"] + " " + element.attrib["LINK"]
        else:
            self._parent = 0
            self._features = element.attrib["FEAT"]
        self._id = int(element.attrib["ID"])
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