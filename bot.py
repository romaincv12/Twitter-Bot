import tweepy
import time

#Authenticate to twitter
auth = tweepy.OAuthHandler("R4BrLxrDN6UXP0jG0TkxvlWJ6",
                            "jFBVEqhm36810DVFHIIRaxlsq9TNxQLUyaaxmm1eSRQcyKKDnX")
auth.set_access_token("2854605777-3euOzqd0W4f3eR8FE0YXRqANcpOW1gQtrjUinT7", 
                      "OXNFRV25ymJrsSSgh7X7t8CpMOPrffHvqJtz9S4CKoQw9")
#Create API Object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#Create a tweet
def TweetInterval(tweet_):
    api.update_status(tweet_)
    time.sleep(900) #Every 15 minutes

#Get informaton about an user
def GetInformationAboutUser(user_name):
    user = api.get_user(user_name)
    print("User details:")
    print(user.name)
    print(user.description)
    print(user.location)

    print("Last followers")
    for follower in user.followers():
        print(follower.name)

#Update the description of your account
def UpdateDescription(desc):
    api.update_profile(description=desc)


#Get the last tweet in your timeline()
def LastTweetInTimeline():
    timeline = api.home_timeline()
    for tweet in timeline:
        print(f"{tweet.user.name} said {tweet.text}")

#Like the last tweet in your timeline
def LikeLastTweetInTimeline():
    tweets = api.home_timeline(count=1)
    tweet = tweets[0]
    print(f"Liking tweet {tweet.id} of {tweet.author.name}")
    api.create_favorite(tweet.id)

#Like tweet where there is a predefined string in the tweet, the 10 most recent
def LikeTweetWithPredefinedString(pr_tweet):
    for tweet in api.search(q=pr_tweet, lang=fr, rpp=10):
        api.create_favorite(tweet.id)

#Search tweet that contains a predefined words
def FindTweetWithPredefinedWord(prs_tweet):
    for tweet in api.search(q=pr_tweet, lang=fr, rpp=10):
        print(f"{tweet.user.name}:{tweet.text}")

#List the current world trend
def ListTheTrends():
    trends_result = api.trends_place(1) #1 Means worldwide
    for trend in trends_result[0]["trends"]:
        print(trend["name"])
