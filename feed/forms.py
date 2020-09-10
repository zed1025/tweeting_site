from django import forms
from feed.models import Tweet, Comment


class CreateTweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['body']


class EditTweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['body']

    def clean_body(self):
        return self.cleaned_data.get('body', '').strip()

    def save(self, commit=True):
        tweet = self.instance
        tweet.body = self.cleaned_data['body']

        if commit:
            tweet.save()
        return tweet


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

    def save(self, commit=True):
        comment = self.instance
        comment.body = self.cleaned_data['body']

        if commit:
            comment.save()
        return comment
