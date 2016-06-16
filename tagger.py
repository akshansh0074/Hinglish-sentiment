from nltk.corpus import indian

from nltk.corpus import brown
from nltk import UnigramTagger

import sys
reload(sys)
from nltk.tag import tnt
from nltk.tokenize import sent_tokenize, word_tokenize


tnt_pos_tagger = tnt.TnT()
tnt_pos_tagger.train(train_data_hindi)
sys.setdefaultencoding("utf-8")
#english tags
train_sents = brown.tagged_sents()
#hindi tags

train_data_hindi = indian.tagged_sents('hindi.pos')[:-1] //used for training 

tnt_pos_tagger.train(train_data_hindi)

def english_tag(eng_tweet):
	word_features = []
	eng_tweet =nltk.word_tokenize(eng_tweet)
	for i,j in nltk.pos_tag(eng_tweet):
    if j in ['JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS']: 
        word_features.append(i)


	rating = 0

	
	 

def hindi_tag(hindi_tweet):
	return nltk.word_tokenize(hindi_tweet)


def hinglish_tag(hinglish_tweet):
	return

def tagger(tweet):
	if(tweet[1] == 'en'):
		return english_tag(tweet[0])
	elif(tweet[1] =='hi'):
		return hindi_tag(tweet[0])
	else return hinglish_tag(tweet[0])

word_features = []

for i,j in nltk.pos_tag(eng_tweet):
    if j in ['JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS']: 
        word_features.append(i)

rating = 0

for i in word_features:
    with open('words.txt', 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if i == row[0]:
                print i, row[1]
                if row[1] == 'pos':
                    rating = rating + 1
                elif row[1] == 'neg':
                    rating = rating - 1


hindi_pos = 


