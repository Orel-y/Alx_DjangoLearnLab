from django.db import models
from datetime import datetime

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.PositiveSmallIntegerField(
        default=datetime.now().year
    )
    def __str__(self):
        return f'{self.title} by {self.author.name}'
