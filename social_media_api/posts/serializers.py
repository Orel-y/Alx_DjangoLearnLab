from rest_framework import serializers
from posts.models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    
    class Meta:
        model = Comment
        fields = [
            'id',
            'author',
            'author_username',
            'content',
            'created_at',
            'updated_at'
        ]

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'author_username'
            'title',
            'content',
            'updated_at',
            'created_at',
            'comments'
        ]
