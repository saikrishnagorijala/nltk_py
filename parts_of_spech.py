import nltk
from nltk import word_tokenize

DATA = open('data.txt', 'r').read()
words = word_tokenize(DATA)
from nltk.corpus import stopwords
import string
stop_words = set(stopwords.words('english'))
stop_words = stop_words.union(string.punctuation)
cleanwords = [w for w in words if not w in stop_words]
from nltk import pos_tag
tageedWords = pos_tag(cleanwords)
print(tageedWords)
print(nltk.help.upenn_tagset())

i=0
for word in tageedWords:
    i = i + 10
    print(str(i)+" : "+str(word))