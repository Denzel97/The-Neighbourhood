from django.shortcuts import render
from django.views.generic import ListView
from .models import *


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'mtaa/home.html', context)


class PostListView(ListView):
    model = Post


def business(request):
    denz = Business.objects.all()
    return render(request, 'mtaa/business.html',locals())
