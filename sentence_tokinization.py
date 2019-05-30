import nltk
from nltk import sent_tokenize

DATA = open('data.txt', 'r').read()
sentences = sent_tokenize(DATA)

print("No of Sentences : "+str(len(sentences)))

i=0
for sentence in sentences:
    i=i+1
    print("sentence ("+str(i)+") : "+str(sentence))