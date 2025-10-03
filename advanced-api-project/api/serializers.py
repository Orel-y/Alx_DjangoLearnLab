from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

"""
    AuthorSerializer and BookSerializer class Defined here
    to convert our python MODELS to JSON format so we can 
    work with the Client and Server side easily.
    
"""
class AuthorSerializer(serializers.ModelSerializer):
    class Meta():
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True, read_only=True)

    class Meta():
        model = Book
        fields = 'id', 'title', 'publication_year', 'author'

    """
        VALIDATING: validating the publication_year data
        so Clients will not send invalid data.
    """
    
    def validate(self, data):
        publication_year = data.get('publication_year')
        if publication_year and publication_year > datetime.now().year:
            raise serializers.ValidationError({
                "publication_year": "What Now! are you a time Traveler fill the form corrctly :("
            })

        return data