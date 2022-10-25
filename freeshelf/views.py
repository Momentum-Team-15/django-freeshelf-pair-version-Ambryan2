from importlib import resources
from django.shortcuts import render
from .models import User, Resource, Mediatype, Topic
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    resources = Resource.objects.all()
    topics = Topic.objects.all()
    return render(request, 'freeshelf/index.html',{'resources':resources,'topics':topics})

# We want topic-detail to load a specific page for each topic
def topic_detail(request, slug):
    # this is grabbing info from resources database that has matching pk
    topic = get_object_or_404(Topic,slug=slug)
    topics = Topic.objects.all()
    return render(request, 'freeshelf/topic_detail.html', {'topic':topic, 'resources':topic.resources.all(),'topics':topics})