from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin
from django.urls import reverse

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

class Resource(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, default='Anonymous')
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE, blank=True, null=True, related_name='resources')
    mediatype = models.ForeignKey('Mediatype', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(max_length=1300)
    # if url doesn't work look into this
    url = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

class Topic(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("topic_detail", kwargs={"slug": self.slug})  # new

class Mediatype(models.Model):
    mediatype = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.mediatype}"

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class Favorite(models.Model):
    resource = models.ForeignKey('Resource', on_delete=models.CASCADE, related_name='favorites')
    user = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True, related_name='favorites')
    created_at = models.DateTimeField(auto_now_add=True)
    
