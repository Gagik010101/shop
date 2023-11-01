from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Category(models.Model):
    category_name = models.CharField(max_length=100)


class Country(models.Model):
    country_name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    count = models.IntegerField()
    photo = models.ImageField(upload_to='images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    country = models.ManyToManyField(Country)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=3)
# Create your models here.
