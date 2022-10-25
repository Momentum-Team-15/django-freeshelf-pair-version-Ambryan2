from django.contrib import admin
from .models import User, Resource, Mediatype, Topic

# Register your models here.
admin.site.register(User)
admin.site.register(Resource)
admin.site.register(Mediatype)
admin.site.register(Topic)