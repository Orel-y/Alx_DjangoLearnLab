from django.urls import path
from accounts import views
from accounts.views import FollowUserAPIView, UnfollowUserAPIView

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('users/follow/<int:user_id>/', FollowUserAPIView.as_view(), name='follow-user'),
    path('users/unfollow/<int:user_id>/', UnfollowUserAPIView.as_view(), name='unfollow-user'),
]
