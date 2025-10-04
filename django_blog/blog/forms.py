from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta():
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

        def clean_title(self):
            title = self.cleaned_data.get('title')
            if len(title) < 5:
                raise forms.ValidationError("Title must be lessa than 5 letter")
            return title