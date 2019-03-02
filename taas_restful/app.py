import os

from flask import Flask
from flask_jwt_extended import JWTManager

from taas_restful.flask_restful_api import restful_api


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    restful_api(app)
    app.config['JWT_SECRET_KEY'] = os.urandom(24)
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    app.config['JWT_COOKIE_CSRF_PROTECT'] = False
    jwt = JWTManager(app)
    return app
