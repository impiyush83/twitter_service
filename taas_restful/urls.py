from taas_restful.resource.index import Index
from taas_restful.resource.user.login import Login
from taas_restful.resource.user.signup import Signup
from taas_restful.resource.user.tweet import Tweet
from taas_restful.utils import URLS

urls = [
    URLS(resource=Index, endpoint=[''], name="homepage"),
    URLS(resource=Signup, endpoint=['user/signup'], name="user_signup"),
    URLS(resource=Login, endpoint=['user/login'], name="login_user"),
    URLS(resource=Tweet, endpoint=['user/tweet'], name="post_tweet"),
]
