from googletrans import Translator


class PhraseTranslation:
    def __init__(self):
        self.translator = Translator(service_urls=['translate.google.com'])

    def get_translation(self, phrase):
        while True:
            try:
                translation = self.translator.translate(phrase, src='en', dest='pl')
                break
            except ConnectionError:
                return ["Network connection error."]
            except Exception:
                pass
        return translation.text
