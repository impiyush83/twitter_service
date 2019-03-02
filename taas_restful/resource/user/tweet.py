from flask import request, make_response, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from taas_restful.constants.common_constants import headers
from taas_restful.models.models import User
from taas_restful.utils.tweepy_client import tweepy_client


class Tweet(Resource):

    def get(self):
        """

    .. http:post::  /user/tweet

        This api will be used to return tweets

        **Example request**:

        .. sourcecode:: http

           GET   /user/tweet  HTTP/1.1

        **Example response**:

        .. sourcecode:: http

           HTTP/1.1 200 OK
           Vary: Accept


        :statuscode 200: responses homepage
        :statuscode 400: bad request error
        :statuscode 404: value error

        """

        response = make_response(render_template('tweet_page.html'), headers)
        return response

    @jwt_required
    def post(self):
        """

    .. http:post::  /user/tweet

        This api will be used to return tweets

        **Example request**:

        .. sourcecode:: http

           POST  /user/tweet  HTTP/1.1

        **Example response**:

        .. sourcecode:: http

           HTTP/1.1 200 OK
           Vary: Accept


        :statuscode 200: responses homepage
        :statuscode 400: bad request error
        :statuscode 404: value error

        """
        try:
            user_email = get_jwt_identity()
            user = User.with_email(user_email)
            data = request.form
            tweet = data.get('tweet_text')

            tweepy_api_client = tweepy_client(
                user.consumer_key,
                user.consumer_secret,
                user.access_token,
                user.access_token_secret
            )

            tweepy_api_client.update_status(tweet)
            response = make_response(render_template('tweet_page.html'), headers)
            return response
        except:
            response = make_response(render_template('400.html'), headers)
            return response
