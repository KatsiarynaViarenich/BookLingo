from googletrans import Translator


class PhraseTranslation:
    def __init__(self):
        self.translator = Translator(service_urls=["translate.google.com"])

    def get_translation(self, phrase):
        while True:
            try:
                translation = self.translator.translate(phrase, src="en", dest="pl")
                break
            except ConnectionError:
                print("ИНЕТ ПРОПАЛ")
                return ["Network connection error."]
            except Exception as e:
                print(e)
                pass
        return translation.text
