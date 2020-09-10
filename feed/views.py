from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from feed.forms import CreateTweetForm, EditTweetForm
from feed.models import Tweet
from django.contrib.auth import get_user_model
from operator import attrgetter


User = get_user_model()


def feed_view(request):
    context = {}

    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)

    tweets = sorted(get_tweet_queryset(query), key=attrgetter('date_updated'), reverse=True)
    context['tweets'] = tweets
    return render(request, 'feed/feed.html', context)


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


def tweet_detail_view(request, slug):
    context = {}

    tweet = get_object_or_404(Tweet, slug=slug)
    context['tweet'] = tweet
    return render(request, 'feed/tweet_detail.html', context)


def tweet_update_view(request, slug):
    context = {}
    user = request.user

    if not user.is_authenticated:
        return redirect('login')
    # print('\n\n\nSLUG VALUE IS: {}\n\n\n'.format(slug))
    tweet = get_object_or_404(Tweet, slug=slug)

    if request.POST:
        form = EditTweetForm(request.POST or None, instance=tweet)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Updated!"
            tweet = obj

    form = EditTweetForm(
        initial={
            'body': tweet.body,
        }
    )
    print('\n\n\nFORM INITIAL BODY: ', form.initial['body'])
    context['form'] = form
    return render(request, 'feed/edit_tweet.html', context)


def get_tweet_queryset(query=None):
    queryset = []
    print(type(query))
    queries = query.split(" ")
    for q in queries:
        posts = Tweet.objects.filter(
            Q(body__icontains=q) |
            Q(author__username__icontains=q) |
            Q(author__first_name__icontains=q) |
            Q(author__last_name__icontains=q)
        ).distinct()

        for post in posts:
            queryset.append(post)
    return list(set(queryset))
