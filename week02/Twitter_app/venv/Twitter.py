import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import Cursor
from Crendentials import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textblob import TextBlob
import re

class TwitterClient():
    def __init__(self, other_twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_app()
        self.twitter_client =API(self.auth)
        self.twitter_user = other_twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client
        
    def get_user_timeline_tweets(self, number):
        tweets = []
        for tweet in Cursor (self.twitter_client.user_timeline, id=self.twitter_user).items(number):
            tweets.append(tweet)
        return tweets

    def get_friend_list (self, number_of_friends):
        friend_list = []
        for friend in Cursor(self.twitter_client.friends, id=self.twitter_user).items(number_of_friends):
            friend_list.append(friend)
        return friend_list

    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets = []
        for tweet in Cursor(self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets


class TwitterAuthenticator():
    def authenticate_app(self):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        return auth


class TwitterListener (StreamListener):

    def __init_ (self, my_tweets):
        self.my_tweets = my_tweets

    def on_data (self, data):
        try:
            print (data)
            with open (my_tweets, "a") as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print ("Error on data: %s" %str(e))
        return True

    def on_error (self, status):
        if status == 420:
            return False
        print (status)


class TwiterStreamer():

    def __init__ (self):
        self.twitter_authenticator = TwitterAuthenticator()

    def stream_tweets(self, my_tweets, hashtag_list):
        listener = TwitterListener()
        auth = self.twitter_authenticator.authenticate_app()
        stream = Stream(auth, listener)
        stream.filter(track=hashtag_list)

class Tweet_analyzer():
    def __init__(self, other_twitter_user=None):
        self.twitter_user = other_twitter_user

    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def analyse_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        if analysis.sentiment.polarity >0:
            return 1
        elif analysis.sentiment.polarity ==0:
            return 0
        else:
            return -1

    def tweets_to_df(self, tweets):
        df = pd.DataFrame([tweet.text for tweet in tweets], columns = ["Tweets"])
        df["id"]= np.array([tweet.id for tweet in tweets])
        df["length"]= np.array([len(tweet.text) for tweet in tweets])
        df["date"]= np.array([tweet.created_at for tweet in tweets])
        df["source"]= np.array([tweet.source for tweet in tweets])
        df["likes"]= np.array([tweet.favorite_count for tweet in tweets])
        df["retweet"]= np.array([tweet.retweet_count for tweet in tweets])
        return df

        time_likes = pd.Series(data=df["likes"].values, index=df["date"])
        time_likes.plot(figsize=[16, 4], label= "likes", legend = True)

        time_retweets = pd.Series(data=df["retweet"].values, index=df["date"])
        time_retweets.plot(figsize=[16, 4], label="retweet", legend=True)
        plt.show()

if __name__ == "__main__":
    twitter_client = TwitterClient ()
    tweet_analyzer = Tweet_analyzer()

    api= twitter_client.get_twitter_client_api()

    tweets = api.user_timeline(screen_name="realDonaldTrump", count=4)

    df = tweet_analyzer.tweets_to_df(tweets)
    df["sentiment"] = np.array([tweet_analyzer.analyse_sentiment(tweet) for tweet in df["Tweets"]])
    print(df)

    # print (np.mean(df["len"])) - kiadja a tweet-ek átlagos hosszát
    # print (np.max(df["likes"])) - kiadja a legtöbbet like-olt tweetet
    # print (np.max(df["retweets"])) - kiadja a legtöbbet retweetelt tweetet

    #time_likes = pd.Series(data = df["retweet"].values, index= df["date"])
    # index az x axis, data az y axis
    #time_likes.plot(figsize = [16,4], color="r")
    #plt.show()




