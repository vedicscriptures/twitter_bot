import tweepy
from bgapi import *
import os

# Getting sloks from Bhagavad Gita API
Slok = Slokm()

# adding tegs
# Slok += "\n#GitaSlok #BhagavadGitaApi #Radhe #Krishna #ISKCON"

# Tweet Text limit
Post = (Slok[:277] + '..') if len(Slok) > 280 else Slok

# Authenticate to Twitter
auth = tweepy.OAuthHandler(os.environ["APIKey"],os.environ["APISecretKey"])
auth.set_access_token(os.environ["AccessToken"],os.environ["AccessTokenSecret"])
api = tweepy.API(auth)

# Tweet Posting
try:
    api.verify_credentials()
    print("Authentication OK")
    api.update_status(Slok)
    print("Posted")
except:
    print("Error during authentication")