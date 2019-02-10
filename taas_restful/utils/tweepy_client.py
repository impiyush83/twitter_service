import tweepy
from flask import current_app as app


def tweepy_client():
    auth = tweepy.OAuthHandler(app.config.get("CONSUMER_KEY"), app.config.get("CONSUMER_SECRET"))
    auth.set_access_token(app.config.get("ACCESS_TOKEN"), app.config.get("ACCESS_TOKEN_SECRET"))
    return tweepy.API(auth)
