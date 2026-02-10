from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Task: Post list view
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # make sure this template exists
    context_object_name = 'posts'

# Task: Post detail view
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # make sure this template exists
    context_object_name = 'post'
