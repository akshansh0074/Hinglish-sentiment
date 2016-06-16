import TwitterSearch
import csv
from TwitterSearch import *
import pandas as pd
import re,collections
import itertools
#import matplotlib as mat
#import nltk 
from collections import Counter




def get_tweets(query, max_tweets):
    
    
    # takes a search term (query) and a max number of tweets to find
    # gets content from twitter and writes it to a csv bearing the name of your query
    maximum = max_tweets
    i = 0
    search = query

    with open(search+'.csv', 'wb') as outf:
        writer = csv.writer(outf)
        writer.writerow(['tweet'])
        try:
            tso = TwitterSearchOrder()
            tso.set_keywords([search])
            tso.set_language('hi') # English tweets only

            ts = TwitterSearch(
                consumer_key = 'Obd0yBbXKQmvASTQK9Dvj9Nta',
                consumer_secret = 'NChicM6KTLRnseNhaKEXgFhqQwfOWCNK4ZUNGWT87LBVDsoNQu',
                access_token = '516433587-p2aOT7o3iiecDgNN0BAgQJJUUhKq3Xb9rVj5gYpL',
                access_token_secret = 'sSaUgDJWzzMU5KhE9moR5IUSnuINiwtZ71brK5tb2SCa3'
            )

            for tweet in ts.search_tweets_iterable(tso):
                
                tweet_text = tweet['text'].strip().encode('ascii', 'ignore')
                tweet_text = ''.join(tweet_text.splitlines())
                print tweet_text
                
                

                writer.writerow([ tweet_text])
                i += 1
                if i > maximum:
                    return()

        except TwitterSearchException as e:
            print(e)

get_tweets('news',100)

try1 = pd.read_csv("news.csv")
print try1
# remove punctuations
def replace_it(tweet):
    tweet = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', tweet, flags=re.MULTILINE)
    return re.sub('[^A-Za-z]+', ' ', tweet)
try1['tweet'] = try1['tweet'].apply(lambda x: replace_it(x))

print try1

#spell check


def words(text): return re.findall('[a-z]+', text.lower()) 

def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model

NWORDS = train(words(file('hinglish.txt').read()))

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def edits1(word):
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
   inserts    = [a + c + b     for a, b in splits for c in alphabet]
   return set(deletes + transposes + replaces + inserts)

def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

def known(words): return set(w for w in words if w in NWORDS)

def correct(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    return max(candidates, key=NWORDS.get)

try1['tweet']  = try1['tweet'].apply(lambda x: correct(x))


# count words for each tweet
def count(text):
    tweety = []
    text = text.lower()
    tweety = text
    return Counter(text.split(" ")).items()

try1['counter'] = try1['tweet'].apply(lambda x: count(x))

## add to dictionary words most frequent
aks =Counter(" ".join(try1["tweet"]).split()).most_common(100)
print aks
