import wikipedia

def search_wikipedia(query):
    try:
        results = wikipedia.search(query)
        if results:
            page = wikipedia.page(results[0])
            return page.summary
    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options
        if options:
            page = wikipedia.page(options[0])
            return page.summary
    except wikipedia.exceptions.PageError:
        return "No Wikipedia page found."
    except ConnectionError:
        return "Network connection error."