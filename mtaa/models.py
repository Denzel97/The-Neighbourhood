from django.shortcuts import render,redirect
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Location(models.Model):
    city = models.CharField(max_length=30, blank=True)
    hood = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.hood

class Neighbourhood(models.Model):
    user_id = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, related_name='user', null=True)
    hood_name = models.CharField(max_length=30, blank=True)
    location_id = models.ForeignKey(Location, blank=True, on_delete=models.CASCADE, related_name='location', null=True)

    def __str__(self):
        return self.hood_name

class Business(models.Model):
    business_name = models.CharField(max_length=30, blank=True)
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE,related_name='neighbourhood', null=True)
    business_email = models.EmailField(max_length=70,blank=True)

    def __str__(self):
        return self.business_name

    @classmethod
    def search_by_business_name(cls,search_term):
        project = Business.objects.filter(business_name__icontains = search_term)
        return project