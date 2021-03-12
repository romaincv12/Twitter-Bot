import tweepy
import logging
from config import create_api
import json


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class MyTwitterBot(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print("Error detected")

def main():
    api = create_api()
    tweets_listener = MyTwitterBot(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=["Python", "Django", "Tweepy"], languages=["en"])

if __name__ == "__main__":
    main()