#import nltk
import pandas as pd
import re
import itertools
import pickle
import csv
#import matplotlib as mat
from collections import Counter

try1 = pd.read_csv("6Dec.csv")

print type(try1)
def replace_it(tweet):
    #tweet = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', tweet, flags=re.MULTILINE)
    tweet = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet)
    return re.sub('[^A-Za-z]+', ' ', tweet)
try1['tweetText'] = try1['tweetText'].apply(lambda x: replace_it(x))

#try1['count_word'] = graphlab.text_analytics.count_words(try1['text'])

def count(text):
	tweety = []
	text = text.lower()
	tweety = text
	return Counter(text.split(" ")).items()

#try1['counter'] = try1['tweetText'].apply(lambda x: count(x))
#print try1['counter']

def max_freq(count):

	c= Counter(count.split(" ")).items()
	
	return c
#result = []
#result = result +try1['tweet'].apply(lambda x:max_freq(x))

#print max_freq()

#for text in try1['tweet']:
	#max_frequency=Counter(text.split(" ")).items()
	
#print len(max_frequency)
wordcount={}
#for word in try1['tweet']:
	#word  = word.split()
    	#if word not in wordcount:
        	#wordcount[word] = 1
    	#else:
        	#wordcount[word] += 1
#for k,v in wordcount.items():
    #print k, v
aks =Counter(" ".join(try1["tweetText"]).split()).most_common(100)
print aks

print type(aks)
with open('count.csv', 'w') as f:
	   writer = csv.writer(f, delimiter=',')
	   writer.writerows(aks)
#outfile.write("\n".join(aks))



#print type(max_frequency)

#for word, count in max_frequency:
        #print("{0}: {1}".format(word, count))
#itertools.islice(wordcount, 0, 100) 

