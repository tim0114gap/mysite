from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

def work(request):
    return render(request, 'blog/work.html')

def profile(request):
    return render(request, 'blog/profile.html')

def blog(request):
    latest_post = Post.objects.order_by('-pub_date')[:5]
    context = {'latest_post':latest_post}
    return render(request, '/blog/blog.html',context)
