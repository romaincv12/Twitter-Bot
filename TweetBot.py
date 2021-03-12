import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def TweetInterval(api, tweets):
    api.update_status(tweets)

def main():
    api = create_api()
    while True:
        TweetInterval(api, tweets)
        logger.info("Waiting...")
        time.sleep(900) #15 minutes

if __name__ == "__main__":
    main("Write the tweet")