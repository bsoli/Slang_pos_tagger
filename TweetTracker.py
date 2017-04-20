__author__ = 'benso_000'
import tweepy
import codecs


consumer_key = 'CWJs1F0V4wsap16ZpG6yP7BDA'
consumer_secret = 'kjBshHyajTPpADxN6rQieevpOwjOH1hEOmOCURhpzvIG71pr4G'
access_token = '187067949-za9sNmm0MyTQHUlmv2j7D0tFxWd15uasr3nfh4ao'
access_token_secret = '8uWuroX8ybkJVs0j0yu1UJ92LRq3Z6J3s5rttMIqvosGV'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)
tweets = []
friend_ids = []
statuses = []
user = api.me()
#finds all the ids for the user's friends
for friend in api.friends_ids(user):
    friend_ids.append(friend)
#adds a list of their most recent statuses to a list 
for i in friend_ids:
    statuses.append(api.user_timeline(i))
#adds the text version of each tweet to a list
for timeline in statuses:
    for tweet in timeline:
        tweets.append(tweet.text)
        
f = open("slang.txt", "w")
#converts the unicode text to ascii and writes the text to a file
for tweet in tweets:
    f.write(tweet.encode('ascii', 'ignore').decode('ascii')+'\n')
f.close()
        
