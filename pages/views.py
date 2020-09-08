from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView


def home_page_view(request):
    if request.user.is_authenticated:
        return redirect('feed')
    return render(request, 'index.html')
