from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Library

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {'books': books})