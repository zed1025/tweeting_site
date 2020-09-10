from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import pre_save
from ckeditor.fields import RichTextField
import uuid


class Tweet(models.Model):
    body = models.TextField(max_length=255, null=False, blank=False)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name='date published')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='date updated')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='tweets')
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.body[:50]

    def clean(self):
        if self.body:
            self.body = self.body.strip()


# creates a slug for the tweet
def pre_save_tweet_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username + '-' + str(uuid.uuid4()))


pre_save.connect(pre_save_tweet_receiver, sender=Tweet)


class Comment(models.Model):
    tweet = models.ForeignKey(Tweet, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.tweet.body[:10], self.name)
