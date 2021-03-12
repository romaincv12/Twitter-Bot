import tweepy

#Authenticate to twitter
auth = tweepy.OAuthHandler("6z38xP3EE8KZ6uAyCnklAfZKZ",
                            "NlNYEqCOpJDQ3I3NIexkXMELF3RTxsQLEiSBfsiojhiaHvhNe6")
auth.set_access_token("2854605777-WCJpjK9W1G2Ab5a3oPNJGRAqEEyFGXOjeSflbRy", 
                      "mz13qxaUsjicmCLUH3VxO3T186qmBNTlyluA7WldBlWLe")
#Create API Object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#Create a tweet