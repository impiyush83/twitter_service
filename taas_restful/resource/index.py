from wsgiref import headers

from flask import current_app as app
from flask import render_template, make_response
from flask_restful import Resource

from taas_restful.constants.common_constants import headers


class Index(Resource):

    def __init__(self):
        app.logger.info('In the constructor of {}'.format(self.__class__.__name__))

    def get(self):
        """

    .. http:get::  /

        This api will be used to showcase homepage

        **Example request**:

        .. sourcecode:: http

           GET  /  HTTP/1.1

        **Example response**:

        .. sourcecode:: http

           HTTP/1.1 200 OK
           Vary: Accept


        :statuscode 200: responses homepage
        :statuscode 400: bad request error
        :statuscode 404: value error

        """
        return make_response(render_template('index.html'), 200, headers)
