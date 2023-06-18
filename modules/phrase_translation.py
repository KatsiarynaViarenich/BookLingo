from googletrans import Translator


class PhraseTranslation:
    def __init__(self):
        self.translator = Translator(service_urls=['translate.google.com'])

    def get_translation(self, phrase):
        translation = self.translator.translate(phrase, src='en', dest='pl')
        return translation.text
