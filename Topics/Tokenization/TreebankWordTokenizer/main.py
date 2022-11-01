from nltk import TreebankWordTokenizer

sentence = input()
tbw = TreebankWordTokenizer()
tokenized_copy_of_text = tbw.tokenize(sentence)
print(tokenized_copy_of_text)