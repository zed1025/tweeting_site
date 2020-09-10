from django.urls import path

from feed.views import (
    feed_view,
    create_tweet_view,
    all_tweets_view,
    tweet_detail_view,
    tweet_update_view,
    like_view,
    # dislike_view,
)

urlpatterns = [
    path('', feed_view, name='feed'),
    path('create/', create_tweet_view, name='create'),
    path('all_tweets/', all_tweets_view, name='all_tweets'),
    path('<slug>/', tweet_detail_view, name='tweet_detail'),
    path('<slug>/edit/', tweet_update_view, name='tweet_edit'),
    path('<slug>/like_tweet/', like_view, name='like_tweet'),
    # path('<slug>/dislike_tweet/', dislike_view, name='dislike_tweet'),
]
