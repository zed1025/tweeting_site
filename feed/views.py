from django.shortcuts import render


def feed_view(request):
    return render(request, 'feed/feed.html')
