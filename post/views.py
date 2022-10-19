from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponseRedirect
from django.urls import  reverse
# Create your views here.

def post(request):
    postdetails=Post.objects.all()
  
    return render(request, 'index.html', {'postdetails': postdetails})

def LikeView(request, pk):
    post=get_object_or_404(Post, id=request.POST.get('post_id'))
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked =True
    return HttpResponseRedirect(reverse('index', args=[str(pk)]))
    