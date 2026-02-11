from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment

# -------------------
# User Registration Form
# -------------------
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# -------------------
# Profile Update Form
# -------------------
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

# -------------------
# Post Form
# -------------------
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

# -------------------
# Comment Form
# -------------------
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Assuming Comment model has 'content'
