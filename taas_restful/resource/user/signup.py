from flask import current_app as app, request, render_template, make_response
from flask_restful import Resource

from taas_restful.constants.common_constants import headers
from taas_restful.models.db import db
from taas_restful.models.models import User
from taas_restful.utils.resource_exceptions import exception_handle


class Signup(Resource):

    decorators = [exception_handle]

    def post(self):
        """

    .. http:post::  /user/signup

        This api will be used to signup user

        **Example request**:

        .. sourcecode:: http

           POST  /user/signup  HTTP/1.1


        **Example response**:

        .. sourcecode:: http

           HTTP/1.1 200 OK
           Vary: Accept


        :statuscode 200: responses homepage
        :statuscode 400: bad request error
        :statuscode 404: value error

        """
        request_data = request.get_json()
        User.insert_user(request_data)
        db.commit()
        return make_response(render_template('index.html'), 200, headers)
