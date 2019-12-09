from django.db import models


# Create your models here.
class Profile(models.Model):
    user_name = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200)


class Offer(models.Model):
    offer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    offer_description = models.TextField()
    tokens_requested = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
