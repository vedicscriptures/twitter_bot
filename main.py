import tweepy
from bgapi import *
import os

# Getting sloks from Bhagavad Gita API
Slok = Slokm()

# Tweet Text limit
Post = (Slok[:277] + "..") if len(Slok) > 280 else Slok

# Authenticate to Twitter
consumer_key = os.environ["APIKey"]
consumer_secret = os.environ["APISecretKey"]
access_token = os.environ["AccessToken"]
access_token_secret = os.environ["AccessTokenSecret"]

client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)

# Tweet Posting
try:
    status = client.create_tweet(text=Post)
    print(Post)
    print(status)
    print("\nPosted")
except Exception as error:
    print(f"Error during authentication :\n{error}")
