from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Posting

class BlogListView(ListView):
    model = Posting
    template_name = "home.html"

class BlogDetailView(DetailView):
    model = Posting
    template_name = "post_detail.html"

class BlogCreateView(CreateView):
    model = Posting
    template_name = "post_new.html"
    fields = ["title", "author", "body"]

class BlogUpdateView(UpdateView):
    model = Posting
    template_name = "post_edit.html"
    fields = ["title", "body"]

class BlogDeleteView(DeleteView):
    model = Posting
    template_name = "post_delete.html"
    success_url = reverse_lazy('blog')
    
