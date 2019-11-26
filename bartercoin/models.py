from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Profile(models.Model):
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_email = models.CharField(max_length=200)
    headline = models.CharField(max_length=200)
    description = models.TextField()
    barter_options = models.CharField(max_length=200)
    tokens_requested = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.headline
