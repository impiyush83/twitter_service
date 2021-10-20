import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(24)
    CONSUMER_KEY = os.environ.get("CONSUMER_KEY", default="<Your key>")
    CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET", default="<Your key>")
    ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", default="<Your key>")
    ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET", default="<Your key>")
