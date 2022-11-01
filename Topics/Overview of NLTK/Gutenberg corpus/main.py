# Don't download gutenberg corpus. Just import it
from nltk.corpus import gutenberg

number = int(input())  # a row number of a sentence in Gutenberg corpus
print(gutenberg.sents("whitman-leaves.txt")[number])
