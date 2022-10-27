from ast import Delete
from importlib import resources
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import User, Resource, Mediatype, Topic, Favorite



# Create your views here.

@login_required
def index(request):
    resources = Resource.objects.all().order_by('-created_at')
    topics = Topic.objects.all()
    return render(request, 'freeshelf/index.html',{'resources':resources,'topics':topics})

# We want topic-detail to load a specific page for each topic
def topic_detail(request, slug):
    # this is grabbing info from resources database that has matching pk
    topic = get_object_or_404(Topic,slug=slug)
    topics = Topic.objects.all()
    return render(request, 'freeshelf/topic_detail.html', {'resources':topic.resources.all(),'topics':topics})

def add_favorite(request, res_pk):
    resource = get_object_or_404(Resource, pk=res_pk)
    unfavorited = False
    for favorite in request.user.favorites.all():
        if resource == favorite.resource:
            favorite.delete()
            unfavorited = True
    if not unfavorited:
        favorite = Favorite.objects.create(resource=resource, user=request.user)
        favorite.save()
    return redirect(request.META['HTTP_REFERER'])

def favorite_page(request):
    favorited = Favorite.objects.filter(user = request.user).order_by('-created_at')
    topics = Topic.objects.all()
    return render(request, 'freeshelf/favorite_detail.html', {'favorited':favorited,'topics':topics})

def logout(request):
    return render(request, 'accounts/logout/')

