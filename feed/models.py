from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import pre_save
import uuid


class Tweet(models.Model):
    body = models.TextField(max_length=255, null=False, blank=False)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name='date published')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='date updated')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
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
