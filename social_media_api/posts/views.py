from rest_framework import viewsets
from posts.models import Post, Comment
from posts.serializers import PostSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import CustomUser
from django.shortcuts import get_object_or_404


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FollowingPage(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        follwoing_user = user.following.all()

        feed_users = list(follwoing_user) + [user]
        posts = Post.objects.filter(author__in=follwoing_user).select_related('author').order_by('-created_at')

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

"""class PostListCreateView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        qs = Post.objects.all()
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            default_user = CustomUser.objects.first()
            serializer.save(author=default_user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetailView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, pk):
        qs = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(qs)

        return Response(serializer.data, status=status.HTTP_200_OK)


    def patch(self, request, pk):
        qs = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(instance=qs, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""