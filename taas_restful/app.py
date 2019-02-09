from flask import Flask

from taas_restful.flask_restful_api import restful_api


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    restful_api(app)
    return app
