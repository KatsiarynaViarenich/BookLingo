import random

import nltk


def get_fancy_words(text, num_words=10):
    tokens = nltk.word_tokenize(text)
    long_words = {word for word in tokens if len(word) > 8}
    num_words = min(num_words, len(long_words))
    fancy_words = random.sample(long_words, num_words)
    return fancy_words
