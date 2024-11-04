from django.shortcuts import render, loader
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Post

# Create your views here.
# class test():
#     template_name = "Hello world"


# def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # template = loader.get_template('myapp/myfirst.html')
    # return HttpResponse("Hello wordl")

class HomeView(ListView):
    model = Post
    template_name = "adminlist_1.html"
    context_object_name = "all_posts_list"
