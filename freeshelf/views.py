from django.shortcuts import render
from .models import User, Resource, Author, Mediatype, Topic

# Create your views here.
def index(request):
    all_resource = Resource.objects.all()
    return render(request, 'freeshelf/index.html',{'all_resource':all_resource})