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
def TweetInterval():
    api.update_status("Test")
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

