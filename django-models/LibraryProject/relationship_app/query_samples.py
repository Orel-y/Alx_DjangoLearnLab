import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")  
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

author = Author.objects.get(name=author_name)
author.objects.filter(author=author)

library = Library.objects.get(name=library_name)
print("Books in", library.name, ":", [book.title for book in library.books.all()])

Librarian.objects.get(library=)