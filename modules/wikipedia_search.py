import wikipedia


class WikipediaSearch:
    def __init__(self):
        pass

    def search_wikipedia(self, query):
        try:
            results = wikipedia.search(query)
            if results:
                page = wikipedia.page(results[0])
                return page.content
        except wikipedia.exceptions.DisambiguationError as e:
            options = e.options
            if options:
                page = wikipedia.page(options[0])
                return page.content
        except wikipedia.exceptions.PageError:
            return "No Wikipedia page found."