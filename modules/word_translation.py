class WordTranslation:
    def __init__(self):
        self.api = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"

    def get_translation(self, word):
        return "There will be a translation."