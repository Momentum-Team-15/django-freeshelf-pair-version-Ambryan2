from importlib import resources
from django.shortcuts import render
from .models import User, Resource, Mediatype, Topic
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    resources = Resource.objects.all()
    topics = Topic.objects.all()
    return render(request, 'freeshelf/index.html',{'resources':resources,'topics':topics})

def topic_detail(request, pk):
    # this is grabbing info from resources database that has matching pk
    resources = Resource.objects.filter(topic=pk)
    return render(request, 'freeshelf/topic_detail.html', {'resources':resources})