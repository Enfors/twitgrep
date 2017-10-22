#!/usr/bin/env python3

"""Classes for words and sentences.
"""

import doctest


class Word(object):
    # """Store a word along with it's type.

    # >>> word = Word("fnurgle")
    # >>> word
    # Word("fnurgle", word_type=1)
    # >>> print(word)
    # fnurgle

    # >>> word2 = Word("http://www.github.com", Word.TYPE_URL)
    # >>> word2
    # Word("http://www.github.com", word_type=2)
    # >>> print(word2)
    # http://www.github.com
    # """

    TYPE_WORD = 1
    TYPE_URL = 2

    def __init__(self, word_text, word_type=TYPE_WORD):
        self.word_text = word_text
        self.word_type = word_type

    def __repr__(self):
        return 'Word("%s", word_type=%d)' % (self.word_text, self.word_type)

    def __str__(self):
        return self.word_text

    def __len__(self):
        return len(self.word_text)


class Sentence(list):
    # """Store a sentence in the form of a list of words.

    # >>> sentence = Sentence(["some", "words"])
    # >>> " ".join(sentence)
    # 'some words'
    # """

    pass


def normalize(text):
    """Return a normalized copy of text.
    """

    text = normalize_whitespace(text)

    return text


def split_sentences(text):
    """Attempt to split a text into sentences.
    """

    text = normalize_whitespace(text)

    sentences = [sentence.strip() for sentence in text.split(". ")]

    sentences[-1] = sentences[-1].rstrip(".")

    return sentences


def make_ngrams(sentence, n):
    """Make n-grams from a normalized sentence.
    """

    words = sentence.split(" ")

    num_words = len(words)
    index = 0
    ngram_list = []

    while index + n <= num_words:
        ngram = words[index:index + n]
        ngram_list.append(ngram)
        index = index + 1

    return ngram_list


def normalize_and_split_sentences(text):
    """Return normalized sentences.

    >>> normalize_and_split_sentences("Foo bar. Another small sentence.")
    ['Foo bar', 'Another small sentence']
    >>> normalize_and_split_sentences(" Foo bar. Another  small sentence.")
    ['Foo bar', 'Another small sentence']
    >>> normalize_and_split_sentences("Foo bar . Another  small sentence.")
    ['Foo bar', 'Another small sentence']
    """

    text = normalize(text)
    sentences = split_sentences(text)

    return sentences


def normalize_whitespace(text):
    """Return a copy of text with one space between all words, with all
    newlines and tab characters removed.

    >>> print(normalize_whitespace("some text"))
    some text
    >>> print(normalize_whitespace(" some text "))
    some text
    >>> print(normalize_whitespace(" some   text"))
    some text
    >>> print(normalize_whitespace('\t\tsome text'))
    some text
    >>> print(normalize_whitespace("  some       text "))
    some text
    """

    new_text = text.replace("\n", " ")
    new_text = new_text.replace("\r", "")
    new_text = new_text.replace("\t", " ")

    words = [word.strip() for word in new_text.split(" ") if len(word) > 0]
    new_text = " ".join(words)
    return new_text


def demo():
    """Demonstrate the functionality in action.
    """

    import textwrap

    text = """
This is some text, split into several sentences over a number
of lines. Let's see what we can do with it. It's still a bit
short though, so I should probably make it longer by adding
more and more nonsense that noone wants to read. But that's\r\n
okay, since it's not meant to be read by humans.\r\n

The most merciful thing in the world, I think, is the human
mind's inability to correlate all its contents.

That is not dead which can eternal lie,
and with strange aeons, even death may die.
"""
    sentences = normalize_and_split_sentences(text)

    for sentence in sentences:
        print("%s." % "\n".join(textwrap.wrap("  " + sentence)))

    print("\nbi-grams:")

    ngrams = make_ngrams(sentences[0], 2)

    for ngram in ngrams:
        print(ngram)

    print("\n3-grams:")

    ngrams = make_ngrams(sentences[0], 3)

    for ngram in ngrams:
        print(ngram)

    print("\n4-grams:")

    ngrams = make_ngrams(sentences[0], 4)

    for ngram in ngrams:
        print(ngram)


if __name__ == "__main__":
    demo()
    doctest.testmod()