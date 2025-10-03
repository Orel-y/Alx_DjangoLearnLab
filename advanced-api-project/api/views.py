from django.shortcuts import render
from rest_framework import generics, permissions, filters
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListApiView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__name']

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [permissions.AllowAny]

class BookUpdateView(generics.UpdateAPIview):
    query_set = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [permissions.IsAuthenticated]

class BookCreateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [permissions.IsAuthenticated]

    #saves automatically who created the books
    def perform_create(self, serializer):
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [permissions.IsAuthenticated]

