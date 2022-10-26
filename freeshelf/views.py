from importlib import resources
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import User, Resource, Mediatype, Topic


# Create your views here.

@login_required
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

def select_favorite():
    if request.method == 'POST':
        form = FavoriteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("home")
    else:
        form = FavoriteForm()
    return render (request, 'freeshelf/select_favorite.html', {'form': form})
