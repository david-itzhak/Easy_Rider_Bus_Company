from nltk.tokenize import regexp_tokenize

sentence = input()
pattern = "[A-z'-]+"
tokenized_copy_of_text = regexp_tokenize(sentence, pattern)
print(tokenized_copy_of_text)
