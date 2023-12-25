import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import spacy

text = "Hello there! This is an example text. NLTK can split it into sentences."
sentences = sent_tokenize(text)
words = word_tokenize(text)
print(words)

print("-----------------")

nlp = spacy.load('en_core_web_sm')
text = "Google was founded by Larry Page and Sergey Brin while they were students at Stanford University."
doc = nlp(text)
for ent in doc.ents:
    print(ent.text, ent.label_)

print("-------------------")

nlp_spa = spacy.load('es_core_news_sm')
text = "Pedro Sánchez será investido con los votos de Junts y Puigdemont."
doc = nlp_spa(text)
for ent in doc.ents:
    print(ent.text, ent.label_)

