from taas_restful.resource.tweets import Tweets
from taas_restful.utils import URLS

urls = [
    URLS(resource=Tweets, endpoint=['tweets'], name="returns_tweets"),
]
