import nltk
from nltk import word_tokenize


sentence = str(input())  # input sentence
tokenized = word_tokenize(sentence)
tokens_list = nltk.pos_tag(tokenized)
verbs_list = []
for word, tag in tokens_list:
    if tag.startswith('V'):
        verbs_list.append(word)
print(verbs_list)