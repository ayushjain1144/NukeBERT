print('hellp')
import re


import nltk.data


tokenizer = nltk.data.load('tokinizers/punkt/english.pickle')
file = open('out1.txt', 'r')

text = file.read()

text = text.replace('\n', ' ')

print('\n-----------\n'.join(tokenizer.tokenize(text)))

#text = "\n".join(token.string.strip() for token in doc.sents)

file1 = open('mod.txt', 'w')

file1.write(text)

file.close()
file1.close()




