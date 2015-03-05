__author__ = 'imozerov'

import elementtree.ElementTree import Element, SubElement, ElementTree

# Check this tutorial http://effbot.org/zone/element.htm 

class TgtDocument:
	def __init__(self, filename):
		tree = ElementTree(file=filename)
		xml = Element("xml")
		body = SubElement(xml, "body")	
		self._senteces = [Sentence(x) for x in body.findall("S")]
	
	@property
	def sentences(self):
		return self._senteces
	

class Sentence:
    def __init__(self, element):
        self._words = [Word(x) for x in string.findall("W")]

    @property
    def words(self):
        return self._words


class Word:
    def __init__(self, element):
        self._word = element.text
        self._features = self._parse_features()

    @property
    def features(self):
        return self._features

    @property
    def features(self):
        return self._word


class Features:
    def __init__(self, element):
        self._features = string

    @property
    def features(self):
        return self._features