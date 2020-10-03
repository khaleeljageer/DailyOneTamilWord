import twitter
import back4app

from secret_keys import *

"""
This file will make a connection with twitter api and tweet one word
"""

def connect():
    return twitter.Api(consumer_key=MY_CONSUMER_KEY,
                       consumer_secret=MY_CONSUMER_SECRET,
                       access_token_key=MY_ACCESS_TOKEN_KEY,
                       access_token_secret=MY_ACCESS_TOKEN_SECRET)


if __name__ == "__main__":
    api = connect()
    mine = back4app.Back4App()

    status = mine.get_sentance()

    if status is not None and len(status) < 210:
        if not DEBUG:
            if ENABLE_TWITTER_POSTING:
                twitStatus = api.PostUpdate(status)
        print(status)

    elif not status:
        print("Status is empty, sorry.")
    else:
        print("TOO LONG: " + status)
