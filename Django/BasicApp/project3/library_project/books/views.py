from django.shortcuts import render

# Create your views here.

from .models import Book
from django.views.generic import ListView

class BookListView(ListView):
    model = Book
    template_name = "book_list.html"
