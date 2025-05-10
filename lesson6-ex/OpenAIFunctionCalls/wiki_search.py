import wikipedia


def wiki_search(wiki_search_words):
    """Returns Wikipedia summary by keywords"""
    print("[wiki_search] param: " + wiki_search_words)
    wikipedia.set_lang("it")
    return wikipedia.summary(wiki_search_words)
