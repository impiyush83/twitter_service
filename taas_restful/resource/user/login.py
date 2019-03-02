from flask import render_template, make_response
from flask import request
from flask_jwt_extended import set_access_cookies
from flask_restful import Resource

from taas_restful.constants.common_constants import headers
from taas_restful.core.login import user_login
from taas_restful.utils.resource_exceptions import exception_handle


class Login(Resource):
    decorators = [exception_handle]

    def post(self):
        """

    .. http:get::  /user/login

        This api will be used to showcase homepage

        **Example request**:

        .. sourcecode:: http

           GET  /user/login  HTTP/1.1

        **Example response**:

        .. sourcecode:: http

           HTTP/1.1 200 OK
           Vary: Accept


        :statuscode 200: responses homepage
        :statuscode 400: bad request error
        :statuscode 404: value error

        """
        request_data = request.get_json()
        access_token, user = user_login(request_data)
        response = make_response(render_template('tweet_page.html'), headers)
        set_access_cookies(response, access_token)
        return response
