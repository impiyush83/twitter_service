from taas_restful.resource.flutter_tweets import FlutterTweets
from taas_restful.resource.index import Index
from taas_restful.resource.tweets import Tweets
from taas_restful.utils import URLS

urls = [
    URLS(resource=Index, endpoint=[''], name="homepage"),
    URLS(resource=Tweets, endpoint=['tweets'], name="returns_tweets"),
    URLS(resource=FlutterTweets, endpoint=['flutter_tweets'], name="returns_tweets"),
]
