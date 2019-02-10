import json

from flask import current_app as app
from flask_restful import Resource

from taas_restful.utils.tweepy_client import tweepy_client


class Tweets(Resource):

    def __init__(self):
        app.logger.info('In the constructor of {}'.format(self.__class__.__name__))

    def get(self):
        """

    .. http:get::  /tweets

        This api will be used to return tweets

        **Example request**:

        .. sourcecode:: http

           GET  /tweets  HTTP/1.1

        **Example response**:

        .. sourcecode:: http

           HTTP/1.1 200 OK
           Vary: Accept


        :statuscode 200: responses homepage
        :statuscode 400: bad request error
        :statuscode 404: value error

        """
        data = []
        try:
            tweepy_api_client = tweepy_client()
            tweets = tweepy_api_client.home_timeline()
        except Exception as e:
            return dict(message="Authentication Error"), 400
        if not tweets:
            return dict(message="No Tweets Found"), 400
        for tweet in tweets:
            temp = {}
            tweet_json = tweet.__dict__
            tweet_json_data = tweet_json.get('_json')
            temp['id'] = tweet_json_data.get('id')
            temp['created_at'] = tweet_json_data.get('created_at')
            temp['text'] = tweet_json_data.get('text')
            data.append(temp)
        return json.dumps(data), 200
