from nltk import sent_tokenize, regexp_tokenize

pattern = "[A-z']+"
text = input()
index = int(input())
sent_tokenize_text = sent_tokenize(text)
tokenized_sentence = regexp_tokenize(sent_tokenize_text[index], pattern)
print(tokenized_sentence)