from django.contrib import admin
from .models import User, Resource, Author, Mediatype, Topic

# Register your models here.
admin.site.register(User)
admin.site.register(Resource)
admin.site.register(Author)
admin.site.register(Mediatype)
admin.site.register(Topic)
