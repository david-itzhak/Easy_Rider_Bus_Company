from nltk import sent_tokenize

text = input()
tokenized_copy_of_text = sent_tokenize(text)
print(tokenized_copy_of_text)