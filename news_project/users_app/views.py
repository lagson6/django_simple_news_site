from django.shortcuts import render

# Create your views here.

from models import post , tag
def index (request):

    posts = post.objects.all()

    return render (request,'index.html',{'posts':posts })