import tweepy
from bgapi import *
import os

"""
import base64
import requests

def generate_bearer_token(api_key, api_secret):
    # URL for Twitter API endpoint to obtain the bearer token
    url = "https://api.twitter.com/oauth2/token"

    # Set up the HTTP Basic Authentication header with API key and API secret key
    auth_headers = {
        "Authorization": f"Basic {base64.b64encode(f'{api_key}:{api_secret}'.encode()).decode()}"
    }

    # Parameters for the POST request to obtain the bearer token
    data = {"grant_type": "client_credentials"}

    # Make the POST request to get the bearer token
    response = requests.post(url, headers=auth_headers, data=data)

    # Parse the response JSON to extract the bearer token
    bearer_token = response.json().get("access_token")

    return bearer_token
import requests

def post_tweet(tweet_text, bearer_token):
    tweet_endpoint = "https://api.twitter.com/2/tweets"
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }
    data = {
        "text": tweet_text
    }
    
    try:
        response = requests.post(tweet_endpoint, headers=headers, json=data)
        response.raise_for_status()
        tweet = response.json()
        return tweet
    except requests.exceptions.HTTPError as e:
        print(f"Error posting tweet: {e}")
        return None

if __name__ == "__main__":
    # Replace 'YOUR_BEARER_TOKEN' with your actual Bearer Token
    bearer_token = 'YOUR_BEARER_TOKEN'
    tweet_text = "Hello, this is my tweet using Twitter API v2 and Python!"

    tweet = post_tweet(tweet_text, bearer_token)
    if tweet:
        print("Tweet successfully posted!")
    else:
        print("Failed to post tweet.")
"""


def main():
    # Getting sloks from Bhagavad Gita API
    Slok = Slokm()

    # Tweet Text limit
    Post = (Slok[:277] + "..") if len(Slok) > 280 else Slok
    print(Post)

    # Authenticate to Twitter
    api_key = os.environ["APIKey"]
    api_secret = os.environ["APISecretKey"]
    access_token = os.environ["AccessToken"]
    access_token_secret = os.environ["AccessTokenSecret"]
    bearer_token = os.environ["BearerToken"]
    # bearer_token = generate_bearer_token(api_key, api_secret)

    # client = tweepy.Client(
     #   consumer_key=api_key,
  #      consumer_secret=api_secret,
  #      access_token=access_token,
 #       access_token_secret=access_token_secret,
 #   )
    auth = tweepy.OAuthHandler(api_key,api_secret)
    auth.set_access_token(access_token, access_token_secret)
    client = tweepy.API(auth)
    # Tweet Posting
    # status = client.create_tweet(text=Post, user_auth=True)
    status = client.update_status(Post)
    print(status)
    print("Posted")


if __name__ == "__main__":
    main()
