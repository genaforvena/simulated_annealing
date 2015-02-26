__author__ = 'imozerov'


class Sentence:
    def __init__(self, string):
        self._string = string
        self._words = self._parse_words()

    @property
    def words(self):
        return self._words

    def _parse_words(self):
        pass


class Word:
    def __init__(self, string):
        self._string = string
        self._word = self._parse_word()
        self._features = self._parse_features()

    @property
    def features(self):
        return self._features

    @property
    def features(self):
        return self._word


class Features:
    def __init__(self, string):
        self._string = string
        self._features = string

    @property
    def features(self):
        return self._features