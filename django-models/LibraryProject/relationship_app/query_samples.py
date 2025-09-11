import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")  
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

author = Author.objects.get(name="J.K. Rowling")
print("Books by", author.name, ":", [book.title for book in author.books.all()])

library = Library.objects.get(name="Central Library")
print("Books in", library.name, ":", [book.title for book in library.books.all()])

library = Library.objects.get(name="Central Library")
print("Librarian of", library.name, ":", library.librarian.name)