import tweepy
from bgapi import *
import os


def main():
    # Getting sloks from Bhagavad Gita API
    Slok = Slokm()

    # Tweet Text limit
    Post = (Slok[:277] + "..") if len(Slok) > 280 else Slok

    # Authenticate to Twitter
    api_key = os.environ["APIKey"]
    api_secret = os.environ["APISecretKey"]
    access_token = os.environ["AccessToken"]
    access_token_secret = os.environ["AccessTokenSecret"]
    bearer_token = os.environ["BearerToken"]

    client = tweepy.Client(
        bearer_token, api_key, api_secret, access_token, access_token_secret
    )

    # Tweet Posting
    try:
        status = client.create_tweet(text=Post, user_auth=True)
        print(Post)
        print(status)
        print("Posted")
    except Exception as error:
        print(f"Error during authentication :\n{error}")


if __name__ == "__main__":
    main()
