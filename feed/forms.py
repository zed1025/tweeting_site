from django import  forms
from feed.models import Tweet


class CreateTweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['body']
