class PhraseTranslation:
    def __init__(self):
        self.api = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"

    def get_translation(self, phrase):
        return "There will be a translation."