import nltk
import TwitterSearch
import tweepy
import csv

from TwitterSearch import *


#Twitter API credentials
#consumer_key = "Obd0yBbXKQmvASTQK9Dvj9Nta"
#consumer_secret = "NChicM6KTLRnseNhaKEXgFhqQwfOWCNK4ZUNGWT87LBVDsoNQu"
#access_key = "516433587-p2aOT7o3iiecDgNN0BAgQJJUUhKq3Xb9rVj5gYpL"
#access_secret = "sSaUgDJWzzMU5KhE9moR5IUSnuINiwtZ71brK5tb2SCa3"
tweets = []
 #write the csv	
 
	#writer.writerow(["user","time","tweet"])

try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['JNU'])
    tso.set_language('hi') # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = "Obd0yBbXKQmvASTQK9Dvj9Nta",
        consumer_secret = "NChicM6KTLRnseNhaKEXgFhqQwfOWCNK4ZUNGWT87LBVDsoNQu",
        access_token = "516433587-p2aOT7o3iiecDgNN0BAgQJJUUhKq3Xb9rVj5gYpL",
        access_token_secret = "sSaUgDJWzzMU5KhE9moR5IUSnuINiwtZ71brK5tb2SCa3"
     )
  
     
    for tweet in ts.search_tweets_iterable(tso):
    	time = tweet['created_at']
        user = tweet['user']['screen_name'].encode("ASCII",errors='ignore')
        tweet_text = tweet['text'].strip().encode('ascii', 'ignore')
        tweet_text = ''.join(tweet_text.splitlines())
        #print( '@%s tweeted: %s' % ( tweet['user']['screen_name'].encode("ASCII",errors='ignore'), tweet['text'].encode("ASCII",errors='ignore') ) )
        tweets.append({'id':user, 'text': tweet_text,'created_at':time })
        
    for i in tweets:
    	print tweets[i]
                    
	#outtweets = [[tweets[0],tweets[1], tweets[2]] for tweet in tweets]
	 #outtweets = [user,time, tweet_text] 
	#with open('newa_tweets.csv', 'wb') as f:
		#writer = csv.writer(f)   
		#writer.writerow(["id","created_at","text"])  
		#writer.writerows(outtweets)
	
	#pass


except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)

