# SBBP - Simple Bogan Bot Protocol v1
import os
import time
import tweepy
import random
import BoganResponses

# To-Do
# Fix this occasional error within BoganResponses.py
# Traceback (most recent call last):
#   File "c:\Users\Jayden\Desktop\BoganResponses.py", line 108, in <module>
#     print(boganResponses.randomizer(boganResponses))
#   File "c:\Users\Jayden\Desktop\BoganResponses.py", line 34, in randomizer
#     return a
# UnboundLocalError: local variable 'a' referenced before assignment


def create_api():
    consumer_key = "0COZjtyCq8eHT27mk0NEV6W4h"
    consumer_secret = "kaZZecEwpq5M17N9CDrG2L6wATnmtKBZ1hv4jxc7XErK74ymN8"
    access_token = "1187414750168117248-apMKhLUxcbP72QMObueVBNemZVBz13"
    access_token_secret = "WrLSdzjo2qv2jkSIQq7mkfqVJUV1FTeoYIAcDoUjSpuWG"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api


def tweetMachine(api):
    # Random Tweet Generator from BoganBotResponses
    # Probably a better method, but going to brute force
    tweet = BoganResponses.boganResponses.randomizer(BoganResponses)
    api.update_status(tweet)


def main():
    api = create_api()
    while True:
        tweetMachine(api)
        time.sleep(300)


if __name__ == "__main__":
    main()


# To-Do
# A random series of hair growth images that bogan endorses
# I'm still a jew day counter
# Series of potential tweets in a different module (Maybe JSON)
# Automatic follower
# Check time library to see if you can post at specific times of day rather than only intervals
# Sorry man I'm going to orem this weekend
# Pictures of bogan
# Automatic Generator of bogan related images to post from
