import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(24)
    CONSUMER_KEY = os.environ.get("CONSUMER_KEY", default="LnApSdzMCcqeiSjO77zhR6UCi")
    CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET", default="A2X9A0f7GZLiZWI9Pneloif5LmGPhYmP2MkttFiaarpzABMDvO")
    ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", default="877038860-LEABRjOfIqBT2YV6MFBhfERKgqQDVpGLB2UPEEnn")
    ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET", default="ucbLaIGFQVe6FmZlKViMSPPjukf3vnCuPFbBUG2FYZXVq")
