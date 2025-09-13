from relationship_app.models import Author, Book, Library, Librarian

author = Author.objects.get(name=author_name)
author.objects.filter(author=author)

library = Library.objects.get(name=library_name)
print("Books in", [book.title for book in library.books.all()])

Librarian.objects.get(library=)


author = Author.objects.get(name=author_name)