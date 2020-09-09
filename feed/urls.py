from django.urls import path

from feed.views import (
    feed_view,
    create_tweet_view,
    all_tweets_view,
)

urlpatterns = [
    path('', feed_view, name='feed'),
    path('create/', create_tweet_view, name='create'),
    path('all_tweets/', all_tweets_view, name='all_tweets'),
]
