from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required



def home(request):
    
    posts= Post.objects.all()
   
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =UploadForm()
        print (form)

    return render(request, 'mtaa/home.html', locals())


class PostListView(ListView):
    model = Post


def business(request):
    denz = Business.objects.all()
    return render(request, 'mtaa/business.html',locals())
