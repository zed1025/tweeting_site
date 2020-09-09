from django.shortcuts import render, redirect
from feed.forms import CreateTweetForm
from feed.models import Tweet
from django.contrib.auth import get_user_model


User = get_user_model()


def feed_view(request):
    return render(request, 'feed/feed.html')


def create_tweet_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('login')

    form = CreateTweetForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = User.objects.filter(username=user.username).first()
        obj.author = author
        obj.save()
        form = CreateTweetForm()

    context['form'] = form
    return render(request, 'feed/create_tweet.html', context)


def all_tweets_view(request):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('login')

    tweets = Tweet.objects.filter(author=user)
    context['tweets'] = tweets

    return render(request, 'feed/all_tweets.html', context)
