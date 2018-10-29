from flask import Flask, render_template, jsonify, json, url_for, request
import json
import pandas as pd
import requests
from flask_wtf import FlaskForm
from wtforms import StringField
from Twitter import TwitterClient
from Twitter import Tweet_analyzer
import jinja2
import pandas


app = Flask(__name__)


@app.route("/", methods=["GET"])
def home_page():
    return render_template("main.html")

@app.route("/stats", methods=["POST"])
def get_stats():
    account = request.form["account"]
    twitter_client = TwitterClient(account)
    tweet_analyzer = Tweet_analyzer(account)

    #getting the first 10 friends
    #friends = twitter_client.get_friend_list(10)
    #friend_name_list = []
    #for i in friends:
     #   friend_name_list.append(friends.name)

    #getting the first 10 tweets, the statistics table and a chart
    raw_tweets= twitter_client.get_user_timeline_tweets(10)
    tweets = []
    for tweet in raw_tweets:
        tweets.append(tweet.text)

    df = tweet_analyzer.tweets_to_df(raw_tweets)

    return render_template("stats.html",account = account, tweets = tweets, df = df)





if __name__ == '__main__':
    app.run(debug=True)