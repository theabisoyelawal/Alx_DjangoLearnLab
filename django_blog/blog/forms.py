# blog/forms.py

from django import forms
from .models import Post, Comment
from taggit.forms import TagWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),  # ensures tags appear in the form
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
