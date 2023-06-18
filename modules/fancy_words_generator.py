import nltk


class FancyWordsGenerator:
    def __init__(self, word_list):
        self.word_list = word_list

    def get_fancy_words(self, text, num_words=10):
        words = nltk.word_tokenize(text.lower())
        word_freq = nltk.FreqDist(words)
        common_words = word_freq.most_common()
        uncommon_words = [word for word, freq in common_words if word not in nltk.corpus.words.words()]
        return uncommon_words[:num_words]