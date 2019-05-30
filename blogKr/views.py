from django.shortcuts import render
from .models import PostKR

# Create your views here.

def indexKr(request):
    return render(request, 'blogKr/indexKr.html')

def workKr(request):
    return render(request, 'blogKr/workKr.html')

def profileKr(request):
    return render(request, 'blogKr/profileKr.html')

def blogKr(request):
    latest_post = PostKR.objects.order_by('-pub_date')[:5]
    context = {'latest_post':latest_post}
    return render(request, 'blogKr/blogKr.html',context)
