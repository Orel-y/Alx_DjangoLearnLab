from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.contrib import messages

def SignupView(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been created')
            return redirect('users:login')

    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/signup.html', {"form": form})


def home(request):
    return render(request, 'blog/home.html')

def posts(request):
    return render(request, 'blog/posts.html')

def profile(request):
    return render(request, 'blog/profile.html')