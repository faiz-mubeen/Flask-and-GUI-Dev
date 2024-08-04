import paralleldots
paralleldots.set_api_key('Your API key')

def ner(text):
    ner = paralleldots.ner(text)
    return ner

def sentiment(text):
    sen= paralleldots.sentiment(text)
    return sen