from django.shortcuts import render
from .models import *

def home(request):
    posts = Post.objects.all()    
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)

def example(request):
    posts2 = Post2.objects.all()
    context = {
        'posts2': posts2
    }
    return render(request, 'examp.html', context)

def post2(request):
    posts2 = Post2.objects.all()
    context = {
        'posts2': posts2
    }
    return render(request, '#2.html', context)

def post3(request):
    posts2 = Post2.objects.all()
    context = {
        'posts2': posts2
    }
    return render(request, '#3.html', context)

def post4(request):
    posts2 = Post2.objects.all()
    context = {
        'posts2': posts2
    }
    return render(request, '#4.html', context)

def post5(request):
    posts2 = Post2.objects.all()
    context = {
        'posts2': posts2
    }
    return render(request, '#5.html', context)

def post6(request):
    posts2 = Post2.objects.all()
    context = {
        'posts2': posts2
    }
    return render(request, '#6.html', context)