from django.urls import path

from pages.views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
]