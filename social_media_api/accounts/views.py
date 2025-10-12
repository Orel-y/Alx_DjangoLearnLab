from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework import permissions
from .models import CustomUser
from .serializers import CustomUserSerializer, LoginSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    pass

class FollowUserAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser, id=user_id)
        current_user = request.user

        if target_user == current_user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        current_user.following.add(target_user)
        target_user.followers.add(current_user)

        return Response({"detail": f"You are now following {target_user.username}."}, status=status.HTTP_200_OK)


class UnfollowUserAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser, id=user_id)
        current_user = request.user

        if target_user == current_user:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        current_user.following.remove(target_user)
        target_user.followers.remove(current_user)

        return Response({"detail": f"You have unfollowed {target_user.username}."}, status=status.HTTP_200_OK)

generics.GenericAPIView
CustomUser.objects.all()