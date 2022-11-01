from nltk import regexp_tokenize

sentence = input()
index = int(input())
pattern = "[a-zA-Z]+"
tokenized_copy_of_text = regexp_tokenize(sentence, pattern)
print(tokenized_copy_of_text[index])