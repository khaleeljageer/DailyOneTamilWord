#import twitter
from __future__ import unicode_literals
import back4app
import toot
import os

from secret_keys import *
from mastodon import Mastodon
from sys import argv


def connect():
    mastodon = Mastodon(access_token = 'GZ4dEVxYNAO3n__fEskXMPf0VMg4aQm0yURL-eJAU9Q',api_base_url = 'https://mastodon.social')
    return mastodon


if __name__ == "__main__":
    api = connect()
    mine = back4app.Back4App()

    status = mine.get_sentance()
    print(status)

    if status is not None and len(status) < 210:
        if not DEBUG:
            post_word=api.toot(status)
        #print(repr(status))
        #print(post_word)

    elif not status:
        print("Status is empty, sorry.")
    else:
        print("TOO LONG: " + status)
