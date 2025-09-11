```python

# CRUD Operations for Book Model

## CREATE
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", 1949)
book 

# Expected Output:
# <Book: 1984 by George Orwell (1949)>


## RETRIEVE
from bookshelf.models import Book

book = Book.objects.get()
book

# Expected Output:
# ('1984', 'George Orwell', 1949)


## UPDATE
from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book


## DELETE
from bookshelf.models import Book

book = Book.objects.get("Nineteen Eighty-Four")
book.delete()
Book.objects.all()

# Expected Output: <QuerySet []>
