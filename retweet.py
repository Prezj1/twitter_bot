import tweepy
import time
from keys import api_key, secret_key, access_token, access_token_secret

auth = tweepy.OAuthHandler(api_key, secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()

def limit_handle(cursor):
    while True:
        try:
            yield cursor.next()
        except StopIteration:
            return
        except tweepy.RateLimitError:
            time.sleep(300)


search_string = "python"
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print("I liked that tweet")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break