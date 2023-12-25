import spacy
import nltk
from nltk.tokenize import word_tokenize

nlp = spacy.load('es_core_news_sm')

def tokenize_(sentence):
    tokens = word_tokenize(sentence)
    doc = nlp(" ".join(tokens))
    max_token_length = max(len(token.text) for token in doc)

    for token in doc:
        token_text = token.text.ljust(max_token_length)
        print(f"Token: {token_text}  POS Tag: {token.pos_}")
    print()

tokenize_("la casa es grande y hermosa")
tokenize_("Pedro Sánchez probablemente será investido con los votos de Junts, aunque sin duda la amnistía será muy cuestionada.")
