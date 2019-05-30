import nltk
from nltk import word_tokenize

DATA = open('data.txt', 'r').read()

#inclusive of stop words
'''
words = word_tokenize(DATA)

print("No of Words : "+str(len(words)))

i=0
for word in words:
    i=i+1
    print("sentence ("+str(i)+") : "+str(word))
    '''

#exclusive of stopwords
words = word_tokenize(DATA)
from nltk.corpus import stopwords
import string
stop_words = set(stopwords.words('english'))
stop_words = stop_words.union(string.punctuation)
cleanwords = [w for w in words if not w in stop_words]


print("No of Words with stopwords : "+str(len(words)))
print("No of Words w/o  stopwords : "+str(len(cleanwords)))
i=0
for word in cleanwords:
    i=i+1
    print("sentence ("+str(i)+") : "+str(word))


