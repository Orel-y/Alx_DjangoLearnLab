from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author

def all_books(request):
    return HttpResponse("hello world")