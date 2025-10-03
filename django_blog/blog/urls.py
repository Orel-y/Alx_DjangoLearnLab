from django.urls import path
from .views import SignupView, home, posts
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('posts/', posts, name='posts'),
    path('register/', SignupView, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout')
]
