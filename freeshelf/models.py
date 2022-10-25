from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

class Resource(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, null=True, blank=True)
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE, blank=True, null=True)
    mediatype = models.ForeignKey('Mediatype', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(max_length=1300)
    # if url doesn't work look into this
    url = models.CharField(max_length=200)
    favorite = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

class Topic(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

class Mediatype(models.Model):
    mediatype = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.mediatype}"

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}