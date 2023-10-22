from deep_translator import GoogleTranslator


class PhraseTranslation:
    def __init__(self, target="pl"):
        self.translator = GoogleTranslator(source="auto", target=target)

    def get_translation(self, phrase):
        translated = self.translator.translate(phrase)
        return translated
